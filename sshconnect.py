import paramiko

def sshconnect(user, passwd):
    trans.connect(username=user, password=passwd)

def sshcommand(command):
    ssh = paramiko.SSHClient()
    ssh._transport = trans 
    try:
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())
    except:
        print('执行失败！')

def sshclose():
    trans.close()

#sshconnect('pi', 'raspberry')
#sshcommand('screenfetch')