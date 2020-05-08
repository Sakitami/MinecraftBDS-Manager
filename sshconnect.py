import paramiko

def sshconnect(ip, port, usern, passwod, command):
    trans = paramiko.Transport((ip, port))
    trans.connect(username=usern, password=passwod)
    ssh = paramiko.SSHClient()
    ssh._transport = trans 
    try:
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        trans.close()
    except:
        print('执行失败！')
        trans.close()

#sshconnect('pi', 'raspberry')
#sshcommand('screenfetch')