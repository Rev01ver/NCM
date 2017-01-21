import paramiko


def get_cisco_conf(host, username, password, config_type):
    port = 3000

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, username, password)
    # stdin, stdout, stderr = ssh.exec_command('sh  vtp status | section VTP V2 Mode')
    stdin, stdout, stderr = ssh.exec_command('sh  run')
    output = stdout.readlines()
    print(''.join(output))
    ssh.close()
    return ''.join(output)
