"""
    As you know, I'm a newbie in Python.
        So there are too many Non-standard code.
            Don't worry about me, despite your suggestions.
                Then I'll thank you for your suggestions.
"""
import configparser
import ctypes
import os
import re
import shutil
import time
import webbrowser

from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QAbstractItemView, QApplication, QHeaderView,
                             QMainWindow, QMessageBox, QTableWidgetItem)

from sshconnect import sshconnect, sshget, sshsend
from whitelist import (add_whitelist, del_whitelist, read_whitelist,
                       write_whitelist)

# 读取配置数据
shutil.copy('config_template.cfg', 'config.cfg')

config = configparser.ConfigParser()
config.read('config.cfg')

# 多线程
# SSH连接线程命令
class SSH(QThread):
    OutPut = pyqtSignal(str)
    OutProgress = pyqtSignal(int)
    OutConsole = pyqtSignal(str)
    OutWhitelist = pyqtSignal(str)
    OutPlugin = pyqtSignal(str)

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
            self.OutPut.emit('正在处理...')
            self.connecting = False
        elif sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password) == False:
            self.OutPut.emit('连接失败')
            self.connecting = False
            return
        #command = 'screen -r EZ'
        #check = sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password, command)
        #self.OutConsole.emit(check)
        #if check.find("screen") == True:
        #    self.OutConsole.emit('没有检测到服务端进程！')
        #    return
        #else:
        #    print('ok')
            #command = 'scp -r '+ SSH_User+'@'+''
            #os.system('')
            #sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password, '')
        sshget(SSH_IP, SSH_Port, SSH_User, SSH_Password, '/root/EZ/whitelist.json')
        if os.path.getsize('Server_Download/whitelist.json'):
            self.OutProgress.emit(85)
        else:
            shutil.copy('Server/whitelist.json', 'Server_Download/whitelist.json')
            self.OutProgress.emit(85)
        sshget(SSH_IP, SSH_Port, SSH_User, SSH_Password, '/root/EZ/permissions.json')
        if os.path.getsize('Server_Download/permissions.json'):
            self.OutProgress.emit(90)
        else:
            shutil.copy('Server/permissions.json', 'Server_Download/permissions.json')
            self.OutProgress.emit(90)
        sshget(SSH_IP, SSH_Port, SSH_User, SSH_Password, '/root/EZ/settings')
        if os.path.exists('Server_Download\settings') == True:
            os.remove('Server_Download\settings')
            shutil.copyfile('Server\js_plugin.txt', 'Server_Download\js_plugin.txt')
        self.OutProgress.emit(95)
        read_whitelist()
        self.OutWhitelist.emit('True')
        self.OutPlugin.emit('True')
        self.OutPut.emit('连接成功')
        return

# 一键搭建线程命令
class Build(QThread):
    consoleOutPut = pyqtSignal(str)
    OutProgress = pyqtSignal(int)
    consoleOutPut_All = pyqtSignal(bool)
    stopcheck = pyqtSignal(bool)
    
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

        elif sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password) == False:
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
                self.OutProgress.emit(40)
                progress = 40
                if os.path.exists('Snap/build_log.txt'):
                    pass
                else:
                    log_txt = open('Snap/build_log.txt','w')
                    log_txt.close()
                    self.consoleOutPut_All.emit(True)
                for i in command_all:
                    sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password,'build_log.txt',i)
                    progress += 5
                    self.OutProgress.emit(progress)
            except:
                self.consoleOutPut.emit("开服失败！")
                return
            self.OutProgress.emit(100)
            self.consoleOutPut.emit('开服成功！执行日志已保存在Log文件夹中，关闭软件则会被删除。')
            self.stopcheck.emit(True)
            return

        # 本地上传
        elif download_url.startswith(('http', 'https', 'ftp')) != True:
            self.consoleOutPut.emit('从本地 \'' + download_url + ' \'获取服务端')
            #time.sleep(5)
            self.OutProgress.emit(20)
            if not download_url.endswith(('zip')):
                self.consoleOutPut.emit('上传的文件不是zip格式，无法上传！')
                return
            try:
                sshsend(SSH_IP, SSH_Port, SSH_User, SSH_Password, download_url, '/root/EZ/local.zip')
                with open('build-shell\\build-debian10-local.sh','r') as command:
    	            command_all = command.read().splitlines()
                self.OutProgress.emit(56)
                progress = 56
                for i in command_all:
                    if os.path.exists('Snap/build_log.txt'):
                        pass
                    else:
                        log_txt = open('Snap/build_log.txt','w')
                        log_txt.close()
                    seof.consoleOutPut_All.emit(True)
                    sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password,'build_log.txt',i)
                    progress += 4
                    self.OutProgress.emit(progress)
                self.consoleOutPut.emit('开服成功！')

                return
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
class Build_Check(QThread):
    consoleOutPut = pyqtSignal(bool)
    OutProgress = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super(Build_Check, self).__init__(parent)
        self.building = True
    def __del__(self):
        self.building = False
        # self.wait()
    def run(self):
        while os.path.exists('Snap/build_log.txt'):
            time.sleep(1)
            self.consoleOutPut.emit(True)
            time.sleep(3)
