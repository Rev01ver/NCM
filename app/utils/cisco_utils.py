import smtplib
import paramiko
import re, datetime
import difflib
from app.mod_ncm.models import Configuration
# from difflib_data import *


#Проверка была ли циска перезагружена
def was_rebooted(ip,username,password):
    rebooted = get_conf(ip,username,password,5)
    if '! No configuration change since last restart' in rebooted:
        rebooted = 'Yes'
    else:
        rebooted = 'No'
    return rebooted


    #обрезка шапки
    run_config = get_conf(ip, username, password, 1)
    run_s = run_config.find("version ")
    run_config = run_config[run_s:-1]
    start_config = get_conf(ip, username, password, 2)
    start_s = start_config.find("version ")
    start_config = start_config[start_s:-1]

    #отличия running-config
    diff_run = difflib.ndiff(run_config.splitlines(), start_config.splitlines())
    diff_run ='\n'.join(x[2:] for x in diff_run if x.startswith('- '))

    #отличия startup-config
    diff_start = difflib.ndiff(run_config.splitlines(), start_config.splitlines())
    diff_start ='\n'.join(x[2:] for x in diff_start if x.startswith('+ '))

    df = "Difference:\n------\n<<<Running-config>>>\n{}\n\n<<<Startup-config>>>\n{}\n".format(diff_run,diff_start)
    return df


#проверка того, что running config не сохранен
def need_save(ip,username,password):
    alarm = do_wr(ip,username,password)
    if alarm == 1:
        run_edit_date = get_conf_date(ip, username, password, 10)
        run_save_date = get_conf_date(ip, username, password, 11)
        unsafe_date = datetime.datetime.today()-run_edit_date
        diff = compare_config(ip, username, password)
        mail_me('Need to save running-config on {}'.format(ip),
                'Hey Dude,\n'
                'You need to save running-config to startup-config, in order to avoid loss of configuration '
                'of device with IP address:{}.\n'
                'Last edit of running-config: {}\n'
                'Last save of running-config: {}\n'
                'Your device is working in unsafe state (hours):{}\n\n'
                '{}'.format(ip,
                               run_edit_date,
                               run_save_date,
                               unsafe_date,
                               diff
                               ),
                'Cisco Admin<j-botman@mail.ru>')

    return 0


#проверка даты на cisco (секунды не берем в расчет)
def check_date(ip,username,password):
    cisco_date = get_conf_date(ip, username, password, 3)
    today_time = datetime.datetime.strftime(datetime.datetime.today(),"%Y-%m-%d %H:%M")
    cisco_date = datetime.datetime.strftime(cisco_date,"%Y-%m-%d %H:%M")
    if cisco_date != today_time:
        bad_date = 1
    else:
        bad_date = 0
    return bad_date


#Уведомление о том, что изменения в running-config не сохранены в startup-config
def do_wr(ip,username,password):
    run_edit_date = get_conf_date(ip, username, password, 10)
    run_save_date = get_conf_date(ip, username, password, 11)
    print(run_save_date)
    rebooted = was_rebooted(ip, username, password)
    if rebooted == 'Yes':
        alarm = 0
    elif run_save_date == None:
        alarm = 1
    elif run_save_date != None and run_save_date < run_edit_date:
        alarm = 1
    return alarm

# Получение пользователя, который правил конфиг циски
def get_conf_editor(ip, username, password, type):
    editor = get_conf(ip, username, password, type)
    n_editor = editor.split()
    return (n_editor[-1])


#Получение даты конфигов циски
def get_conf_date(ip,username,password,type):
    date_temp = get_conf(ip,username,password,type)
    if not date_temp:
        # time = datetime.datetime.strftime(datetime.datetime.today(),'%H:%M:%S %b %d %Y')
        time = None
    else:
        hours = re.findall('\d+:\d+:\d+',date_temp)
        date = re.findall('\w{3} \d+ \d{4}',date_temp)
        time = (''.join(hours)) + ' ' + (''.join(date))
        time = datetime.datetime.strptime(time,'%H:%M:%S %b %d %Y')
    # print(time)
    return time

#Получение конфига с циски
def get_conf(ip,username,password,type):
    port = 3000
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port, username, password)
    #1,10 - running-config
    #2,20 - startup-config
    if type == 1:
        stdin, stdout, stderr = ssh.exec_command('sh run view full')
    elif type == 2:
        stdin, stdout, stderr = ssh.exec_command('sh start')
    elif type == 3:
        stdin, stdout, stderr = ssh.exec_command('sh clock')
    elif type == 5:
        stdin, stdout, stderr = ssh.exec_command('sh run | include No configuration')
    elif type == 10:
        stdin, stdout, stderr = ssh.exec_command('sh run | include Last configuration')
    elif type == 11:
        stdin, stdout, stderr = ssh.exec_command('sh run | include NVRAM')
    output = stdout.readlines()
    conf = ''.join(output)
    ssh.close()
    return conf

#Редактирование конфига
# def write_conf(ip,username,password,type):
#     port = 3000
#     ssh = paramiko.SSHClient()
#     ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     ssh.connect(ip, port, username, password)
#     if type == 20:
#         stdin, stdout, stderr = ssh.exec_command('copy run start')
#     elif type ==2:
#         stdin, stdout, stderr = ssh.exec_command('sh start')
#     elif type ==3:
#         stdin, stdout, stderr = ssh.exec_command('sh clock')
#     elif type == 10:
#         stdin, stdout, stderr = ssh.exec_command('sh run | include Last configuration')
#     elif type == 20:
#         stdin, stdout, stderr = ssh.exec_command('sh run | include NVRAM')
#     output = stdout.readlines()
#     conf = ''.join(output)
#     ssh.close()
#     return conf

#Получение runnning-config с циски
# def get_cisco_run_conf(ip, username, password):
#     return get_conf(ip, username, password, 1)

# Получение startup-config с циски
def get_cisco_start_conf(ip, username, password):
    return get_conf(ip, username, password, 2)

# Получение runnning-config с циски
def get_cisco_run_conf(hostname, host_id, username, password):
    conf = Configuration()
    conf.host_id = host_id
    conf.config_type = 'runnning-config'
    conf.datetime = get_conf_date(hostname, username, password, 10)
    conf.data = get_conf(hostname, username, password, 1)
    return conf


#Уведомление админа по email
def mail_me(subj,msg_txt,toaddr):
    # От кого:
    fromaddr = 'NCM notify <ncm_notify@mail.ru>'

    # Создаем письмо (заголовки и текст)
    msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromaddr, toaddr, subj, msg_txt)
    username = 'ncm_notify'
    password = '123456Zz'
    server = smtplib.SMTP('smtp.mail.ru:587')

    # Лог работы с сервером (для отладки 1 = True)
    server.set_debuglevel(0);

    # Переводим соединение в защищенный режим TLS
    server.starttls()

    # Проводим авторизацию:
    server.login(username, password)

    # Отправляем письмо:
    server.sendmail(fromaddr, toaddr, msg)

    # Закрываем соединение с сервером
    server.quit()
    return