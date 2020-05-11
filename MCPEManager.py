from PySide2.QtWidgets import QApplication, QMessageBox
#from PySide2.QtUiTools import QUiLoader
from PyQt5 import uic
from sshconnect import sshconnect


# 初始化变量
Server_name = ''
SSH_IP = ''
SSH_Port = ''
SSH_User = ''
SSH_Password = ''
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
        
        def SSHconnect():
            print(SSH_IP + SSH_Port + SSH_User + SSH_Password)
            #check_connect = sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password)
            #if check_connect:
            #   QMessageBox.about(self.ui,
            #        '统计结果',
            #        '''薪资20000 以上的有：\n
            #        \n薪资20000 以下的有：'''
            #        )
            #else:
            #    QMessageBox.about(self.ui,
            #        '统计结果0',
            #        '''薪资20000 以上的有：\n
            #       \n薪资20000 以下的有：\n'''
            #       )               

        self.ui = uic.loadUi('UI/main.ui')
        self.ui.IP_edit.textChanged.connect(getIPText)
        self.ui.Port_edit.textChanged.connect(getPortText)
        self.ui.User_edit.textChanged.connect(getUserText)
        self.ui.Password_edit.textChanged.connect(getPasswordText)
        self.ui.Connect_button.clicked.connect(SSHconnect)
        
        self.ui.control_servername_edit.textChanged.connect(getservernameText)

add = QApplication([])
minecraft = Minecraft()
minecraft.ui.show()
add.exec_()