# 日志监控线程命令
class Log(QThread):
    consoleOutPut = pyqtSignal(bool)
    OutProgress = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super(Log, self).__init__(parent)
        self.building = True
    def __del__(self):
        self.building = False
        # self.wait()
    def run(self):
        SSH_IP = config.get("SSH", "server_ip")
        SSH_Port = config.get("SSH", "server_port")
        SSH_User = config.get("SSH", "server_user")
        SSH_Password = config.get("SSH", "server_pass")
        SCREEN_Id = config.get("EZ","screen_id")
        commandd = 'screen -D -r '+SCREEN_Id
        print(commandd)
        if os.path.exists('Snap/log.txt'):
            pass
        else:
            log_txt = open('Snap/log.txt','w')
            log_txt.close()
        self.consoleOutPut.emit(True)
        sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password, 'log.txt', commandd)
class Log_Check(QThread):
    consoleOutPut = pyqtSignal(bool)
    OutProgress = pyqtSignal(int)
    
    def __init__(self, parent=None):
        super(Log_Check, self).__init__(parent)
        self.building = True
    def __del__(self):
        self.building = False
        # self.wait()
    def run(self):
        while os.path.exists('Snap/log.txt'):
            time.sleep(1)
            self.consoleOutPut.emit(True)
            time.sleep(3)

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
        server_name = config.get("CONTROL", 'server-name')
        gamemode = config.get("CONTROL", 'gamemode')
        cheats = config.get("CONTROL", 'allow-cheats')
        max_players = config.getint("CONTROL", 'max-players')
        online_mode = config.get("CONTROL", 'online-mode')
        white_list = config.get("CONTROL", 'white-list')
        view_distance = config.getint("CONTROL", 'view-distance')
        tick_distance = config.getint("CONTROL", 'tick-distance')
        player_idle_timeout = config.getint("CONTROL", 'player-idle-timeout')
        max_threads = config.getint("CONTROL", 'max-threads')
        player_chara = config.get("CONTROL", 'default-player-permission-level')
        texture = config.get("CONTROL", 'texturepack-required')
        error_log = config.get("CONTROL", 'content-log-file-enabled')
        compress = config.getint("CONTROL", 'compression-threshold')
        server_port = config.getint("CONTROL", 'server-port')
        server_port_v6 = config.getint("CONTROL", 'server-portv6')
        try:
            os.mkdir('Snap')
        except:
            pass
        shutil.copy('Server/server.properties.cfg', 'Snap/server.properties2.cfg')

        SSH_IP = config.get("SSH", "server_ip")
        SSH_Port = config.getint("SSH", "server_port")
        SSH_User = config.get("SSH", "server_user")
        SSH_Password = config.get("SSH", "server_pass")

        self.OutProgress.emit(50)
        config2 = configparser.ConfigParser()
        config2.read('Snap/server.properties2.cfg')
        config2.set("CONTROL", 'server-name', server_name)
        config2.set("CONTROL", 'gamemode', gamemode)
        config2.set("CONTROL", 'allow-cheats', cheats)
        config2.set("CONTROL", 'max-players', str(max_players))
        config2.set("CONTROL", 'online-mode', online_mode)
        config2.set("CONTROL", 'white-list', white_list)
        config2.set("CONTROL", 'view-distance', str(view_distance))
        config2.set("CONTROL", 'tick-distance', str(tick_distance))
        config2.set("CONTROL", 'player-idle-timeout', str(player_idle_timeout))
        config2.set("CONTROL", 'max-threads', str(max_threads))
        config2.set("CONTROL", 'default-player-permission-level', player_chara)
        config2.set("CONTROL", 'texturepack-required', texture)
        config2.set("CONTROL", 'content-log-file-enabled', error_log)
        config2.set("CONTROL", 'compression-threshold', str(compress))
        config2.set("CONTROL", 'server-port', str(server_port))
        config2.set("CONTROL", 'server-portv6', str(server_port_v6))
        config2.write(open("Snap/server.properties2.cfg", "w"))
        self.OutProgress.emit(60)
        shutil.copy('Snap/server.properties2.cfg', 'Snap/server.properties_snap')
        create_server = open('Snap/server.properties_snap', 'r+')
        open('Snap/server.properties_snap2', 'w').write(re.sub(r"\[CONTROL\]", "# By MCPEManager", create_server.read()))
        create_server.close()
        f = open("Snap/server.properties_snap2")
        conf = f.read()
        conf = conf.replace(" = ","=")
        open('server.properties', 'w').write(conf)
        f.close()
        try:
            sshsend(SSH_IP, SSH_Port, SSH_User, SSH_Password, 'server.properties', '/root/EZ/server.properties')
            self.OutPut.emit('保存成功！')
            self.OutProgress.emit(100)
        except:
            self.OutPut.emit('保存失败！')
            self.OutProgress.emit(0)
        #try:
        #    sshconnect(SSH_IP, SSH_Port, SSH_User, SSH_Password, command=['screen -S EZ -X quit', 'screen -r EZ', ''])
        #    self.OutPut.emit('保存成功！')
        #    self.OutProgress.emit(100)
        #except:
        #    self.OutPut.emit('保存失败！')
        #    self.OutProgress.emit(0)
        return

