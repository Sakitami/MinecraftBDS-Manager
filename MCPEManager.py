#################################################
#                 As you know, I'm a newbie in Python.                       #
#             So there are too many Non-standard code.                #
#        Don't worry about me, despite your suggestions.        #
#               Then I'll thank you for your suggestions.                   #
#################################################
import configparser
import re
import webbrowser
from threading import Thread

# from PySide2.QtUiTools import QUiLoader
from PyQt5 import uic
from PySide2.QtWidgets import QApplication, QMessageBox

from sshconnect import sshconnect, sshsend

# 读取配置数据
config = configparser.ConfigParser()
config.read('config.cfg')

class Minecraft:

    def __init__(self):
        def CheckVersion(self):
            webbrowser.open("https://github.com/Sakitami/MinecraftBDS-Manager/releases", new=0, autoraise=True)
        
        # SSH连接线程函数
        def SSHconnect():
            self.ui.Connect_button.setEnabled(False)
            self.ui.Connect_button.setText('连接中')
            SSH_IP = self.ui.IP_edit.text()
            SSH_Port = self.ui.Port_edit.text()
            SSH_Port = str(SSH_Port)
            SSH_User = self.ui.User_edit.text()
            SSH_Password = self.ui.Password_edit.text()
            
            config.set("SSH", "server_ip", SSH_IP)
            config.set("SSH", "server_port", SSH_Port)
            config.set("SSH", "server_user", SSH_User)
            config.set("SSH", "server_pass", SSH_Password)
            config.write(open("config.cfg", "w"))
            try:
                SSH_Port = int(SSH_Port)
            except:
                self.ui.Connect_button.setText('输入有误')
                self.ui.Connect_button.setEnabled(True)
                return

            if sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password) == True:
                self.ui.Connect_button.setText('连接成功')
            elif sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password) == 'Failed':
                self.ui.Connect_button.setText('连接失败')
                self.ui.Connect_button.setEnabled(True)
                return
            command = ['screen -r BDX']
            check = sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password, command)
            print(check)
            print(check)
            if check .find("screen") != -1:
                self.ui.log_log_text.append(' \n    没有检测到服务端进程！')

        def SSHCONNECT():
            sshconnecT =Thread(target=SSHconnect)
            sshconnecT.start()
            #sshconnecT.join()

        def ServerBuild():
            self.ui.build_build_button.setText('执行中')
            self.ui.build_build_button.setEnabled(False)
            self.ui.progressBar.setRange(0,100)
            self.ui.build_log_text.append('开始构建...')
            self.ui.progressBar.setValue(10)

            # 从config读取SSH
            SSH_IP = config.get("SSH", "server_ip")
            SSH_Port = config.getint("SSH", "server_port")
            SSH_User = config.get("SSH", "server_user")
            SSH_Password = config.get("SSH", "server_user")
            self.ui.build_log_text.append('已读取SSH信息')
            self.ui.progressBar.setValue(15)

            # 读取用户自定义下载地址
            download_url = self.ui.log_save_edit_2.text()
            if  download_url == '':
                download_url = config.get("Server", "download_url")
                self.ui.build_log_text.append('已读取用户自定义下载地址')
                self.ui.progressBar.setValue(17)

            # 本地上传
            if  download_url.startswith(('http', 'https', 'ftp')) != True:
                config.set("Server", "local", download_url)
                config.write(open("config.cfg", "w")) 
                self.ui.build_log_text.append('从本地' + download_url + '获取服务端')

                sshsend(SSH_IP, SSH_Port, SSH_User, SSH_Password, download_url, '/home/pi/BDX/local.py')
                self.ui.progressBar.setValue(21)
                return

            self.ui.build_log_text.append('从 ' +download_url+ '获取服务端')
            f1 = open('build-shell/build-debian10.sh')
            f2 = open('build.sh','r+')
            for s in  f1.readlines():
                f2.write(s.replace('bedrockserver.zip', download_url))
            f1.close()
            f2.close()
            self.ui.progressBar.setValue(20)
        
        self.ui = uic.loadUi('UI/main.ui')

        # SSH连接
        self.ui.Connect_button.clicked.connect(SSHCONNECT)

        # 关于标签页
        self.ui.about_vcheck_button.clicked.connect(CheckVersion)
        
        #一键开服标签页
        self.ui.build_build_button.clicked.connect(ServerBuild)

add = QApplication([])
minecraft = Minecraft()
minecraft.ui.show()
add.exec_()
