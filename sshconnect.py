import os
import paramiko
import requests


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
    if file.startswith(('http', 'https', 'ftp')) == True:
        if file.endswith('zip') == True:

            try:
                local_zip = requests.get(file, stream=True)
                with open("Server\local.zip", "wb") as zip:
                    for chunk in local_zip.iter_content(chunk_size=1024):
                        if chunk:
                            zip.write(chunk)
                    zip.close()
                # sh.raise_for_status()
                # sh.encoding = sh.apparent_encoding
                # print(sh.text)
                # shfile = open('local.zip', "w+")
                # shfile.write(sh.text)
                # shfile.close()
                file = os.getcwd() + "\\Server\\local.zip"
            except:
                return False
    sftp = paramiko.SFTPClient.from_transport(trans)
    sftp.put(file, local)
    trans.close()
    return True

# 下载文件函数
def sshget(ip, port, usern, passwod, file):
    trans = paramiko.Transport((ip, port))
    try:
        trans.connect(username=usern, password=passwod)
    except:
        pass
    sftp = paramiko.SFTPClient.from_transport(trans)
    try:
        download_list = sftp.listdir(file)
        print(download_list)
        print('开始下载'+ file +'文件夹中的文件')
        for i in download_list:
            print('开始下载 ' + i)
            download_singal = file + '/' + i
            download_local = 'Server_Download/' + i
            sftp.get(download_singal, download_local)
    except:
        print('开始下载文件：' + file)
        download_local = 'Server_Download/' + file.rpartition('/')[2]
        try:
            sftp.get(file, download_local)
        except:
            return False
    trans.close()

if __name__ == "__main__":
    pass
    #sshget('192.168.3.213', 22, 'pi', 'raspberry', '/home/pi/skihome.xyzerjdo')
    #sshsend('192.168.3.213', 22, 'pi', 'raspberry', 'https://unlock.skihome.xyz/subscription/build-debian10.sh', '/home/pi/BDX/local.py')

    #with open('build-shell\\test.sh','r') as command:
    #    command_all = command.read().splitlines()
    #print(sshconnect('192.168.3.213', 22, 'pi', 'raspberry', command_all))