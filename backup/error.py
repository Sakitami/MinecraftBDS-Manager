from PyQt5.QtCore import QThread

class SSH_Connect(QThread):
    def __init__(self):
        super().__init__()
    def SSHconnect(self):
        xxxxxx

class Minecraft:
    def __init__(self):
        def SSHCONNECT(self):
            self.sshconnecT = SSH_Connect()
            self.sshconnecT.start()

        self.ui = uic.loadUi('UI/main.ui')

        self.ui.Connect_button.clicked.connect(SSHCONNECT)

add = QApplication([])
minecraft = Minecraft()
minecraft.ui.show()
add.exec_()