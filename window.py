# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainquqeAz.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from kurlrequester import KUrlRequester
from kpasswordlineedit import KPasswordLineEdit
from kurllabel import KUrlLabel


class Ui_Minecraft(object):
    def setupUi(self, Minecraft):
        if not Minecraft.objectName():
            Minecraft.setObjectName(u"Minecraft")
        Minecraft.resize(809, 453)
        self.build = QTabWidget(Minecraft)
        self.build.setObjectName(u"build")
        self.build.setGeometry(QRect(10, 20, 641, 421))
        self.Control = QWidget()
        self.Control.setObjectName(u"Control")
        self.control_servername_title = QLabel(self.Control)
        self.control_servername_title.setObjectName(u"control_servername_title")
        self.control_servername_title.setGeometry(QRect(10, 10, 71, 31))
        self.control_servername_edit = QLineEdit(self.Control)
        self.control_servername_edit.setObjectName(u"control_servername_edit")
        self.control_servername_edit.setGeometry(QRect(80, 10, 231, 32))
        self.horizontalLayoutWidget_2 = QWidget(self.Control)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 50, 301, 321))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.control_gamemode_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_gamemode_title.setObjectName(u"control_gamemode_title")

        self.verticalLayout_3.addWidget(self.control_gamemode_title)

        self.control_gamemode_combo = QComboBox(self.horizontalLayoutWidget_2)
        self.control_gamemode_combo.addItem("")
        self.control_gamemode_combo.addItem("")
        self.control_gamemode_combo.addItem("")
        self.control_gamemode_combo.setObjectName(u"control_gamemode_combo")

        self.verticalLayout_3.addWidget(self.control_gamemode_combo)

        self.control_chest_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_chest_title.setObjectName(u"control_chest_title")

        self.verticalLayout_3.addWidget(self.control_chest_title)

        self.control_chest_combo = QComboBox(self.horizontalLayoutWidget_2)
        self.control_chest_combo.addItem("")
        self.control_chest_combo.addItem("")
        self.control_chest_combo.setObjectName(u"control_chest_combo")

        self.verticalLayout_3.addWidget(self.control_chest_combo)

        self.control_maxplayer_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_maxplayer_title.setObjectName(u"control_maxplayer_title")

        self.verticalLayout_3.addWidget(self.control_maxplayer_title)

        self.control_maxplayer_spin = QSpinBox(self.horizontalLayoutWidget_2)
        self.control_maxplayer_spin.setObjectName(u"control_maxplayer_spin")
        self.control_maxplayer_spin.setMinimum(1)
        self.control_maxplayer_spin.setMaximum(999)
        self.control_maxplayer_spin.setValue(10)

        self.verticalLayout_3.addWidget(self.control_maxplayer_spin)

        self.control_xbox_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_xbox_title.setObjectName(u"control_xbox_title")

        self.verticalLayout_3.addWidget(self.control_xbox_title)

        self.control_xbox_combo = QComboBox(self.horizontalLayoutWidget_2)
        self.control_xbox_combo.addItem("")
        self.control_xbox_combo.addItem("")
        self.control_xbox_combo.setObjectName(u"control_xbox_combo")

        self.verticalLayout_3.addWidget(self.control_xbox_combo)

        self.control_whitelist_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_whitelist_title.setObjectName(u"control_whitelist_title")

        self.verticalLayout_3.addWidget(self.control_whitelist_title)

        self.control_whitelist_combo = QComboBox(self.horizontalLayoutWidget_2)
        self.control_whitelist_combo.addItem("")
        self.control_whitelist_combo.addItem("")
        self.control_whitelist_combo.setObjectName(u"control_whitelist_combo")

        self.verticalLayout_3.addWidget(self.control_whitelist_combo)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.control_view_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_view_title.setObjectName(u"control_view_title")

        self.verticalLayout_5.addWidget(self.control_view_title)

        self.control_view_spin = QSpinBox(self.horizontalLayoutWidget_2)
        self.control_view_spin.setObjectName(u"control_view_spin")
        self.control_view_spin.setMinimum(1)
        self.control_view_spin.setMaximum(999)
        self.control_view_spin.setValue(32)
        self.control_view_spin.setDisplayIntegerBase(10)

        self.verticalLayout_5.addWidget(self.control_view_spin)

        self.control_tkdistance_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_tkdistance_title.setObjectName(u"control_tkdistance_title")

        self.verticalLayout_5.addWidget(self.control_tkdistance_title)

        self.control_tkdistance_spin = QSpinBox(self.horizontalLayoutWidget_2)
        self.control_tkdistance_spin.setObjectName(u"control_tkdistance_spin")
        self.control_tkdistance_spin.setMinimum(4)
        self.control_tkdistance_spin.setMaximum(12)
        self.control_tkdistance_spin.setValue(4)
        self.control_tkdistance_spin.setDisplayIntegerBase(10)

        self.verticalLayout_5.addWidget(self.control_tkdistance_spin)

        self.control_ktime_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_ktime_title.setObjectName(u"control_ktime_title")

        self.verticalLayout_5.addWidget(self.control_ktime_title)

        self.control_ktime_spin = QSpinBox(self.horizontalLayoutWidget_2)
        self.control_ktime_spin.setObjectName(u"control_ktime_spin")
        self.control_ktime_spin.setMinimum(0)
        self.control_ktime_spin.setMaximum(999)
        self.control_ktime_spin.setValue(0)

        self.verticalLayout_5.addWidget(self.control_ktime_spin)

        self.control_maxthread_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_maxthread_title.setObjectName(u"control_maxthread_title")

        self.verticalLayout_5.addWidget(self.control_maxthread_title)

        self.control_maxthread_spin = QSpinBox(self.horizontalLayoutWidget_2)
        self.control_maxthread_spin.setObjectName(u"control_maxthread_spin")
        self.control_maxthread_spin.setMinimum(0)
        self.control_maxthread_spin.setMaximum(999)
        self.control_maxthread_spin.setValue(8)

        self.verticalLayout_5.addWidget(self.control_maxthread_spin)

        self.control_playerchara_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_playerchara_title.setObjectName(u"control_playerchara_title")

        self.verticalLayout_5.addWidget(self.control_playerchara_title)

        self.control_playerchara_combo = QComboBox(self.horizontalLayoutWidget_2)
        self.control_playerchara_combo.addItem("")
        self.control_playerchara_combo.addItem("")
        self.control_playerchara_combo.addItem("")
        self.control_playerchara_combo.setObjectName(u"control_playerchara_combo")

        self.verticalLayout_5.addWidget(self.control_playerchara_combo)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.control_texture_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_texture_title.setObjectName(u"control_texture_title")

        self.verticalLayout_4.addWidget(self.control_texture_title)

        self.control_texture_combo = QComboBox(self.horizontalLayoutWidget_2)
        self.control_texture_combo.addItem("")
        self.control_texture_combo.addItem("")
        self.control_texture_combo.setObjectName(u"control_texture_combo")

        self.verticalLayout_4.addWidget(self.control_texture_combo)

        self.control_log_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_log_title.setObjectName(u"control_log_title")

        self.verticalLayout_4.addWidget(self.control_log_title)

        self.control_log_combo = QComboBox(self.horizontalLayoutWidget_2)
        self.control_log_combo.addItem("")
        self.control_log_combo.addItem("")
        self.control_log_combo.setObjectName(u"control_log_combo")

        self.verticalLayout_4.addWidget(self.control_log_combo)

        self.control_zip_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_zip_title.setObjectName(u"control_zip_title")

        self.verticalLayout_4.addWidget(self.control_zip_title)

        self.control_zip_spin = QSpinBox(self.horizontalLayoutWidget_2)
        self.control_zip_spin.setObjectName(u"control_zip_spin")
        self.control_zip_spin.setMinimum(1)
        self.control_zip_spin.setMaximum(999)
        self.control_zip_spin.setValue(1)

        self.verticalLayout_4.addWidget(self.control_zip_spin)

        self.control_v4_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_v4_title.setObjectName(u"control_v4_title")

        self.verticalLayout_4.addWidget(self.control_v4_title)

        self.control_v4_spin = QSpinBox(self.horizontalLayoutWidget_2)
        self.control_v4_spin.setObjectName(u"control_v4_spin")
        self.control_v4_spin.setMinimum(1)
        self.control_v4_spin.setMaximum(65535)
        self.control_v4_spin.setValue(19132)

        self.verticalLayout_4.addWidget(self.control_v4_spin)

        self.control_v6_title = QLabel(self.horizontalLayoutWidget_2)
        self.control_v6_title.setObjectName(u"control_v6_title")

        self.verticalLayout_4.addWidget(self.control_v6_title)

        self.control_v6_spin = QSpinBox(self.horizontalLayoutWidget_2)
        self.control_v6_spin.setObjectName(u"control_v6_spin")
        self.control_v6_spin.setMinimum(1)
        self.control_v6_spin.setMaximum(65535)
        self.control_v6_spin.setValue(19133)

        self.verticalLayout_4.addWidget(self.control_v6_spin)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)

        self.control_olplayer_title = QLabel(self.Control)
        self.control_olplayer_title.setObjectName(u"control_olplayer_title")
        self.control_olplayer_title.setGeometry(QRect(330, 10, 71, 31))
        self.listView = QListView(self.Control)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(330, 50, 301, 131))
        self.label_24 = QLabel(self.Control)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(330, 180, 71, 31))
        self.listView_2 = QListView(self.Control)
        self.listView_2.setObjectName(u"listView_2")
        self.listView_2.setGeometry(QRect(330, 210, 301, 81))
        self.control_op_edit = QLineEdit(self.Control)
        self.control_op_edit.setObjectName(u"control_op_edit")
        self.control_op_edit.setGeometry(QRect(330, 301, 181, 31))
        self.horizontalLayoutWidget_3 = QWidget(self.Control)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(520, 290, 101, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.control_opadd_button = QPushButton(self.horizontalLayoutWidget_3)
        self.control_opadd_button.setObjectName(u"control_opadd_button")

        self.horizontalLayout_3.addWidget(self.control_opadd_button)

        self.control_opdel_button = QPushButton(self.horizontalLayoutWidget_3)
        self.control_opdel_button.setObjectName(u"control_opdel_button")

        self.horizontalLayout_3.addWidget(self.control_opdel_button)

        self.control_command_edit = QLineEdit(self.Control)
        self.control_command_edit.setObjectName(u"control_command_edit")
        self.control_command_edit.setGeometry(QRect(330, 340, 181, 32))
        self.control_save = QPushButton(self.Control)
        self.control_save.setObjectName(u"control_save")
        self.control_save.setGeometry(QRect(530, 340, 91, 34))
        self.control_onkick_button = QPushButton(self.Control)
        self.control_onkick_button.setObjectName(u"control_onkick_button")
        self.control_onkick_button.setGeometry(QRect(530, 10, 91, 34))
        self.build.addTab(self.Control, "")
        self.build1 = QWidget()
        self.build1.setObjectName(u"build1")
        self.build_serverdown_choose = KUrlRequester(self.build1)
        self.build_serverdown_choose.setObjectName(u"build_serverdown_choose")
        self.build_serverdown_choose.setGeometry(QRect(10, 40, 611, 32))
        self.build_serverdown_choose.setUrl(QUrl(u"https://www.github.com/Sakitami/BDX/1.14.60.tar.gz"))
        self.build_serverdown_title = QLabel(self.build1)
        self.build_serverdown_title.setObjectName(u"build_serverdown_title")
        self.build_serverdown_title.setGeometry(QRect(10, 10, 141, 31))
        self.build_log_title = QLabel(self.build1)
        self.build_log_title.setObjectName(u"build_log_title")
        self.build_log_title.setGeometry(QRect(10, 80, 141, 31))
        self.build_log_text = QTextBrowser(self.build1)
        self.build_log_text.setObjectName(u"build_log_text")
        self.build_log_text.setGeometry(QRect(10, 110, 611, 191))
        self.build_debian10_title = QLabel(self.build1)
        self.build_debian10_title.setObjectName(u"build_debian10_title")
        self.build_debian10_title.setGeometry(QRect(10, 340, 311, 31))
        self.build_build_button = QPushButton(self.build1)
        self.build_build_button.setObjectName(u"build_build_button")
        self.build_build_button.setGeometry(QRect(530, 340, 91, 34))
        self.build.addTab(self.build1, "")
        self.log = QWidget()
        self.log.setObjectName(u"log")
        self.log_log_text = QTextBrowser(self.log)
        self.log_log_text.setObjectName(u"log_log_text")
        self.log_log_text.setGeometry(QRect(-10, -10, 651, 341))
        self.log_save_button = QPushButton(self.log)
        self.log_save_button.setObjectName(u"log_save_button")
        self.log_save_button.setGeometry(QRect(530, 340, 91, 34))
        self.log_save_choose = KUrlRequester(self.log)
        self.log_save_choose.setObjectName(u"log_save_choose")
        self.log_save_choose.setGeometry(QRect(20, 340, 281, 32))
        self.log_save_choose.setUrl(QUrl(u""))
        self.build.addTab(self.log, "")
        self.whitelist = QWidget()
        self.whitelist.setObjectName(u"whitelist")
        self.whitelist_add_edit = QLineEdit(self.whitelist)
        self.whitelist_add_edit.setObjectName(u"whitelist_add_edit")
        self.whitelist_add_edit.setGeometry(QRect(20, 340, 241, 32))
        self.whitelist_whitelist_list = QTextBrowser(self.whitelist)
        self.whitelist_whitelist_list.setObjectName(u"whitelist_whitelist_list")
        self.whitelist_whitelist_list.setGeometry(QRect(-10, -10, 651, 341))
        self.whitelist_del_button = QPushButton(self.whitelist)
        self.whitelist_del_button.setObjectName(u"whitelist_del_button")
        self.whitelist_del_button.setGeometry(QRect(530, 340, 91, 34))
        self.whitelist_add_button = QPushButton(self.whitelist)
        self.whitelist_add_button.setObjectName(u"whitelist_add_button")
        self.whitelist_add_button.setGeometry(QRect(430, 340, 91, 34))
        self.build.addTab(self.whitelist, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.plugin_list_lst = QListView(self.tab_6)
        self.plugin_list_lst.setObjectName(u"plugin_list_lst")
        self.plugin_list_lst.setGeometry(QRect(-10, -10, 651, 341))
        self.plugin_upload_choose = KUrlRequester(self.tab_6)
        self.plugin_upload_choose.setObjectName(u"plugin_upload_choose")
        self.plugin_upload_choose.setGeometry(QRect(20, 340, 281, 32))
        self.plugin_upload_choose.setUrl(QUrl(u""))
        self.plugin_onoff_button = QPushButton(self.tab_6)
        self.plugin_onoff_button.setObjectName(u"plugin_onoff_button")
        self.plugin_onoff_button.setGeometry(QRect(430, 340, 91, 34))
        self.plugin_del_button = QPushButton(self.tab_6)
        self.plugin_del_button.setObjectName(u"plugin_del_button")
        self.plugin_del_button.setGeometry(QRect(530, 340, 91, 34))
        self.build.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.pluginstore_pstore_list = QListView(self.tab_5)
        self.pluginstore_pstore_list.setObjectName(u"pluginstore_pstore_list")
        self.pluginstore_pstore_list.setGeometry(QRect(-10, -10, 651, 341))
        self.pluginstore_ori_edit = QLineEdit(self.tab_5)
        self.pluginstore_ori_edit.setObjectName(u"pluginstore_ori_edit")
        self.pluginstore_ori_edit.setGeometry(QRect(20, 340, 241, 32))
        self.pluginstore_install_button = QPushButton(self.tab_5)
        self.pluginstore_install_button.setObjectName(u"pluginstore_install_button")
        self.pluginstore_install_button.setGeometry(QRect(530, 340, 91, 34))
        self.pluginstore_switch_button = QPushButton(self.tab_5)
        self.pluginstore_switch_button.setObjectName(u"pluginstore_switch_button")
        self.pluginstore_switch_button.setGeometry(QRect(430, 340, 91, 34))
        self.build.addTab(self.tab_5, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 611, 91))
        self.label_28 = QLabel(self.groupBox)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setGeometry(QRect(10, 40, 91, 31))
        self.pushButton_13 = QPushButton(self.groupBox)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(90, 40, 88, 34))
        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 0, 611, 91))
        self.label_29 = QLabel(self.groupBox_2)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 40, 91, 31))
        self.pushButton_14 = QPushButton(self.groupBox_2)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(90, 40, 88, 34))
        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(0, 0, 611, 91))
        self.label_30 = QLabel(self.groupBox_3)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 40, 91, 31))
        self.pushButton_15 = QPushButton(self.groupBox_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(90, 40, 88, 34))
        self.about_software_group = QGroupBox(self.groupBox_3)
        self.about_software_group.setObjectName(u"about_software_group")
        self.about_software_group.setGeometry(QRect(0, 0, 611, 91))
        self.about_software_title = QLabel(self.about_software_group)
        self.about_software_title.setObjectName(u"about_software_title")
        self.about_software_title.setGeometry(QRect(10, 40, 91, 31))
        self.about_vcheck_button = QPushButton(self.about_software_group)
        self.about_vcheck_button.setObjectName(u"about_vcheck_button")
        self.about_vcheck_button.setGeometry(QRect(90, 40, 88, 34))
        self.about_thanks_group = QGroupBox(self.tab)
        self.about_thanks_group.setObjectName(u"about_thanks_group")
        self.about_thanks_group.setGeometry(QRect(10, 110, 611, 91))
        self.label_32 = QLabel(self.about_thanks_group)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(10, 40, 91, 31))
        self.pushButton_17 = QPushButton(self.about_thanks_group)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(90, 40, 88, 34))
        self.about_about_group = QGroupBox(self.tab)
        self.about_about_group.setObjectName(u"about_about_group")
        self.about_about_group.setGeometry(QRect(10, 210, 611, 171))
        self.about_author_title = QLabel(self.about_about_group)
        self.about_author_title.setObjectName(u"about_author_title")
        self.about_author_title.setGeometry(QRect(10, 40, 141, 31))
        self.about_github_title = QLabel(self.about_about_group)
        self.about_github_title.setObjectName(u"about_github_title")
        self.about_github_title.setGeometry(QRect(10, 60, 141, 31))
        self.about_github_http = KUrlLabel(self.about_about_group)
        self.about_github_http.setObjectName(u"about_github_http")
        self.about_github_http.setGeometry(QRect(70, 70, 221, 16))
        self.about_blog_title = QLabel(self.about_about_group)
        self.about_blog_title.setObjectName(u"about_blog_title")
        self.about_blog_title.setGeometry(QRect(10, 80, 141, 31))
        self.about_blog_http = KUrlLabel(self.about_about_group)
        self.about_blog_http.setObjectName(u"about_blog_http")
        self.about_blog_http.setGeometry(QRect(70, 90, 221, 16))
        self.about_donate_title = QLabel(self.about_about_group)
        self.about_donate_title.setObjectName(u"about_donate_title")
        self.about_donate_title.setGeometry(QRect(10, 100, 141, 31))
        self.about_donate_http = KUrlLabel(self.about_about_group)
        self.about_donate_http.setObjectName(u"about_donate_http")
        self.about_donate_http.setGeometry(QRect(70, 110, 221, 16))
        self.about_repo_title = QLabel(self.about_about_group)
        self.about_repo_title.setObjectName(u"about_repo_title")
        self.about_repo_title.setGeometry(QRect(10, 120, 141, 31))
        self.about_repo_http = KUrlLabel(self.about_about_group)
        self.about_repo_http.setObjectName(u"about_repo_http")
        self.about_repo_http.setGeometry(QRect(70, 130, 221, 16))
        self.about_qt_button = QPushButton(self.about_about_group)
        self.about_qt_button.setObjectName(u"about_qt_button")
        self.about_qt_button.setGeometry(QRect(510, 140, 88, 21))
        self.build.addTab(self.tab, "")
        self.verticalLayoutWidget = QWidget(Minecraft)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(660, 50, 141, 391))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.SSH_title = QLabel(self.verticalLayoutWidget)
        self.SSH_title.setObjectName(u"SSH_title")

        self.verticalLayout.addWidget(self.SSH_title)

        self.line = QFrame(self.verticalLayoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.IP_title = QLabel(self.verticalLayoutWidget)
        self.IP_title.setObjectName(u"IP_title")

        self.verticalLayout.addWidget(self.IP_title)

        self.IP_edit = QLineEdit(self.verticalLayoutWidget)
        self.IP_edit.setObjectName(u"IP_edit")

        self.verticalLayout.addWidget(self.IP_edit)

        self.Port_title = QLabel(self.verticalLayoutWidget)
        self.Port_title.setObjectName(u"Port_title")

        self.verticalLayout.addWidget(self.Port_title)

        self.Port_edit = QLineEdit(self.verticalLayoutWidget)
        self.Port_edit.setObjectName(u"Port_edit")

        self.verticalLayout.addWidget(self.Port_edit)

        self.User_title = QLabel(self.verticalLayoutWidget)
        self.User_title.setObjectName(u"User_title")

        self.verticalLayout.addWidget(self.User_title)

        self.User_edit = QLineEdit(self.verticalLayoutWidget)
        self.User_edit.setObjectName(u"User_edit")

        self.verticalLayout.addWidget(self.User_edit)

        self.Password_title = QLabel(self.verticalLayoutWidget)
        self.Password_title.setObjectName(u"Password_title")

        self.verticalLayout.addWidget(self.Password_title)

        self.Password_edit = KPasswordLineEdit(self.verticalLayoutWidget)
        self.Password_edit.setObjectName(u"Password_edit")

        self.verticalLayout.addWidget(self.Password_edit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Connect_button = QPushButton(self.verticalLayoutWidget)
        self.Connect_button.setObjectName(u"Connect_button")

        self.horizontalLayout.addWidget(self.Connect_button)

        self.Key_button = QToolButton(self.verticalLayoutWidget)
        self.Key_button.setObjectName(u"Key_button")

        self.horizontalLayout.addWidget(self.Key_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.progressBar = QProgressBar(self.verticalLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)


        self.retranslateUi(Minecraft)

        self.build.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Minecraft)
    # setupUi

    def retranslateUi(self, Minecraft):
        Minecraft.setWindowTitle(QCoreApplication.translate("Minecraft", u"Minecraft BDS Manager", None))
        self.control_servername_title.setText(QCoreApplication.translate("Minecraft", u"\u670d\u52a1\u5668\u540d\uff1a", None))
        self.control_servername_edit.setText(QCoreApplication.translate("Minecraft", u"Dedicated Server", None))
        self.control_gamemode_title.setText(QCoreApplication.translate("Minecraft", u"\u6e38\u620f\u6a21\u5f0f\uff1a", None))
        self.control_gamemode_combo.setItemText(0, QCoreApplication.translate("Minecraft", u"\u751f\u5b58", None))
        self.control_gamemode_combo.setItemText(1, QCoreApplication.translate("Minecraft", u"\u521b\u9020", None))
        self.control_gamemode_combo.setItemText(2, QCoreApplication.translate("Minecraft", u"\u6781\u9650", None))

        self.control_chest_title.setText(QCoreApplication.translate("Minecraft", u"\u4f5c\u5f0a\uff1a", None))
        self.control_chest_combo.setItemText(0, QCoreApplication.translate("Minecraft", u"\u542f\u7528", None))
        self.control_chest_combo.setItemText(1, QCoreApplication.translate("Minecraft", u"\u7981\u7528", None))

        self.control_maxplayer_title.setText(QCoreApplication.translate("Minecraft", u"\u6700\u5927\u73a9\u5bb6\u6570\uff1a", None))
        self.control_xbox_title.setText(QCoreApplication.translate("Minecraft", u"Xbox\u9a8c\u8bc1\uff1a", None))
        self.control_xbox_combo.setItemText(0, QCoreApplication.translate("Minecraft", u"\u542f\u7528", None))
        self.control_xbox_combo.setItemText(1, QCoreApplication.translate("Minecraft", u"\u7981\u7528", None))

        self.control_whitelist_title.setText(QCoreApplication.translate("Minecraft", u"\u767d\u540d\u5355\uff1a", None))
        self.control_whitelist_combo.setItemText(0, QCoreApplication.translate("Minecraft", u"\u542f\u7528", None))
        self.control_whitelist_combo.setItemText(1, QCoreApplication.translate("Minecraft", u"\u7981\u7528", None))

        self.control_view_title.setText(QCoreApplication.translate("Minecraft", u"\u89c6\u91ce\uff1a", None))
        self.control_tkdistance_title.setText(QCoreApplication.translate("Minecraft", u"Tick distance\uff1a", None))
        self.control_ktime_title.setText(QCoreApplication.translate("Minecraft", u"\u8e22\u51fa\u65f6\u95f4\uff1a", None))
        self.control_maxthread_title.setText(QCoreApplication.translate("Minecraft", u"\u6700\u5927\u7ebf\u7a0b\u6570\uff1a", None))
        self.control_playerchara_title.setText(QCoreApplication.translate("Minecraft", u"\u73a9\u5bb6\u8eab\u4efd\uff1a", None))
        self.control_playerchara_combo.setItemText(0, QCoreApplication.translate("Minecraft", u"\u6210\u5458", None))
        self.control_playerchara_combo.setItemText(1, QCoreApplication.translate("Minecraft", u"\u65c1\u89c2\u8005", None))
        self.control_playerchara_combo.setItemText(2, QCoreApplication.translate("Minecraft", u"\u7ba1\u7406\u5458", None))

        self.control_texture_title.setText(QCoreApplication.translate("Minecraft", u"\u6750\u8d28\u5305\uff1a", None))
        self.control_texture_combo.setItemText(0, QCoreApplication.translate("Minecraft", u"\u7981\u7528", None))
        self.control_texture_combo.setItemText(1, QCoreApplication.translate("Minecraft", u"\u542f\u7528", None))

        self.control_log_title.setText(QCoreApplication.translate("Minecraft", u"\u9519\u8bef\u65e5\u5fd7\uff1a", None))
        self.control_log_combo.setItemText(0, QCoreApplication.translate("Minecraft", u"\u7981\u7528", None))
        self.control_log_combo.setItemText(1, QCoreApplication.translate("Minecraft", u"\u542f\u7528", None))

        self.control_zip_title.setText(QCoreApplication.translate("Minecraft", u"\u538b\u7f29\u9600\u503c\uff1a", None))
        self.control_v4_title.setText(QCoreApplication.translate("Minecraft", u"IPv4\u7aef\u53e3\uff1a", None))
        self.control_v6_title.setText(QCoreApplication.translate("Minecraft", u"IPv6\u7aef\u53e3\uff1a", None))
        self.control_olplayer_title.setText(QCoreApplication.translate("Minecraft", u"\u5728\u7ebf\u73a9\u5bb6\uff1a", None))
        self.label_24.setText(QCoreApplication.translate("Minecraft", u"\u7ba1\u7406\u5458\uff1a", None))
        self.control_op_edit.setText(QCoreApplication.translate("Minecraft", u"\u6dfb\u52a0\u7ba1\u7406\u5458\uff1a", None))
        self.control_opadd_button.setText(QCoreApplication.translate("Minecraft", u"\u6dfb\u52a0", None))
        self.control_opdel_button.setText(QCoreApplication.translate("Minecraft", u"\u5220\u9664", None))
        self.control_command_edit.setText(QCoreApplication.translate("Minecraft", u"\u6309Enter\u6267\u884c\u670d\u52a1\u5668\u547d\u4ee4\uff1a", None))
        self.control_save.setText(QCoreApplication.translate("Minecraft", u"\u4fdd\u5b58", None))
        self.control_onkick_button.setText(QCoreApplication.translate("Minecraft", u"\u8e22\u51fa", None))
        self.build.setTabText(self.build.indexOf(self.Control), QCoreApplication.translate("Minecraft", u"\u670d\u52a1\u5668\u63a7\u5236", None))
        self.build_serverdown_title.setText(QCoreApplication.translate("Minecraft", u"\u670d\u52a1\u7aef\u4e0b\u8f7d\uff1a", None))
        self.build_log_title.setText(QCoreApplication.translate("Minecraft", u"\u5b89\u88c5\u65e5\u5fd7\uff1a", None))
        self.build_debian10_title.setText(QCoreApplication.translate("Minecraft", u"<h2>\u6ce8\uff1a\u6d4b\u8bd5\u529f\u80fd\u3002\u4ec5\u652f\u6301Debian10\uff01</h2>", None))
        self.build_build_button.setText(QCoreApplication.translate("Minecraft", u"\u5f00\u670d", None))
        self.build.setTabText(self.build.indexOf(self.build1), QCoreApplication.translate("Minecraft", u"\u4e00\u952e\u5f00\u670d", None))
        self.log_save_button.setText(QCoreApplication.translate("Minecraft", u"\u4fdd\u5b58\u65e5\u5fd7", None))
        self.log_save_choose.setFilter("")
        self.log_save_choose.setClickMessage(QCoreApplication.translate("Minecraft", u"\u4fdd\u5b58\u5230\uff1a", None))
        self.build.setTabText(self.build.indexOf(self.log), QCoreApplication.translate("Minecraft", u"\u65e5\u5fd7", None))
        self.whitelist_add_edit.setText(QCoreApplication.translate("Minecraft", u"\u6dfb\u52a0\u767d\u540d\u5355\uff1a", None))
        self.whitelist_del_button.setText(QCoreApplication.translate("Minecraft", u"\u5220\u9664", None))
        self.whitelist_add_button.setText(QCoreApplication.translate("Minecraft", u"\u6dfb\u52a0", None))
        self.build.setTabText(self.build.indexOf(self.whitelist), QCoreApplication.translate("Minecraft", u"\u767d\u540d\u5355\u7ba1\u7406", None))
        self.plugin_upload_choose.setFilter("")
        self.plugin_upload_choose.setClickMessage(QCoreApplication.translate("Minecraft", u"\u4e0a\u4f20\u63d2\u4ef6\uff1a", None))
        self.plugin_upload_choose.setPlaceholderText(QCoreApplication.translate("Minecraft", u"\u4e0a\u4f20\u63d2\u4ef6\uff1a", None))
        self.plugin_onoff_button.setText(QCoreApplication.translate("Minecraft", u"\u7981\u7528/\u542f\u7528", None))
        self.plugin_del_button.setText(QCoreApplication.translate("Minecraft", u"\u5220\u9664", None))
        self.build.setTabText(self.build.indexOf(self.tab_6), QCoreApplication.translate("Minecraft", u"\u63d2\u4ef6\u7ba1\u7406", None))
        self.pluginstore_ori_edit.setText(QCoreApplication.translate("Minecraft", u"\u81ea\u5b9a\u4e49\u6e90\uff1a", None))
        self.pluginstore_install_button.setText(QCoreApplication.translate("Minecraft", u"\u5b89\u88c5", None))
        self.pluginstore_switch_button.setText(QCoreApplication.translate("Minecraft", u"\u5207\u6362", None))
        self.build.setTabText(self.build.indexOf(self.tab_5), QCoreApplication.translate("Minecraft", u"\u63d2\u4ef6\u4ed3\u5e93", None))
        self.groupBox.setTitle(QCoreApplication.translate("Minecraft", u"\u8f6f\u4ef6\u8bbe\u7f6e", None))
        self.label_28.setText(QCoreApplication.translate("Minecraft", u"\u7248\u672c\uff1av1.0", None))
        self.pushButton_13.setText(QCoreApplication.translate("Minecraft", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Minecraft", u"\u8f6f\u4ef6\u8bbe\u7f6e", None))
        self.label_29.setText(QCoreApplication.translate("Minecraft", u"\u7248\u672c\uff1av1.0", None))
        self.pushButton_14.setText(QCoreApplication.translate("Minecraft", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Minecraft", u"\u8f6f\u4ef6\u8bbe\u7f6e", None))
        self.label_30.setText(QCoreApplication.translate("Minecraft", u"\u7248\u672c\uff1av1.0", None))
        self.pushButton_15.setText(QCoreApplication.translate("Minecraft", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.about_software_group.setTitle(QCoreApplication.translate("Minecraft", u"\u8f6f\u4ef6\u8bbe\u7f6e", None))
        self.about_software_title.setText(QCoreApplication.translate("Minecraft", u"\u7248\u672c\uff1av1.0", None))
        self.about_vcheck_button.setText(QCoreApplication.translate("Minecraft", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.about_thanks_group.setTitle(QCoreApplication.translate("Minecraft", u"\u9e23\u8c22", None))
        self.label_32.setText(QCoreApplication.translate("Minecraft", u"\u7248\u672c\uff1av1.0", None))
        self.pushButton_17.setText(QCoreApplication.translate("Minecraft", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.about_about_group.setTitle(QCoreApplication.translate("Minecraft", u"\u5173\u4e8e", None))
        self.about_author_title.setText(QCoreApplication.translate("Minecraft", u"\u4f5c\u8005\uff1aSakitami", None))
        self.about_github_title.setText(QCoreApplication.translate("Minecraft", u"Github\uff1a", None))
        self.about_github_http.setText(QCoreApplication.translate("Minecraft", u"https://www.github.com/Sakitami", None))
        self.about_blog_title.setText(QCoreApplication.translate("Minecraft", u"Blog\uff1a", None))
        self.about_blog_http.setText(QCoreApplication.translate("Minecraft", u"https://blog.skihome.xyz", None))
        self.about_donate_title.setText(QCoreApplication.translate("Minecraft", u"\u6350\u8d60\uff1a", None))
        self.about_donate_http.setText(QCoreApplication.translate("Minecraft", u"https://blog.skihome.xyz", None))
        self.about_repo_title.setText(QCoreApplication.translate("Minecraft", u"\u9879\u76ee\u5730\u5740\uff1a", None))
        self.about_repo_http.setText(QCoreApplication.translate("Minecraft", u"https://www.github.com/Sakitami", None))
        self.about_qt_button.setText(QCoreApplication.translate("Minecraft", u"\u5173\u4e8eQt", None))
        self.build.setTabText(self.build.indexOf(self.tab), QCoreApplication.translate("Minecraft", u"\u5173\u4e8e", None))
        self.SSH_title.setText(QCoreApplication.translate("Minecraft", u"<h3>SSH</h3>", None))
        self.IP_title.setText(QCoreApplication.translate("Minecraft", u"IP\uff1a", None))
        self.IP_edit.setText(QCoreApplication.translate("Minecraft", u"127.0.0.1", None))
        self.Port_title.setText(QCoreApplication.translate("Minecraft", u"\u7aef\u53e3\uff1a", None))
        self.Port_edit.setText(QCoreApplication.translate("Minecraft", u"22", None))
        self.User_title.setText(QCoreApplication.translate("Minecraft", u"\u7528\u6237\u540d\uff1a", None))
        self.User_edit.setText(QCoreApplication.translate("Minecraft", u"root", None))
        self.Password_title.setText(QCoreApplication.translate("Minecraft", u"\u5bc6\u7801\uff1a", None))
        self.Connect_button.setText(QCoreApplication.translate("Minecraft", u"\u8fde\u63a5", None))
        self.Key_button.setText(QCoreApplication.translate("Minecraft", u"...", None))
    # retranslateUi