# 白名单线程命令
class Whitelist(QThread):
    OutProgress = pyqtSignal(int)
    OutPut = pyqtSignal(str)
    OutWhitelist = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Whitelist, self).__init__(parent)
        self.controling = True
    def __del__(self):
        self.controling = False
        # self.wait()
    def run(self):
        self._whitelist_list = []
        SSH_IP = config.get("SSH", "server_ip")
        SSH_Port = config.getint("SSH", "server_port")
        SSH_User = config.get("SSH", "server_user")
        SSH_Password = config.get("SSH", "server_pass")
        for self._whitelist in open('Snap/whitelist.txt'):
            self._whitelist_singal = []
            self._whitelist = self._whitelist.replace('\n', '').replace('\r', '')
            if self._whitelist.endswith("False"):
                self._whitelist = self._whitelist.replace('False', 'false')
            elif self._whitelist.endswith("True"):
                self._whitelist = self._whitelist.replace('True', 'true')
            self.xuid = ''
            self.white_name = self._whitelist.partition(';')[0]
            self.ignoresPlayerLimit_id = self._whitelist.rpartition(';')[2]
            self._whitelist_singal.append(self.white_name)
            self.del_name_id = self._whitelist.find(';')
            self.del_ignore_id = self._whitelist.rfind(';')
            for i in range(0,len(self._whitelist)):
                if i > self.del_name_id and i < self.del_ignore_id:
                    self.xuid = self.xuid + self._whitelist[i]
            self._whitelist_singal.append(self.xuid)
            self._whitelist_singal.append(self.ignoresPlayerLimit_id)
            self._whitelist_list.append(self._whitelist_singal)
        write_whitelist()
        self.OutWhitelist.emit(self._whitelist_list)
        try:
            sshsend(SSH_IP, SSH_Port, SSH_User, SSH_Password, 'Snap/whitelist.json', '/root/EZ/whitelist.json')
        except:
            pass
class WhitelistAdd(QThread):
    OutProgress = pyqtSignal(int)
    OutPut = pyqtSignal(str)
    OutWhitelist = pyqtSignal(str)

    def __init__(self, parent=None):
        super(WhitelistAdd, self).__init__(parent)
        self.controling = True
    def __del__(self):
        self.controling = False
        # self.wait()
    def run(self):
        user = config.get("Server", "add_user")
        add_whitelist(user)
        self.OutWhitelist.emit('True')
class WhitelistDel(QThread):
    OutProgress = pyqtSignal(int)
    OutPut = pyqtSignal(str)
    OutWhitelist = pyqtSignal(str)

    def __init__(self, parent=None):
        super(WhitelistDel, self).__init__(parent)
        self.controling = True
    def __del__(self):
        self.controling = False
        # self.wait()
    def run(self):
        user = config.get("Server", "del_user")
        del_whitelist(user)
        self.OutWhitelist.emit('True')

