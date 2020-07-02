import paramiko

# SSH连接函数
def sshconnect(ip, port, usern, passwod, command=[]):
    try:
        trans = paramiko.Transport((ip, port))
    except:
        return 'Failed'
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

# 发送文件函数
def sshsend(ip, port, usern, passwod, file, local):
    trans = paramiko.Transport((ip, port))
    try:
        trans.connect(username=usern, password=passwod)
    except:
        return False
    sftp = paramiko.SFTPClient.from_transport(trans)
    sftp.put(file, local)
    trans.close()
    return True

#sshsend('192.168.3.213', 22, 'pi', 'raspberry', 'C:\Users\harri\Documents\Github\MinecraftBDS-Manager\error.py', '/home/pi/BDX/local.py')