# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'remote_vedio_player_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 720)
        Form.setStyleSheet(u"QWidget{\n"
"	background:rgb(250,259,240);\n"
"}\n"
"QTextEdit{\n"
"	color:rgb(255,255,255);\n"
"	font: 12pt \"\u5e7c\u5706\";\n"
"\n"
"}\n"
"QPushButton{\n"
"    color:white;\n"
"	font: 15pt \"\u5e7c\u5706\";\n"
"	border-color:(255,255,255);\n"
"	border-width:1px;\n"
"	border-style:outset;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color:red;\n"
"	font: 15pt \"\u5e7c\u5706\";\n"
"	border-color:(255,255,255);\n"
"	border-width:1px;\n"
"	border-style:outset;\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    color:white;\n"
"	font: 17pt \"\u5e7c\u5706\";	\n"
"	border-style:inset;\n"
"	border-width:2px;\n"
"	border-radius:5px;\n"
"}\n"
"QLabel {\n"
"	color:rgb(255,255,255);\n"
"	font: 22pt \"\u5e7c\u5706\";\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.pushButton_vedio_report = QPushButton(Form)
        self.pushButton_vedio_report.setObjectName(u"pushButton_vedio_report")
        self.pushButton_vedio_report.setMinimumSize(QSize(100, 50))

        self.verticalLayout_2.addWidget(self.pushButton_vedio_report)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.pushButton_vedio_quit = QPushButton(Form)
        self.pushButton_vedio_quit.setObjectName(u"pushButton_vedio_quit")
        self.pushButton_vedio_quit.setMinimumSize(QSize(100, 50))

        self.verticalLayout_2.addWidget(self.pushButton_vedio_quit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 100)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_vedio_report.setText(QCoreApplication.translate("Form", u"\u56de\u653e", None))
        self.pushButton_vedio_quit.setText(QCoreApplication.translate("Form", u"\u9000\u51fa", None))
    # retranslateUi

