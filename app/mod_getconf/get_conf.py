import paramiko

def get_cisco_conf(host,username,password,config_type)
    hostname = '5.35.23.196'
    port = 3000
    username = ''
    password = ''

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)
    # stdin, stdout, stderr = ssh.exec_command('sh  vtp status | section VTP V2 Mode')
    stdin, stdout, stderr = ssh.exec_command('sh  run')
    output = stdout.readlines()
    print(''.join(output))
    ssh.close()