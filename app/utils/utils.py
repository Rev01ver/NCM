from app.mod_ncm.models import Host
from app.mod_ncm.models import Configuration

from app.mod_getconf import get_conf

import paramiko
import re, datetime


def get_all_hosts():
    hosts = Host.query.all()
    return hosts


def get_all_configs_by_host_id(host_id):
    print(type(host_id))
    print("in get_all")
    config = Configuration
    configs = Configuration.query.filter(config.id == host_id).all()
    # print(configs + " Config")
    return configs


def get_all_configs():
    configs = Configuration.query.all()
    return configs


#Уведомление о том, что изменения в running-config не сохранены в startup-config
def do_wr(hostname,username,password):
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