# 插件管理线程命令
class PluginJs(QThread):
    OutProgress = pyqtSignal(int)
    OutPut = pyqtSignal(str)
    OutPluginJs = pyqtSignal(list)

    def __init__(self, parent=None):
        super(PluginJs, self).__init__(parent)
        self.controling = True
    def __del__(self):
        self.controling = False
        # self.wait()
    def run(self):
        self._plugin_js_list = []
        for self._plugin_js in open('Server_Download/js_plugin.txt',encoding='utf-8'):
            self._plugin_js_singal = []
            self._plugin_js = self._plugin_js.replace('\n', '').replace('\r', '')
            self.plugin_js_introduction = ''
            self.plugin_js_name = self._plugin_js.partition(';')[0]
            self.plugin_js_enable = self._plugin_js.rpartition(';')[2]
            self._plugin_js_singal.append(self.plugin_js_name)
            self.del_name_id = self._plugin_js.find(';')
            self.del_ignore_id = self._plugin_js.rfind(';')
            for i in range(0,len(self._plugin_js)):
                if i > self.del_name_id and i < self.del_ignore_id:
                    self.plugin_js_introduction = self.plugin_js_introduction + self._plugin_js[i]
            self._plugin_js_singal.append(self.plugin_js_introduction)
            self._plugin_js_singal.append(self.plugin_js_enable)
            self._plugin_js_list.append(self._plugin_js_singal)
        #write_whitelist()
        self.OutPluginJs.emit(self._plugin_js_list)

