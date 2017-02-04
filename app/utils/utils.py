from app.mod_ncm.models import Host, Configuration, User

import paramiko
import re, datetime


def get_all_hosts():
    hosts = Host.query.all()
    return hosts


def get_host_by_id(host_id):
    return Host.query.filter(Host.id == host_id).first()


def get_user_by_id(user_id):
    return User.query.filter(User.id == user_id).first()


def get_all_configs_by_host_id(host_id):
    return Configuration.query.filter(Configuration.host_id == host_id).all()


def get_all_configs():
    configs = Configuration.query.all()
    return configs


def get_config_by_id(config_id):
    return Configuration.query.filter(Configuration.id == config_id).first()


# проверка даты на cisco (секунды не берем в расчет)
def check_date(hostname, username, password):
    cisco_date = get_conf_date(hostname, username, password, 3)
    today_time = datetime.datetime.strftime(datetime.datetime.today(), "%Y-%m-%d %H:%M")
    cisco_date = datetime.datetime.strftime(cisco_date, "%Y-%m-%d %H:%M")
    if cisco_date != today_time:
        bad_date = 1
    else:
        bad_date = 0
    return bad_date


# Уведомление о том, что изменения в running-config не сохранены в startup-config
def do_wr(hostname, username, password):
    print(hostname, username, password)
    run_save_date = get_conf_date(hostname, username, password, 10)
    start_save_date = get_conf_date(hostname, username, password, 20)
    if start_save_date < run_save_date:
        alarm = 1
    else:
        alarm = 0
    return alarm


# Получение пользователя, который правил конфиг циски
def get_conf_editor(hostname, username, password, type):
    editor = get_conf(hostname, username, password, type)
    n_editor = editor.split()
    return (n_editor[-1])


# Получение даты конфигов циски
def get_conf_date(hostname, username, password, type):
    date_temp = get_conf(hostname, username, password, type)
    print(date_temp)
    hours = re.findall('\d+:\d+:\d+', date_temp)
    print(hours)
    date = re.findall('\w{3} \d{2} \d{4}', date_temp)
    print(date)
    time = hours[0] + ' ' + date[0]
    time = datetime.datetime.strptime(time, '%H:%M:%S %b %d %Y')
    return time


# Получение конфига с циски
def get_conf(hostname, username, password, type):
    port = 3000
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)
    # 1,10 - running-config
    # 2,20 - startup-config
    if type == 1:
        stdin, stdout, stderr = ssh.exec_command('sh run view full')
    elif type == 2:
        stdin, stdout, stderr = ssh.exec_command('sh start')
    elif type == 3:
        stdin, stdout, stderr = ssh.exec_command('sh clock')
    elif type == 10:
        stdin, stdout, stderr = ssh.exec_command('sh start | include Last configuration')
    elif type == 20:
        stdin, stdout, stderr = ssh.exec_command('sh start | include NVRAM')
    output = stdout.readlines()
    conf = ''.join(output)
    # print(type(conf))
    ssh.close()
    return conf


# Получение runnning-config с циски
def get_cisco_run_conf(hostname, host_id, username, password):
    conf = Configuration()
    conf.host_id = host_id
    conf.config_type = 'runnning-config'
    conf.datetime = get_conf_date(hostname, username, password, 1)
    conf.data = get_conf(hostname, username, password, 1)
    return conf


# Получение runnning-config с циски
def get_cisco_start_conf(hostname, username, password):
    return get_conf(hostname, username, password, 2)
