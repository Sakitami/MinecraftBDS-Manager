#################################################
#                 As you know, I'm a newbie in Python.                       #
#             So there are too many Non-standard code.                #
#        Don't worry about me, despite your suggestions.        #
#               Then I'll thank you for your suggestions.                   #
#################################################
import configparser
import webbrowser
import re
#from PySide2.QtUiTools import QUiLoader
from PyQt5 import uic
from PySide2.QtWidgets import QApplication, QMessageBox

from sshconnect import sshconnect

# 初始化变量
Server_name = ''
SSH_IP = ''
SSH_Port = ''
SSH_User = ''
SSH_Password = ''

# 读取配置数据
config = configparser.ConfigParser()
config.read('config.cfg')

class Minecraft:

    def __init__(self):

        def getservernameText(self):
            Server_name = self
        def getIPText(self):
            SSH_IP = self
        def getPortText(self):
            SSH_Port = self
        def getUserText(self):
            SSH_User = self
        def getPasswordText(self):
            SSH_Password = self
        
        def CheckVersion(self):
            webbrowser.open("https://github.com/Sakitami/MinecraftBDS-Manager/releases", new=0, autoraise=True)
        
        def SSHconnect():
            print(SSH_IP + SSH_Port + SSH_User + SSH_Password)     

        def ServerBuild():
            url_head = ('http', 'https', 'ftp')
            self.ui.progressBar.setRange(0,10)
            self.ui.build_build_button.setEnabled(False)
            self.ui.build_log_text.append('开始构建...')
            self.ui.progressBar.setValue(1)
            download_url = self.ui.log_save_edit_2.text()
            if  download_url == '':
                download_url = config.get("Server", "download_url")

            if not download_url.startswith(url_head) == True:
                print()

            self.ui.build_log_text.append('从 ' +download_url+ '获取服务端')
            f1 = open('build-shell/build-debian10.sh')
            f2 = open('build.sh','r+')
            for s in  f1.readlines():
                f2.write(s.replace('bedrockserver.zip', download_url))
            f1.close()
            f2.close()
            self.ui.progressBar.setValue(2)
        
        self.ui = uic.loadUi('UI/main.ui')

        # SSH连接
        self.ui.IP_edit.textChanged.connect(getIPText)
        self.ui.Port_edit.textChanged.connect(getPortText)
        self.ui.User_edit.textChanged.connect(getUserText)
        self.ui.Password_edit.textChanged.connect(getPasswordText)
        self.ui.Connect_button.clicked.connect(SSHconnect)
        self.ui.control_servername_edit.textChanged.connect(getservernameText)

        # 关于标签页
        self.ui.about_vcheck_button.clicked.connect(CheckVersion)
        
        #一键开服标签页
        self.ui.build_build_button.clicked.connect(ServerBuild)
add = QApplication([])
minecraft = Minecraft()
minecraft.ui.show()
add.exec_()
