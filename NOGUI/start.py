import configparser
import os

import paramiko

from sshconnect import sshconnect

def showinterface1(info=''):
    os.system('clear')
    print('='*20)
    print('Mincraft PE Manager\nSuitable for BDX\nNO GUI version(v0.0.1)')
    print('='*20)
    print(info)

def showinterface2(info=''):
    os.system('clear')
    print('='*20)
    print('Mincraft PE Manager\nNO GUI version')
    print('='*20+'\n提示：'+info +'\n'+'='*20 + '\n功能：'+'\n '+'\n1.搭建服务端(Debian9或以上，基于BDX)\n2.输入指令\n3.上传插件\n4.退出程序\n'+'='*20)

def checkbedrock():
    if not os.path.exists('/root/BDX/bedrock_server.exe'):
        info = '没有检测到BDX服务端！'
        return info
    else:
        return True

def setssh():
    # 保存SSH配置
    ip = input('请输入服务器ip地址：')
    while True:
        port = input('请输入服务器端口号：')
        if port.isdecimal() == True:
            try:
                port = int(port)
            except:
                showinterface1('非法输入，请重新输入！')
                continue
            if port >= 65535 or port <=1:
                showinterface1('非法输入，请重新输入！')
                continue
            break
        else:
            showinterface1('非法输入，请重新输入！')

    while True:
        user = input('请输入服务器用户名：')
        if user.isalnum() == True:
            break
        else:
            showinterface1('非法输入，请重新输入！')
    passwd = input('请输入密码：')

    ssh['SSH'] = {
        'ip':ip,
        'port':port,
        'username':user,
        'password':passwd
    }
    with open('ssh.cfg', 'w') as configfile:
        ssh.write(configfile)

ssh = configparser.ConfigParser()
config = configparser.ConfigParser()

showinterface1()
if os.path.isfile('ssh.cfg'):
    sshcheck = input('检测到已存在的SSH配置，是否使用默认配置？[y/N]:')
    if sshcheck == 'N':
        setssh()

# 读取ssh.cfg
setssh()
ssh.read('ssh.cfg')
ssh_remote = ssh.items('SSH')

os.system('clear')
info = checkbedrock()
showinterface2(info)
while True:
    showinterface2()
    func = input('请选择一个功能：')
    try:
        func = int(func)
    except:
        os.system('clear')
        showinterface2('非法输入，请重新输入！')
    
    if func == 1:
        process = os.system('pidof bedrock_server.exe')
        process = str(process)
        if process.isdecimal() == True:
            check = input('检测到其他PE服务端，是否终止？[n/Y]:')
            if check == 'Y':
                os.system('kill '+process)
            else:
                continue
        if checkbedrock() != True:
            process = os.system('python3 Build.py')
            continue
        else:
            check = input('检测到已安装的BDX服务端，是否删除？[n/Y]:')
            if check == 'Y':
                os.system('rm -rf /root/BDX/ && python3 Build.py')
                continue
            else:
                continue
    
    elif func == 2:
        showinterface2()
        command = input('请输入指令:\n> ')
        sshconnect(ssh_remote[0][1], ssh_remote[1][1], ssh_remote[2][1], ssh_remote[3][1], command)
        break
        #sshcommand('screen -r MinecraftPEManager')