# 界面操作
class Minecraft:
    def __init__(self,parent=None):
        self.ui = uic.loadUi('UI/main.ui')
        self.ui.setWindowIcon(QIcon('MCPEManager.ico'))
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

        # 白名单管理
        self.Whitelist_QThread = Whitelist()
        self.Whitelist_Add_QThread = WhitelistAdd()
        self.Whitelist_Del_QThread = WhitelistDel()
        self.ui.whitelist_list.setColumnCount(3)
        self.ui.whitelist_list.setRowCount(100)
        self.ui.whitelist_list.setHorizontalHeaderLabels(['ID','xuid','忽略玩家计数'])
        self.ui.whitelist_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.whitelist_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.whitelist_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) 
        #self.ui.whitelist_add_edit.setEnabled(False)
        #self.ui.whitelist_add_button.setEnabled(False)
        #self.ui.whitelist_del_button.setEnabled(False)
        self.ui.whitelist_list.itemClicked.connect(self.Whitelist_Click)
        self.ui.whitelist_add_button.clicked.connect(self.Whitelist_Add)
        self.ui.whitelist_del_button.clicked.connect(self.Whitelist_Del)
        self.Whitelist_QThread.OutWhitelist.connect(self.Whitelist_Show)
        self.Whitelist_Add_QThread.OutWhitelist.connect(self.SSH_Whitelist)
        self.Whitelist_Del_QThread.OutWhitelist.connect(self.SSH_Whitelist)

        # 关于标签页
        self.ui.about_vcheck_button.clicked.connect(self.CheckVersion)

        # 一键开服标签页
        self.Build_QThread = Build()
        self.Build_Check_QThread = Build_Check()
        self.ui.build_build_button.clicked.connect(self.Build_Start)
        self.Build_QThread.consoleOutPut_All.connect(self.Build_Check)
        self.Build_QThread.consoleOutPut.connect(self.Build_Console_Show)
        self.Build_QThread.OutProgress.connect(self.ProgressBar)
        self.Build_QThread.stopcheck.connect(self.Build_Check_Stop)
        self.Build_Check_QThread.consoleOutPut.connect(self.Build_Console_All_Show)

        # 日志监控标签页
        self.Log_QThread = Log()
        self.Log_Check_QThread = Log_Check()
        self.ui.log_startlog_button.clicked.connect(self.Log_Start)
        self.Log_QThread.consoleOutPut.connect(self.Log_Check)
        self.Log_Check_QThread.consoleOutPut.connect(self.Log_Show)

        # SSH连接
        self.SSH_QThread = SSH()
        self.ui.Connect_button.clicked.connect(self.SSH_Start)
        self.SSH_QThread.OutPut.connect(self.SSH_Show)
        self.SSH_QThread.OutProgress.connect(self.ProgressBar)
        self.SSH_QThread.OutConsole.connect(self.Console)
        self.SSH_QThread.OutWhitelist.connect(self.SSH_Whitelist)
        self.SSH_QThread.OutPlugin.connect(self.SSH_Plugin_Js)

        # 服务器控制
        self.Control_QThread = Control()
        self.ui.control_save.clicked.connect(self.Control_Start)
        self.Control_QThread.OutProgress.connect(self.ProgressBar)
        self.Control_QThread.OutPut.connect(self.Control_button_Show)

        # 插件管理
        self.Plugin_JS_QThread = PluginJs()
        self.ui.plugin_js_list.setColumnCount(3)
        self.ui.plugin_js_list.setHorizontalHeaderLabels(['插件','简介','是否启用'])
        self.ui.plugin_js_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.plugin_js_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.plugin_js_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.plugin_js_list.setRowCount(100)
        self.ui.plugin_dll_list.setColumnCount(3)
        self.ui.plugin_dll_list.setHorizontalHeaderLabels(['插件','简介','是否启用'])
        self.ui.plugin_dll_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.plugin_dll_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.plugin_dll_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.plugin_dll_list.setRowCount(100)
        self.ui.plugin_script_list.setColumnCount(3)
        self.ui.plugin_script_list.setHorizontalHeaderLabels(['插件','简介','是否启用'])
        self.ui.plugin_script_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.plugin_script_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.plugin_script_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.plugin_script_list.setRowCount(100)
        self.Plugin_JS_QThread.OutPluginJs.connect(self.Plugin_Js_Show)
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
        if button_show == '正在处理...':
            self.ui.progressBar.setValue(80)
        elif button_show == '连接成功':
            self.ui.progressBar.setValue(100)
            config.set("SSH", "connected", '1')
            config.write(open("config.cfg", "w"))
            self.ui.log_startlog_button.setEnabled(True)
            return
        else:
            self.ui.progressBar.reset()
            self.ui.Connect_button.setEnabled(True)
            self.ui.IP_edit.setEnabled(True)
            self.ui.Port_edit.setEnabled(True)
            self.ui.User_edit.setEnabled(True)
            self.ui.Password_edit.setEnabled(True)
        

    def SSH_Whitelist(self,start):
        if start == 'True':
            self.ui.whitelist_add_edit.setEnabled(True)
            self.ui.whitelist_add_button.setEnabled(True)
            self.ui.whitelist_del_button.setEnabled(True)
            self.Whitelist_QThread.start()
    def SSH_Plugin_Js(self,start):
        if start == 'True':
            self.Plugin_JS_QThread.start()

    # 日志监控信号与界面逻辑
    def Log_Start(self):
        self.ui.log_startlog_button.setEnabled(False)
        self.Log_QThread.start()
    def Log_Check(self,check):
        if check == True:
            self.ui.log_startlog_button.setText('已开启')
            self.Log_Check_QThread.start()
    def Log_Show(self,check):
        self.ui.log_log_text.clear()
        with open('Snap/log.txt','r')as f:
            f = f.read()
            self.ui.log_log_text.append(f)

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
    def Build_Check(self,check):
        if check == True:
            self.Build_Check_QThread.start()
    def Build_Check_Stop(self,check):
        shutil.copy('Snap/build_log.txt', 'Log/build_log.txt')
        os.remove('Snap/build_log.txt')
        self.Build_Check_QThread.quit()
        self.ui.build_build_button.setText('开服')
        self.ui.build_build_button.setEnabled(True)

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
    def Build_Console_All_Show(self,check):
        if check == True:
            self.ui.build_log_text.clear()
            with open('Snap/build_log.txt','r')as f:
                f = f.read()
                self.ui.build_log_text.append(f)        
    # 服务器控制信号与界面逻辑
    def Control_Start(self):
        if config.getint('SSH', 'connected') == 0:
            self.ui.control_save.setText('SSH未连接')
        else:
            self.ui.control_save.setEnabled(False)
            self.ui.control_save.setText('保存中')
            self.ui.control_servername_edit.setEnabled(False)
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
            config.set("CONTROL", 'server-name', str(self.ui.control_servername_edit.text()))
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
            self.ui.progressBar.setValue(10)
            self.Control_QThread.start()
    def Control_button_Show(self, text):
        self.ui.control_save.setText(text)
        self.ui.control_servername_edit.setEnabled(True)
        self.ui.control_save.setEnabled(True)
        self.ui.control_gamemode_combo.setEnabled(True)
        self.ui.control_chest_combo.setEnabled(True)
        self.ui.control_maxplayer_spin.setEnabled(True)
        self.ui.control_xbox_combo.setEnabled(True)
        self.ui.control_whitelist_combo.setEnabled(True)
        self.ui.control_view_spin.setEnabled(True)
        self.ui.control_tkdistance_spin.setEnabled(True)
        self.ui.control_ktime_spin.setEnabled(True)
        self.ui.control_maxthread_spin.setEnabled(True)
        self.ui.control_playerchara_combo.setEnabled(True)
        self.ui.control_texture_combo.setEnabled(True)
        self.ui.control_log_combo.setEnabled(True)
        self.ui.control_zip_spin.setEnabled(True)
        self.ui.control_v4_spin.setEnabled(True)
        self.ui.control_v6_spin.setEnabled(True)

    # 白名单管理信号与界面逻辑
    def Whitelist_Add(self):
        self.ui.whitelist_add_edit.setEnabled(False)
        self.ui.whitelist_add_button.setEnabled(False)
        self.ui.whitelist_del_button.setEnabled(False)
        if str(self.ui.whitelist_add_edit.text()) == '':
            self.ui.whitelist_add_button.setText('未输入！')
            self.ui.whitelist_add_edit.setEnabled(True)
            self.ui.whitelist_add_button.setEnabled(True)
            self.ui.whitelist_del_button.setEnabled(True)
            return
        
        config.set("Server", "add_user", str(self.ui.whitelist_add_edit.text()))
        self.ui.whitelist_add_edit.setEnabled(True)
        self.ui.whitelist_add_button.setEnabled(True)
        self.ui.whitelist_del_button.setEnabled(True)
        self.Whitelist_Add_QThread.start()
    def Whitelist_Del(self):
        self.ui.whitelist_add_edit.setEnabled(False)
        self.ui.whitelist_add_button.setEnabled(False)
        self.ui.whitelist_del_button.setEnabled(False)
        if str(self.ui.whitelist_add_edit.text()) == '':
            self.ui.whitelist_add_button.setText('未输入！')
            self.ui.whitelist_add_edit.setEnabled(True)
            self.ui.whitelist_add_button.setEnabled(True)
            self.ui.whitelist_del_button.setEnabled(True)
            return
        
        config.set("Server", "del_user", str(self.ui.whitelist_add_edit.text()))
        self.ui.whitelist_add_edit.setEnabled(True)
        self.ui.whitelist_add_button.setEnabled(True)
        self.ui.whitelist_del_button.setEnabled(True)
        self.Whitelist_Del_QThread.start()
    def Whitelist_Show(self, whitelist):
        self.ui.whitelist_list.clearContents()
        self.column_number = 0
        for i in range(0,len(whitelist)):
            self.white_user = []
            self.white_user.append(whitelist[i][0])
            self.white_user.append(whitelist[i][1])
            self.white_user.append(whitelist[i][2])
            self.line_number = 0
            for j in self.white_user:
                newItem = QTableWidgetItem(str(j))
                self.ui.whitelist_list.setItem(self.line_number, self.column_number,newItem)
                self.column_number += 1
            self.line_number += 1
            #self.ui.whitelist_list.append(whitelist[i])
        # write_whitelist()
    def Whitelist_Click(self):
        print('Clicked')

    # 插件管理信号与界面逻辑
    def Plugin_Js_Add(self):
        pass
    def Plugin_Js_Show(self, plugin_js_list):
        self.ui.plugin_js_list.clearContents()
        self.column_number = 0
        for i in range(0,len(plugin_js_list)):
            self.white_user = []
            self.white_user.append(plugin_js_list[i][0])
            self.white_user.append(plugin_js_list[i][1])
            self.white_user.append(plugin_js_list[i][2])
            self.line_number = 0
            for j in self.white_user:
                newItem = QTableWidgetItem(str(j))
                self.ui.plugin_js_list.setItem(self.line_number, self.column_number,newItem)
                self.column_number += 1
            self.line_number += 1
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
    os.remove('config.cfg')
    try:
        os.remove('server.properties')
    except:
        pass
    if os.listdir('Snap') != []:
        remove = os.listdir('Snap')
        print(remove)
        for i in remove:
            os.remove('Snap/'+i)
    if os.listdir('Server_Download') != []:
        remove = os.listdir('Server_Download')
        print(remove)
        for j in remove:
            os.remove('Server_Download/'+j)
    if os.listdir('Log') != []:
        remove = os.listdir('Log')
        print(remove)
        for k in remove:
            os.remove('Log/'+k)
