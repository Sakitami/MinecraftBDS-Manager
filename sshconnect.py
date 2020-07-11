import os
import paramiko
import requests
from gevent.socket import wait_read
from paramiko import SSHClient, AutoAddPolicy

class MySSHClient(SSHClient):


    def _forward_bound(self, channel, callback, *args):
        try:
            while True:
                wait_read(channel.fileno())
                data = channel.recv(1024)
                if not len(data):
                    return
                callback(data, *args)
        finally:
            self.close()


    def run(self, command, callback, *args):
        stdin, stdout, stderr = self.exec_command(
            command, get_pty=True
        )
        self._forward_bound(stdout.channel, callback, *args)

        return stdin, stdout, stderr


# SSH连接函数
def sshconnect(ip, port, usern, passwod, log=None, command=None, show=True):
    def console(text):
        #print(text)
        texxt = str(text,encoding='utf-8')
        print(texxt)
        if command == 'cd wine-5.12; ./configure --enable-win64 --without-freetype; make; make install':
        #if command = 'cd wine-5.12; ./configure --enable-win64 --without-freetype; make; make install':
            pass
        elif show == False:
            pass
        else:
            with open('Snap/' + log, 'a') as f:
                f.write(texxt)
        # 删除空行
        #count = len(open('Snap/' + log, 'r').readlines())
        #file1 = open('Snap/' + log, 'r', encoding='utf-8') 
        #file2 = open('Snap/2' + log, 'w', encoding='utf-8')
        #try:
        #    for line in file1.readlines():
        #        if line == '\n':
        #            line = line.strip("\n")
        #        file2.write(line)
        #finally:
        #    file1.close()
        #    file2.close()
        #    os.remove('Snap/' + log)
        #    os.rename('Snap/2' + log,'Snap/' + log)
        #    f.close()
    ssh = MySSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(ip, port, usern, passwod)
    #ssh.connect(ip, port, usern, passwod)
    #try:
    #    trans = paramiko.Transport((ip, port))
    #except:
    #    return 'Failed'
    #try:
    #    trans.connect(username=usern, password=passwod)
    #except:
    #    return 'Failed'
    #ssh = paramiko.SSHClient()
    #ssh._transport = trans 
    if not command == None:
        #command_all = 'clear;'
        #for i in command:
        #    command_temp = i + ' ;'
        #    command_all = command_all + command_temp
        #print(command_all)
        try:
            stdin, stdout, stderr = ssh.run(command,console)
        #texxt232 = str(console,encoding='utf-8')
        #print(texxt232)
            #console = str(console,encoding='utf-8')
            #print(stdout)
            #stdin, stdout, stderr = ssh.exec_command(i,get_pty=True)
                #print(stdout.read().decode())
            #return stdout.read().decode()
            #bytess = stderr.channel.recv_exit_status()
            #print(bytess)
            #str(bytess,encoding='utf-8')
            ssh.close()
            return True
        except:
            print('Failed')
            ssh.close()
            return False
    else:
        ssh.close()
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

# 获取文件夹列表函数
def sshdirlist(ip, port, usern, passwod, dirname):
    trans = paramiko.Transport((ip, port))
    try:
        trans.connect(username=usern, password=passwod)
    except:
        pass
    sftp = paramiko.SFTPClient.from_transport(trans)
    try:
        dir_list = sftp.listdir(dirname)
        return dir_list
    except:
        return []
if __name__ == "__main__":
    pass