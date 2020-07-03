"""
    As you know, I'm a newbie in Python.
        So there are too many Non-standard code.
            Don't worry about me, despite your suggestions.
                Then I'll thank you for your suggestions.
"""
import configparser
import re
import webbrowser
import os
import shutil
import time

from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from sshconnect import sshconnect, sshsend


# 读取配置数据
config = configparser.ConfigParser()
config.read('config.cfg')

# 多线程
# SSH连接线程命令
class SSH(QThread):
    OutPut = pyqtSignal(str)
    OutProgress = pyqtSignal(int)
    OutConsole = pyqtSignal(str)

    def __init__(self, parent=None):
        super(SSH, self).__init__(parent)
        self.connecting = True

    def __del__(self):
        self.connceting = False
        # self.wait()
    def run(self):
        SSH_IP = config.get("SSH", "server_ip")
        SSH_Port = config.get("SSH", "server_port")
        SSH_User = config.get("SSH", "server_user")
        SSH_Password = config.get("SSH", "server_pass")
        try:
            SSH_Port = int(SSH_Port)
        except:
            self.OutPut.emit('输入有误')
            self.connecting = False
            return
        if sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password) == True:
            self.OutPut.emit('连接成功')
            self.OutProgress.emit(100)
            self.connecting = False
        elif sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password) == 'Failed':
            self.OutPut.emit('连接失败')
            self.OutProgress.emit(0)
            self.connecting = False
            return
        command = ['screen -r EZ']
        check = sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password, command)
        if check .find("screen") == True:
            self.OutConsole.emit(' \n没有检测到服务端进程！')
            return
        else:
            #command = 'scp -r '+ SSH_User+'@'+''
            #os.system('')
            #sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password, '')
            return

# 一键搭建线程命令
class Build(QThread):
    consoleOutPut = pyqtSignal(str)
    OutProgress = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super(Build, self).__init__(parent)
        self.building = True
    def __del__(self):
        self.building = False
        # self.wait()
    def run(self):
        # 从config读取SSH
        SSH_IP = config.get("SSH", "server_ip")
        SSH_Port = config.getint("SSH", "server_port")
        SSH_User = config.get("SSH", "server_user")
        SSH_Password = config.get("SSH", "server_pass")
        self.consoleOutPut.emit('已读取SSH信息')
        # time.sleep(5)

        # 验证SSH连接
        if sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password) == True:
            self.consoleOutPut.emit('SSH连接有效！')
            self.OutProgress.emit(17)
            # time.sleep(4)

        elif sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password) == 'Failed':
            self.consoleOutPut.emit('SSH连接失败！')
            return
        download_url = config.get("Server", "download_user")

        # 使用默认下载地址
        if download_url == '':
            download_url = config.get("Server", "download_url")
            self.consoleOutPut.emit('使用默认下载地址')
            self.OutProgress.emit(20)
            try:
                with open('build-shell\\build-debian10.sh','r') as command:
    	            command_all = command.read().splitlines()
                self.consoleOutPut.emit(sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password, command_all))
            except:
                self.consoleOutPut.emit("上传失败！")
            return

        # 本地上传
        elif download_url.startswith(('http', 'https', 'ftp')) != True:
            self.consoleOutPut.emit('从本地 \'' + download_url + ' \'获取服务端')
            #time.sleep(5)
            self.OutProgress.emit(20)
            try:
                sshsend(SSH_IP, SSH_Port, SSH_User, SSH_Password, download_url, '/root/EZ/local.zip')
            except:
                self.consoleOutPut.emit("上传失败！")
            return

        # 使用用户自定义下载地址
        elif download_url.startswith(('http', 'https', 'ftp')) == True:
            self.consoleOutPut.emit('使用用户自定义下载地址')
            self.ui.progressBar.setValue(20)
            try:
                sshsend(SSH_IP, SSH_Port, SSH_User, SSH_Password, download_url, '/root/EZ/local.zip')
            except:
                self.consoleOutPut.emit("上传失败！")
            return

