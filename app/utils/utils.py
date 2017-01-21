import paramiko
import re, datetime

def get_last_rev():
    return None


def get_rev_by_id():
    return None


def save_rev():
    return None


# Получение пользователя, который правил конфиг циски
def get_conf_editor(hostname, username, password, type):
    editor = get_conf(hostname, username, password, type)
    n_editor = editor.split()
    return (n_editor[-1])


#Получение даты конфигов циски
def get_conf_date(hostname,username,password,type):
    date_temp = get_conf(hostname,username,password,type)
    hours = re.findall('\d+:\d+:\d+',date_temp)
    date = re.findall('\w{3} \d{2} \d{4}',date_temp)
    time = (''.join(hours)) + ' ' + (''.join(date))
    time = datetime.datetime.strptime(time,'%H:%M:%S %b %d %Y')
    return time

#Получение конфига с циски
def get_conf(hostname,username,password,type):
    port = 3000
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)
    #1,10 - running-config
    #2,20 - startup-config
    if type == 1:
        stdin, stdout, stderr = ssh.exec_command('sh  run view full')
    elif type ==2:
        stdin, stdout, stderr = ssh.exec_command('sh  start')
    elif type == 10:
        stdin, stdout, stderr = ssh.exec_command('sh start | include Last configuration')
    elif type == 20:
        stdin, stdout, stderr = ssh.exec_command('sh start | include NVRAM')
    output = stdout.readlines()
    conf = ''.join(output)
    # print(type(conf))
    ssh.close()
    return conf

#Получение runnning-config с циски
def get_cisco_run_conf():
    return None

#Получение runnning-config с циски
def get_cisco_start_conf():
    return None