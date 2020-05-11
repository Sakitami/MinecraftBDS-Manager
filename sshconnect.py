import paramiko

def sshconnect(ip, port, usern, passwod, command=[]):
    trans = paramiko.Transport((ip, port))
    try:
        trans.connect(username=usern, password=passwod)
    except:
        return 'Failed'
    ssh = paramiko.SSHClient()
    ssh._transport = trans 
    if not command == []:
        print(command[0])
        command_all = 'clear;'
        for i in command:
            command_temp = i + ' ;'
            command_all = command_all + command_temp
        print(command_all)

        try:
            stdin, stdout, stderr = ssh.exec_command(command_all,get_pty=True)
            return stdout.read().decode()

        except:
            print('执行失败！')
        trans.close()
    else:
        trans.close()
        return True