# 服务器控制线程命令
class Control(QThread):
    OutProgress = pyqtSignal(int)
    OutPut = pyqtSignal(str)

    def __init__(self, parent=None):
        super(Control, self).__init__(parent)
        self.saving = True
    def __del__(self):
        self.saving = False
        # self.wait()
    def run(self):
        config.get("CONTROL", 'gamemode')
        config.get("CONTROL", 'allow-cheats')
        config.getint("CONTROL", 'max-players')
        config.get("CONTROL", 'online-mode')
        config.get("CONTROL", 'white-list')
        config.getint("CONTROL", 'view-distance')
        config.getint("CONTROL", 'tick-distance')
        config.getint("CONTROL", 'player-idle-timeout')
        config.getint("CONTROL", 'max-threads')
        config.get("CONTROL", 'default-player-permission-level')
        config.get("CONTROL", 'texturepack-required')
        config.get("CONTROL", 'content-log-file-enabled')
        config.getint("CONTROL", 'compression-threshold')
        config.getint("CONTROL", 'server-port')
        config.getint("CONTROL", 'server-portv6')
        shutil.copy('Server/server.properties.cfg', 'Server/server.properties')

# 界面操作
class Minecraft:
    def __init__(self,parent=None):
        self.ui = uic.loadUi('UI/main.ui')
        # 关于标签页
        self.ui.about_vcheck_button.clicked.connect(self.CheckVersion)
        #一键开服标签页
        self.Build_QThread = Build()
        self.ui.build_build_button.clicked.connect(self.Build_Start)
        self.Build_QThread.consoleOutPut.connect(self.Build_Console_Show)
        self.Build_QThread.OutProgress.connect(self.ProgressBar)

        # SSH连接
        self.SSH_QThread = SSH()
        self.ui.Connect_button.clicked.connect(self.SSH_Start)
        self.SSH_QThread.OutPut.connect(self.SSH_Show)
        self.SSH_QThread.OutProgress.connect(self.ProgressBar)
        self.SSH_QThread.OutConsole.connect(self.Console)

        # 服务器控制
        self.Control_QThread = Control()
        self.ui.control_save.clicked.connect(self.Control_Start)

    # 关于页面相关控件
    def CheckVersion(self):
        webbrowser.open("https://github.com/Sakitami/MinecraftBDS-Manager/releases", new=0, autoraise=True)

    # SSH连接信号与界面逻辑
    def SSH_Start(self):
        self.ui.Connect_button.setEnabled(False)
        self.ui.Connect_button.setEnabled(False)
        self.ui.IP_edit.setEnabled(False)
        self.ui.Port_edit.setEnabled(False)
        self.ui.User_edit.setEnabled(False)
        self.ui.Password_edit.setEnabled(False)
        self.ui.progressBar.setRange(0,100)
        self.ui.Connect_button.setText('连接中')
        self.ui.progressBar.setValue(10)
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
        self.SSH_QThread.start()
    def SSH_Show(self, button_show):
        self.ui.Connect_button.setText(button_show)
        if button_show == '连接成功':
            self.ui.progressBar.setValue(100)
            config.set("SSH", "connected", '1')
            config.write(open("config.cfg", "w"))
            #self.SSH_QThread.stop
            return
        self.ui.progressBar.reset()
        self.ui.Connect_button.setEnabled(True)
        self.ui.IP_edit.setEnabled(True)
        self.ui.Port_edit.setEnabled(True)
        self.ui.User_edit.setEnabled(True)
        self.ui.Password_edit.setEnabled(True)

    # 一键开服信号与界面逻辑
    def Build_Start(self):
        self.ui.build_build_button.setText('执行中')
        self.ui.build_build_button.setEnabled(False)
        self.ui.progressBar.setRange(0,100)
        self.ui.build_log_text.clear()
        self.ui.build_log_text.append('开始构建...')
        self.ui.progressBar.setValue(10)
        download_user = self.ui.log_save_edit_2.text()
        config.set("Server", "local", download_user)
        config.write(open("config.cfg", "w")) 
        self.Build_QThread.start()
    def Build_Console_Show(self, console_txt):
        if console_txt == 'SSH连接失败！':
            self.ui.build_build_button.setText('开服')
            self.ui.progressBar.reset()
            self.ui.build_build_button.setEnabled(True)
        elif console_txt == '上传失败！':
            self.ui.build_build_button.setText('开服')
            self.ui.progressBar.reset()
            self.ui.build_build_button.setEnabled(True)
        self.ui.build_log_text.append(console_txt)

    # 服务器控制信号与界面逻辑
    def Control_Start(self):
        if config.getint('SSH', 'connected') == 0:
            self.ui.control_save.setText('SSH未连接')
            time.sleep(5)
            self.ui.control_save.setText('保存')
        else:
            self.ui.control_save.setEnabled(False)
            self.ui.control_save.setText('保存中')
            self.ui.control_gamemode_combo.setEnabled(False)
            self.ui.control_chest_combo.setEnabled(False)
            self.ui.control_maxplayer_spin.setEnabled(False)
            self.ui.control_xbox_combo.setEnabled(False)
            self.ui.control_whitelist_combo.setEnabled(False)
            self.ui.control_view_spin.setEnabled(False)
            self.ui.control_tkdistance_spin.setEnabled(False)
            self.ui.control_ktime_spin.setEnabled(False)
            self.ui.control_maxthread_spin.setEnabled(False)
            self.ui.control_playerchara_combo.setEnabled(False)
            self.ui.control_texture_combo.setEnabled(False)
            self.ui.control_log_combo.setEnabled(False)
            self.ui.control_zip_spin.setEnabled(False)
            self.ui.control_v4_spin.setEnabled(False)
            self.ui.control_v6_spin.setEnabled(False)
            config.set("CONTROL", 'gamemode', self.ui.control_gamemode_combo.currentText())
            config.set("CONTROL", 'allow-cheats', self.ui.control_chest_combo.currentText())
            config.set("CONTROL", 'max-players', str(self.ui.control_maxplayer_spin.value()))
            config.set("CONTROL", 'online-mode', self.ui.control_xbox_combo.currentText())
            config.set("CONTROL", 'white-list', self.ui.control_whitelist_combo.currentText())
            config.set("CONTROL", 'view-distance', str(self.ui.control_view_spin.value()))
            config.set("CONTROL", 'tick-distance', str(self.ui.control_tkdistance_spin.value()))
            config.set("CONTROL", 'player-idle-timeout', str(self.ui.control_ktime_spin.value()))
            config.set("CONTROL", 'max-threads', str(self.ui.control_maxthread_spin.value()))
            config.set("CONTROL", 'default-player-permission-level', self.ui.control_playerchara_combo.currentText())
            config.set("CONTROL", 'texturepack-required', self.ui.control_texture_combo.currentText())
            config.set("CONTROL", 'content-log-file-enabled', self.ui.control_log_combo.currentText())
            config.set("CONTROL", 'compression-threshold', str(self.ui.control_zip_spin.value()))
            config.set("CONTROL", 'server-port', str(self.ui.control_v4_spin.value()))
            config.set("CONTROL", 'server-portv6', str(self.ui.control_v6_spin.value()))
            config.write(open("config.cfg", "w"))
            self.Control_QThread.start()
    # 进度条显示
    def ProgressBar(self, progress_int):
        self.ui.progressBar.setValue(progress_int)

    # 控制台显示
    def Console(self, text):
        self.ui.log_log_text.append(text)


if __name__ == '__main__':
    add = QApplication([])
    minecraft = Minecraft()
    minecraft.ui.show()
    add.exec_()
