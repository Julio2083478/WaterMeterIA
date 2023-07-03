# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'INTERFAZMOCKUPFINALGJyUdw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 731)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1300, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color: rgb(85, 255, 255);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"QWidget #centralwidget{\n"
"background-color: #715bff;\n"
"}\n"
"")
        self.verticalLayout_21 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_sup = QFrame(self.centralwidget)
        self.frame_sup.setObjectName(u"frame_sup")
        sizePolicy.setHeightForWidth(self.frame_sup.sizePolicy().hasHeightForWidth())
        self.frame_sup.setSizePolicy(sizePolicy)
        self.frame_sup.setMinimumSize(QSize(150, 70))
        self.frame_sup.setMaximumSize(QSize(16777215, 70))
        self.frame_sup.setStyleSheet(u"background-color: #151f28;")
        self.frame_sup.setFrameShape(QFrame.StyledPanel)
        self.frame_sup.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_sup)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 1, 15, 1)
        self.bt_menu = QPushButton(self.frame_sup)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"ICONOS/MENUBAR_BLANCOO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)
        self.bt_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_menu)

        self.bt_atras = QPushButton(self.frame_sup)
        self.bt_atras.setObjectName(u"bt_atras")
        self.bt_atras.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"ICONOS/ATRAS_WITHE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_atras.setIcon(icon1)
        self.bt_atras.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.bt_atras)

        self.label_2 = QLabel(self.frame_sup)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setMinimumSize(QSize(210, 60))
        self.label_2.setMaximumSize(QSize(210, 60))
        self.label_2.setStyleSheet(u"font: 26pt \"Ubuntu Mono\";\n"
"color: white;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.bt_logosup = QPushButton(self.frame_sup)
        self.bt_logosup.setObjectName(u"bt_logosup")
        self.bt_logosup.setStyleSheet(u"border:0px;")
        icon2 = QIcon()
        icon2.addFile(u"ICONOS/LOGO_WATER_METER.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_logosup.setIcon(icon2)
        self.bt_logosup.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.bt_logosup)

        self.horizontalSpacer = QSpacerItem(521, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.consumo_total_m = QLabel(self.frame_sup)
        self.consumo_total_m.setObjectName(u"consumo_total_m")
        sizePolicy1.setHeightForWidth(self.consumo_total_m.sizePolicy().hasHeightForWidth())
        self.consumo_total_m.setSizePolicy(sizePolicy1)
        self.consumo_total_m.setMinimumSize(QSize(300, 55))
        self.consumo_total_m.setMaximumSize(QSize(300, 55))
        self.consumo_total_m.setStyleSheet(u"background-color: #ffef65;\n"
"border: 5px solid black;\n"
"border-color: black;\n"
"color:black;\n"
"font: 2200 15pt \"Ubuntu Mono\";")

        self.horizontalLayout_2.addWidget(self.consumo_total_m, 0, Qt.AlignLeft)

        self.consumo_m_numero = QLabel(self.frame_sup)
        self.consumo_m_numero.setObjectName(u"consumo_m_numero")
        sizePolicy1.setHeightForWidth(self.consumo_m_numero.sizePolicy().hasHeightForWidth())
        self.consumo_m_numero.setSizePolicy(sizePolicy1)
        self.consumo_m_numero.setMinimumSize(QSize(150, 55))
        self.consumo_m_numero.setMaximumSize(QSize(150, 55))
        self.consumo_m_numero.setStyleSheet(u"background-color: #90CAF9;\n"
"border: 5px solid black;\n"
"border-color: black;\n"
"color:black;\n"
"font: 2200 15pt \"Ubuntu Mono\";")

        self.horizontalLayout_2.addWidget(self.consumo_m_numero, 0, Qt.AlignLeft)

        self.alerta_consumo = QLabel(self.frame_sup)
        self.alerta_consumo.setObjectName(u"alerta_consumo")
        self.alerta_consumo.setMinimumSize(QSize(150, 55))
        self.alerta_consumo.setMaximumSize(QSize(150, 55))
        self.alerta_consumo.setStyleSheet(u"background-color: #90CAF9;\n"
"border: 5px solid black;\n"
"border-color: black;\n"
"color:black;\n"
"font: 2200 15pt \"Ubuntu Mono\";")

        self.horizontalLayout_2.addWidget(self.alerta_consumo)

        self.precio_consumo_total = QLabel(self.frame_sup)
        self.precio_consumo_total.setObjectName(u"precio_consumo_total")
        self.precio_consumo_total.setMinimumSize(QSize(150, 55))
        self.precio_consumo_total.setMaximumSize(QSize(150, 55))
        self.precio_consumo_total.setStyleSheet(u"background-color: #90CAF9;\n"
"border: 5px solid black;\n"
"border-color: black;\n"
"color:black;\n"
"font: 2200 15pt \"Ubuntu Mono\";")

        self.horizontalLayout_2.addWidget(self.precio_consumo_total)

        self.pushButton_2 = QPushButton(self.frame_sup)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(40, 40))
        self.pushButton_2.setMaximumSize(QSize(40, 40))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"ICONOS/USER_BLANCO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon3)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.verticalLayout_21.addWidget(self.frame_sup)

        self.frame_inf = QFrame(self.centralwidget)
        self.frame_inf.setObjectName(u"frame_inf")
        sizePolicy.setHeightForWidth(self.frame_inf.sizePolicy().hasHeightForWidth())
        self.frame_inf.setSizePolicy(sizePolicy)
        self.frame_inf.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_inf.setFrameShape(QFrame.StyledPanel)
        self.frame_inf.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inf)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inf)
        self.frame_lateral.setObjectName(u"frame_lateral")
        sizePolicy.setHeightForWidth(self.frame_lateral.sizePolicy().hasHeightForWidth())
        self.frame_lateral.setSizePolicy(sizePolicy)
        self.frame_lateral.setMinimumSize(QSize(0, 0))
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setStyleSheet(u"QFrame{\n"
"background-color:#151f28;\n"
"}\n"
"\n"
"")
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_p1 = QPushButton(self.frame_lateral)
        self.btn_p1.setObjectName(u"btn_p1")
        sizePolicy1.setHeightForWidth(self.btn_p1.sizePolicy().hasHeightForWidth())
        self.btn_p1.setSizePolicy(sizePolicy1)
        self.btn_p1.setMinimumSize(QSize(0, 40))
        self.btn_p1.setMaximumSize(QSize(16777215, 40))
        self.btn_p1.setStyleSheet(u"QPushButton{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #151f28;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_p1)

        self.btn_p2 = QPushButton(self.frame_lateral)
        self.btn_p2.setObjectName(u"btn_p2")
        self.btn_p2.setMinimumSize(QSize(0, 40))
        self.btn_p2.setMaximumSize(QSize(16777215, 40))
        self.btn_p2.setStyleSheet(u"QPushButton{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #151f28;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_p2)

        self.btn_p3 = QPushButton(self.frame_lateral)
        self.btn_p3.setObjectName(u"btn_p3")
        self.btn_p3.setMinimumSize(QSize(0, 40))
        self.btn_p3.setMaximumSize(QSize(16777215, 40))
        self.btn_p3.setStyleSheet(u"QPushButton{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #151f28;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_p3)

        self.btn_p4 = QPushButton(self.frame_lateral)
        self.btn_p4.setObjectName(u"btn_p4")
        self.btn_p4.setMinimumSize(QSize(0, 40))
        self.btn_p4.setMaximumSize(QSize(16777215, 40))
        self.btn_p4.setStyleSheet(u"QPushButton{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #151f28;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_p4)

        self.btn_p5 = QPushButton(self.frame_lateral)
        self.btn_p5.setObjectName(u"btn_p5")
        self.btn_p5.setMinimumSize(QSize(0, 40))
        self.btn_p5.setMaximumSize(QSize(16777215, 40))
        self.btn_p5.setStyleSheet(u"QPushButton{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #151f28;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_p5)

        self.btn_p6 = QPushButton(self.frame_lateral)
        self.btn_p6.setObjectName(u"btn_p6")
        self.btn_p6.setMinimumSize(QSize(0, 40))
        self.btn_p6.setMaximumSize(QSize(16777215, 40))
        self.btn_p6.setStyleSheet(u"QPushButton{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #151f28;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_p6)

        self.btn_p7 = QPushButton(self.frame_lateral)
        self.btn_p7.setObjectName(u"btn_p7")
        self.btn_p7.setMinimumSize(QSize(0, 40))
        self.btn_p7.setMaximumSize(QSize(16777215, 40))
        self.btn_p7.setStyleSheet(u"QPushButton{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #151f28;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: #90CAF9;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.btn_p7)

        self.verticalSpacer = QSpacerItem(20, 290, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.logo_uis = QPushButton(self.frame_lateral)
        self.logo_uis.setObjectName(u"logo_uis")
        self.logo_uis.setStyleSheet(u"QPushButton{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"background-color: #151f28; \n"
"}\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u"ICONOS/LOGO UIS_PNG.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_uis.setIcon(icon4)
        self.logo_uis.setIconSize(QSize(130, 80))

        self.verticalLayout_3.addWidget(self.logo_uis)


        self.horizontalLayout.addWidget(self.frame_lateral)

        self.frame_contenedor = QFrame(self.frame_inf)
        self.frame_contenedor.setObjectName(u"frame_contenedor")
        sizePolicy.setHeightForWidth(self.frame_contenedor.sizePolicy().hasHeightForWidth())
        self.frame_contenedor.setSizePolicy(sizePolicy)
        self.frame_contenedor.setFrameShape(QFrame.StyledPanel)
        self.frame_contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_contenedor)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_contenedor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page_inicio = QWidget()
        self.page_inicio.setObjectName(u"page_inicio")
        sizePolicy.setHeightForWidth(self.page_inicio.sizePolicy().hasHeightForWidth())
        self.page_inicio.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.page_inicio)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_inicio)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet(u"background-color: #90CAF9;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.LOGO = QPushButton(self.frame)
        self.LOGO.setObjectName(u"LOGO")
        sizePolicy.setHeightForWidth(self.LOGO.sizePolicy().hasHeightForWidth())
        self.LOGO.setSizePolicy(sizePolicy)
        self.LOGO.setStyleSheet(u"QPushButton{\n"
"border: 0px;\n"
"}")
        self.LOGO.setIcon(icon2)
        self.LOGO.setIconSize(QSize(350, 350))

        self.verticalLayout_4.addWidget(self.LOGO)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 26pt \"Ubuntu Mono\";\n"
"color: black;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_3)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 20pt \"Ubuntu Mono\";\n"
"color: black;")

        self.verticalLayout_4.addWidget(self.label)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 20pt \"Ubuntu Mono\";\n"
"\n"
"color: black;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 18pt \"Ubuntu Mono\";\n"
"\n"
"color: black;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.verticalLayout_4.setStretch(0, 5)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)
        self.verticalLayout_4.setStretch(4, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_inicio)
        self.page_uno = QWidget()
        self.page_uno.setObjectName(u"page_uno")
        sizePolicy.setHeightForWidth(self.page_uno.sizePolicy().hasHeightForWidth())
        self.page_uno.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.page_uno)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_uno)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: #90CAF9;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font:520 15pt \"Ubuntu Mono\";\n"
"border-radius:0px;\n"
"color: white;\n"
"background-color: rgb(113, 91, 255);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_2)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy1.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy1)
        self.frame_21.setMinimumSize(QSize(0, 100))
        self.frame_21.setMaximumSize(QSize(16777215, 100))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.bt_newref = QPushButton(self.frame_21)
        self.bt_newref.setObjectName(u"bt_newref")
        self.bt_newref.setStyleSheet(u"border-style: solid;\n"
"border-width: 3px;\n"
"border-radius:33px;\n"
"background-color: #90CAF9;")
        icon5 = QIcon()
        icon5.addFile(u"ICONOS/PLUS_WHITE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_newref.setIcon(icon5)
        self.bt_newref.setIconSize(QSize(64, 64))

        self.horizontalLayout_7.addWidget(self.bt_newref)

        self.bt_x = QPushButton(self.frame_21)
        self.bt_x.setObjectName(u"bt_x")
        font = QFont()
        font.setFamily(u"Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(65)
        self.bt_x.setFont(font)
        self.bt_x.setStyleSheet(u"border-style: solid;\n"
"border-width: 3px;\n"
"border-radius:33px;\n"
"background-color:#90CAF9;")
        icon6 = QIcon()
        icon6.addFile(u"ICONOS/X_WHITE.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_x.setIcon(icon6)
        self.bt_x.setIconSize(QSize(64, 64))

        self.horizontalLayout_7.addWidget(self.bt_x)

        self.btn_menu_elim_ref = QPushButton(self.frame_21)
        self.btn_menu_elim_ref.setObjectName(u"btn_menu_elim_ref")
        self.btn_menu_elim_ref.setMinimumSize(QSize(200, 70))
        self.btn_menu_elim_ref.setMaximumSize(QSize(200, 70))
        self.btn_menu_elim_ref.setStyleSheet(u"border-style: solid;\n"
"border-width: 3px;\n"
"border-radius:33px;\n"
"background-color: #90CAF9;")

        self.horizontalLayout_7.addWidget(self.btn_menu_elim_ref)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addWidget(self.frame_21)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tablaregistros = QTableWidget(self.frame_3)
        self.tablaregistros.setObjectName(u"tablaregistros")

        self.verticalLayout_6.addWidget(self.tablaregistros)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_uno)
        self.page_tres = QWidget()
        self.page_tres.setObjectName(u"page_tres")
        sizePolicy.setHeightForWidth(self.page_tres.sizePolicy().hasHeightForWidth())
        self.page_tres.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.page_tres)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_tres)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setStyleSheet(u"background-color: rgb(113, 91, 255);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_4)
        self.label_35.setObjectName(u"label_35")
        sizePolicy1.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy1)
        self.label_35.setMinimumSize(QSize(0, 50))
        self.label_35.setMaximumSize(QSize(16777215, 50))
        self.label_35.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;")
        self.label_35.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_35)

        self.frame_canvas3 = QFrame(self.frame_4)
        self.frame_canvas3.setObjectName(u"frame_canvas3")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_canvas3.sizePolicy().hasHeightForWidth())
        self.frame_canvas3.setSizePolicy(sizePolicy3)
        self.frame_canvas3.setMinimumSize(QSize(0, 0))
        self.frame_canvas3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_canvas3.setStyleSheet(u"background-color: #FFEF65;")
        self.frame_canvas3.setFrameShape(QFrame.StyledPanel)
        self.frame_canvas3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.frame_canvas3)

        self.frame_20 = QFrame(self.frame_4)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy3.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy3)
        self.frame_20.setMinimumSize(QSize(0, 270))
        self.frame_20.setMaximumSize(QSize(16777215, 270))
        self.frame_20.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_12.setSpacing(9)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.frame_24 = QFrame(self.frame_20)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy3.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy3)
        self.frame_24.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_24)
        self.verticalLayout_25.setSpacing(6)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_27 = QLabel(self.frame_24)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 22000 6pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_25.addWidget(self.label_27)

        self.calendariomensual = QCalendarWidget(self.frame_24)
        self.calendariomensual.setObjectName(u"calendariomensual")
        sizePolicy3.setHeightForWidth(self.calendariomensual.sizePolicy().hasHeightForWidth())
        self.calendariomensual.setSizePolicy(sizePolicy3)
        self.calendariomensual.setMaximumSize(QSize(320, 200))
        self.calendariomensual.setStyleSheet(u"QCalendarWidget QWidget {\n"
"	 alternate-background-color: #ffffff;\n"
"}\n"
"\n"
"/* style for top navigation area ###############################################*/ \n"
"\n"
"#qt_calendar_navigationbar {\n"
"    background-color: #151f28;\n"
"	border: 2px solid  #ffef65;\n"
"	border-bottom: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* style for month change buttons ############################################ */\n"
"\n"
"\n"
"\n"
"\n"
"/* Style for month and yeat buttons #################################### */\n"
"\n"
"#qt_calendar_yearbutton {\n"
"    color: #000000;\n"
"	margin:5px;\n"
"    border-radius: 5px;\n"
"	background-color: #e0e0e0;\n"
"	font-size: 13px;\n"
"	padding:0px 10px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"	width: 110px;\n"
"    color: #000000;\n"
"	font-size: 13px;\n"
"	margin:5px 0px;\n"
"    border-radius: 5px;\n"
"	background-color: #e0e0e0;\n"
"	padding:0px 2px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_mont"
                        "hbutton:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/* Style for year input lineEdit ######################################*/\n"
"\n"
"#qt_calendar_yearedit {\n"
"    min-width: 53px;\n"
"    color: #fef128;\n"
"    background: transparent;\n"
"	font-size: 13px;\n"
"}\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"	/* border delete */\n"
"    border: none;  \n"
"  \n"
"	/* set background transparent */\n"
"    background-color: transparent; \n"
"	padding: 5px;\n"
"}\n"
"/* Style for year change buttons ######################################*/\n"
"\n"
"#qt_calendar_yearedit::up-button { \n"
"	image: url(:/icon/arrow-151-48.ico);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button { \n"
"	image: url(:/icon/arrow-213-48.ico);\n"
"    subcontrol-position: left; \n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
""
                        "#qt_calendar_yearedit::up-button {\n"
"	width:10px;\n"
"	padding: 0px 5px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button:hover, \n"
"#qt_calendar_yearedit::up-button:hover {\n"
"	background-color: #fef128;\n"
"}\n"
"\n"
"/* Style for month select menu ##################################### */\n"
"\n"
"#calendarWidget QToolButton QMenu {\n"
"     background-color: white;\n"
"\n"
"}\n"
"#calendarWidget QToolButton QMenu::item {\n"
"	/*padding: 10px;*/\n"
"}\n"
" #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidget QToolButton::menu-indicator {\n"
"	/* Remove toolButton arrow */\n"
"      /*image: none; */\n"
"	nosubcontrol-origin: margin;\n"
"	subcontrol-position: right center;\n"
"	margin-top: 10px;\n"
"	width:20px;\n"
"}\n"
"\n"
"/* Style for calendar table ########################################## */\n"
"#qt_calendar_calendarview {\n"
"	/* Remove the selected dashed box */\n"
"    outline: 0px;\n"
"	color: #000"
                        "000;\n"
"	border: 2px solid  #fef128;\n"
"	background-color: #e0e0e0;\n"
"	border-top: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	\n"
"	font: 733335 8pt \"Ubuntu Mono\";\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"   border-radius:5px;\n"
"	background-color:#aaffff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected {\n"
"    background-color: #55aa7f; \n"
"	border-radius:5px;\n"
"}")

        self.verticalLayout_25.addWidget(self.calendariomensual)


        self.horizontalLayout_12.addWidget(self.frame_24, 0, Qt.AlignHCenter)

        self.frame_25 = QFrame(self.frame_20)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy3.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy3)
        self.frame_25.setMinimumSize(QSize(600, 0))
        self.frame_25.setMaximumSize(QSize(600, 16777215))
        self.frame_25.setStyleSheet(u"background-color: #90CAF9;\n"
"")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_25)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_30 = QLabel(self.frame_25)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(300, 50))
        self.label_30.setMaximumSize(QSize(300, 50))
        self.label_30.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_26.addWidget(self.label_30, 0, Qt.AlignHCenter)

        self.frame_pico_dia_3 = QFrame(self.frame_25)
        self.frame_pico_dia_3.setObjectName(u"frame_pico_dia_3")
        sizePolicy3.setHeightForWidth(self.frame_pico_dia_3.sizePolicy().hasHeightForWidth())
        self.frame_pico_dia_3.setSizePolicy(sizePolicy3)
        self.frame_pico_dia_3.setMinimumSize(QSize(580, 70))
        self.frame_pico_dia_3.setMaximumSize(QSize(580, 70))
        self.frame_pico_dia_3.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_pico_dia_3.setFrameShape(QFrame.StyledPanel)
        self.frame_pico_dia_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_pico_dia_3)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(28, 0, 28, 0)
        self.label_31 = QLabel(self.frame_pico_dia_3)
        self.label_31.setObjectName(u"label_31")
        sizePolicy3.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy3)
        self.label_31.setMinimumSize(QSize(350, 50))
        self.label_31.setMaximumSize(QSize(350, 50))
        self.label_31.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #151f28;\n"
"border: 5px solid black;\n"
"border-color: white;\n"
"color:white;\n"
"")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_31)

        self.label_32 = QLabel(self.frame_pico_dia_3)
        self.label_32.setObjectName(u"label_32")
        sizePolicy3.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy3)
        self.label_32.setMinimumSize(QSize(170, 50))
        self.label_32.setMaximumSize(QSize(170, 50))
        self.label_32.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #151f28;\n"
"border: 5px solid black;\n"
"border-color: white;\n"
"color:white;")
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_32)


        self.verticalLayout_26.addWidget(self.frame_pico_dia_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_12.addWidget(self.frame_25, 0, Qt.AlignHCenter)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_7.addWidget(self.frame_20)


        self.verticalLayout_9.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_tres)
        self.page_dos = QWidget()
        self.page_dos.setObjectName(u"page_dos")
        sizePolicy.setHeightForWidth(self.page_dos.sizePolicy().hasHeightForWidth())
        self.page_dos.setSizePolicy(sizePolicy)
        self.gridLayout_5 = QGridLayout(self.page_dos)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.page_dos)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setStyleSheet(u"background-color: rgb(113, 91, 255);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_5)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        sizePolicy1.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy1)
        self.label_6.setMinimumSize(QSize(0, 50))
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.frame_canvas1 = QFrame(self.frame_5)
        self.frame_canvas1.setObjectName(u"frame_canvas1")
        sizePolicy3.setHeightForWidth(self.frame_canvas1.sizePolicy().hasHeightForWidth())
        self.frame_canvas1.setSizePolicy(sizePolicy3)
        self.frame_canvas1.setMinimumSize(QSize(0, 0))
        self.frame_canvas1.setMaximumSize(QSize(16777215, 16777215))
        self.frame_canvas1.setStyleSheet(u"background-color: #FFEF65;")
        self.frame_canvas1.setFrameShape(QFrame.StyledPanel)
        self.frame_canvas1.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame_canvas1)

        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy3.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy3)
        self.frame_14.setMinimumSize(QSize(0, 270))
        self.frame_14.setMaximumSize(QSize(16777215, 270))
        self.frame_14.setStyleSheet(u"background-color:#90CAF9;")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 9, 9, 9)
        self.frame_18 = QFrame(self.frame_14)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy3.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy3)
        self.frame_18.setStyleSheet(u"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_18)
        self.verticalLayout_20.setSpacing(6)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(9, 9, 9, 9)
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 22000 6pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_20.addWidget(self.label_20)

        self.calendarWidget = QCalendarWidget(self.frame_18)
        self.calendarWidget.setObjectName(u"calendarWidget")
        sizePolicy3.setHeightForWidth(self.calendarWidget.sizePolicy().hasHeightForWidth())
        self.calendarWidget.setSizePolicy(sizePolicy3)
        self.calendarWidget.setMaximumSize(QSize(320, 200))
        self.calendarWidget.setStyleSheet(u"QCalendarWidget QWidget {\n"
"	 alternate-background-color: #ffffff;\n"
"}\n"
"\n"
"/* style for top navigation area ###############################################*/ \n"
"\n"
"#qt_calendar_navigationbar {\n"
"    background-color: #151f28;\n"
"	border: 2px solid  #ffef65;\n"
"	border-bottom: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* style for month change buttons ############################################ */\n"
"\n"
"\n"
"\n"
"\n"
"/* Style for month and yeat buttons #################################### */\n"
"\n"
"#qt_calendar_yearbutton {\n"
"    color: #000000;\n"
"	margin:5px;\n"
"    border-radius: 5px;\n"
"	background-color: #e0e0e0;\n"
"	font-size: 13px;\n"
"	padding:0px 10px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"	width: 110px;\n"
"    color: #000000;\n"
"	font-size: 13px;\n"
"	margin:5px 0px;\n"
"    border-radius: 5px;\n"
"	background-color: #e0e0e0;\n"
"	padding:0px 2px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_mont"
                        "hbutton:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/* Style for year input lineEdit ######################################*/\n"
"\n"
"#qt_calendar_yearedit {\n"
"    min-width: 53px;\n"
"    color: #fef128;\n"
"    background: transparent;\n"
"	font-size: 13px;\n"
"}\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"	/* border delete */\n"
"    border: none;  \n"
"  \n"
"	/* set background transparent */\n"
"    background-color: transparent; \n"
"	padding: 5px;\n"
"}\n"
"/* Style for year change buttons ######################################*/\n"
"\n"
"#qt_calendar_yearedit::up-button { \n"
"	image: url(:/icon/arrow-151-48.ico);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button { \n"
"	image: url(:/icon/arrow-213-48.ico);\n"
"    subcontrol-position: left; \n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
""
                        "#qt_calendar_yearedit::up-button {\n"
"	width:10px;\n"
"	padding: 0px 5px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button:hover, \n"
"#qt_calendar_yearedit::up-button:hover {\n"
"	background-color: #fef128;\n"
"}\n"
"\n"
"/* Style for month select menu ##################################### */\n"
"\n"
"#calendarWidget QToolButton QMenu {\n"
"     background-color: white;\n"
"\n"
"}\n"
"#calendarWidget QToolButton QMenu::item {\n"
"	/*padding: 10px;*/\n"
"}\n"
" #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidget QToolButton::menu-indicator {\n"
"	/* Remove toolButton arrow */\n"
"      /*image: none; */\n"
"	nosubcontrol-origin: margin;\n"
"	subcontrol-position: right center;\n"
"	margin-top: 10px;\n"
"	width:20px;\n"
"}\n"
"\n"
"/* Style for calendar table ########################################## */\n"
"#qt_calendar_calendarview {\n"
"	/* Remove the selected dashed box */\n"
"    outline: 0px;\n"
"	color: #000"
                        "000;\n"
"	border: 2px solid  #fef128;\n"
"	background-color: #e0e0e0;\n"
"	border-top: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	\n"
"	font: 733335 8pt \"Ubuntu Mono\";\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"   border-radius:5px;\n"
"	background-color:#aaffff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected {\n"
"    background-color: #55aa7f; \n"
"	border-radius:5px;\n"
"}")

        self.verticalLayout_20.addWidget(self.calendarWidget)


        self.horizontalLayout_5.addWidget(self.frame_18, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy3.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy3)
        self.frame_17.setMinimumSize(QSize(600, 0))
        self.frame_17.setMaximumSize(QSize(600, 16777215))
        self.frame_17.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_17)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(9, 9, 9, 9)
        self.label_19 = QLabel(self.frame_17)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(300, 50))
        self.label_19.setMaximumSize(QSize(300, 50))
        self.label_19.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_18.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.frame_pico_dia = QFrame(self.frame_17)
        self.frame_pico_dia.setObjectName(u"frame_pico_dia")
        sizePolicy3.setHeightForWidth(self.frame_pico_dia.sizePolicy().hasHeightForWidth())
        self.frame_pico_dia.setSizePolicy(sizePolicy3)
        self.frame_pico_dia.setMinimumSize(QSize(580, 70))
        self.frame_pico_dia.setMaximumSize(QSize(580, 70))
        self.frame_pico_dia.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_pico_dia.setFrameShape(QFrame.StyledPanel)
        self.frame_pico_dia.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_pico_dia)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(28, 0, 28, 0)
        self.label_11 = QLabel(self.frame_pico_dia)
        self.label_11.setObjectName(u"label_11")
        sizePolicy3.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy3)
        self.label_11.setMinimumSize(QSize(350, 50))
        self.label_11.setMaximumSize(QSize(350, 50))
        self.label_11.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #151f28;\n"
"border: 5px solid black;\n"
"border-color: white;\n"
"color:white;\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.label_12 = QLabel(self.frame_pico_dia)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setMinimumSize(QSize(170, 50))
        self.label_12.setMaximumSize(QSize(170, 50))
        self.label_12.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #151f28;\n"
"border: 5px solid black;\n"
"border-color: white;\n"
"color:white;\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_12)


        self.verticalLayout_18.addWidget(self.frame_pico_dia, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.frame_17, 0, Qt.AlignHCenter)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout.addWidget(self.frame_14)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(2, 1)

        self.gridLayout_5.addWidget(self.frame_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_dos)
        self.page_cuatro = QWidget()
        self.page_cuatro.setObjectName(u"page_cuatro")
        self.gridLayout_6 = QGridLayout(self.page_cuatro)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.page_cuatro)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setStyleSheet(u"background-color: rgb(113, 91, 255);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        sizePolicy1.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy1)
        self.label_8.setMinimumSize(QSize(0, 50))
        self.label_8.setMaximumSize(QSize(16777215, 50))
        self.label_8.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_8)

        self.frame_canvas2 = QFrame(self.frame_6)
        self.frame_canvas2.setObjectName(u"frame_canvas2")
        sizePolicy3.setHeightForWidth(self.frame_canvas2.sizePolicy().hasHeightForWidth())
        self.frame_canvas2.setSizePolicy(sizePolicy3)
        self.frame_canvas2.setMinimumSize(QSize(0, 0))
        self.frame_canvas2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_canvas2.setStyleSheet(u"background-color: #FFEF65;")
        self.frame_canvas2.setFrameShape(QFrame.StyledPanel)
        self.frame_canvas2.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_canvas2)

        self.frame_19 = QFrame(self.frame_6)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy3.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy3)
        self.frame_19.setMinimumSize(QSize(0, 270))
        self.frame_19.setMaximumSize(QSize(16777215, 270))
        self.frame_19.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_9.setSpacing(9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(9, 9, 9, 9)
        self.frame_22 = QFrame(self.frame_19)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy3.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy3)
        self.frame_22.setStyleSheet(u"")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_22)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_14 = QLabel(self.frame_22)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"font: 22000 6pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_23.addWidget(self.label_14)

        self.calendariosemanal = QCalendarWidget(self.frame_22)
        self.calendariosemanal.setObjectName(u"calendariosemanal")
        sizePolicy3.setHeightForWidth(self.calendariosemanal.sizePolicy().hasHeightForWidth())
        self.calendariosemanal.setSizePolicy(sizePolicy3)
        self.calendariosemanal.setMaximumSize(QSize(320, 200))
        self.calendariosemanal.setStyleSheet(u"QCalendarWidget QWidget {\n"
"	 alternate-background-color: #ffffff;\n"
"}\n"
"\n"
"/* style for top navigation area ###############################################*/ \n"
"\n"
"#qt_calendar_navigationbar {\n"
"    background-color: #151f28;\n"
"	border: 2px solid  #ffef65;\n"
"	border-bottom: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* style for month change buttons ############################################ */\n"
"\n"
"\n"
"\n"
"\n"
"/* Style for month and yeat buttons #################################### */\n"
"\n"
"#qt_calendar_yearbutton {\n"
"    color: #000000;\n"
"	margin:5px;\n"
"    border-radius: 5px;\n"
"	background-color: #e0e0e0;\n"
"	font-size: 13px;\n"
"	padding:0px 10px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"	width: 110px;\n"
"    color: #000000;\n"
"	font-size: 13px;\n"
"	margin:5px 0px;\n"
"    border-radius: 5px;\n"
"	background-color: #e0e0e0;\n"
"	padding:0px 2px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_mont"
                        "hbutton:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/* Style for year input lineEdit ######################################*/\n"
"\n"
"#qt_calendar_yearedit {\n"
"    min-width: 53px;\n"
"    color: #fef128;\n"
"    background: transparent;\n"
"	font-size: 13px;\n"
"}\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"	/* border delete */\n"
"    border: none;  \n"
"  \n"
"	/* set background transparent */\n"
"    background-color: transparent; \n"
"	padding: 5px;\n"
"}\n"
"/* Style for year change buttons ######################################*/\n"
"\n"
"#qt_calendar_yearedit::up-button { \n"
"	image: url(:/icon/arrow-151-48.ico);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button { \n"
"	image: url(:/icon/arrow-213-48.ico);\n"
"    subcontrol-position: left; \n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
""
                        "#qt_calendar_yearedit::up-button {\n"
"	width:10px;\n"
"	padding: 0px 5px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button:hover, \n"
"#qt_calendar_yearedit::up-button:hover {\n"
"	background-color: #fef128;\n"
"}\n"
"\n"
"/* Style for month select menu ##################################### */\n"
"\n"
"#calendarWidget QToolButton QMenu {\n"
"     background-color: white;\n"
"\n"
"}\n"
"#calendarWidget QToolButton QMenu::item {\n"
"	/*padding: 10px;*/\n"
"}\n"
" #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidget QToolButton::menu-indicator {\n"
"	/* Remove toolButton arrow */\n"
"      /*image: none; */\n"
"	nosubcontrol-origin: margin;\n"
"	subcontrol-position: right center;\n"
"	margin-top: 10px;\n"
"	width:20px;\n"
"}\n"
"\n"
"/* Style for calendar table ########################################## */\n"
"#qt_calendar_calendarview {\n"
"	/* Remove the selected dashed box */\n"
"    outline: 0px;\n"
"	color: #000"
                        "000;\n"
"	border: 2px solid  #fef128;\n"
"	background-color: #e0e0e0;\n"
"	border-top: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	\n"
"	font: 733335 8pt \"Ubuntu Mono\";\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"   border-radius:5px;\n"
"	background-color:#aaffff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected {\n"
"    background-color: #55aa7f; \n"
"	border-radius:5px;\n"
"}")

        self.verticalLayout_23.addWidget(self.calendariosemanal)


        self.horizontalLayout_9.addWidget(self.frame_22, 0, Qt.AlignHCenter)

        self.frame_23 = QFrame(self.frame_19)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy3.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy3)
        self.frame_23.setMinimumSize(QSize(600, 0))
        self.frame_23.setMaximumSize(QSize(600, 16777215))
        self.frame_23.setStyleSheet(u"background-color: #90CAF9;\n"
"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_23)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_13 = QLabel(self.frame_23)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(300, 50))
        self.label_13.setMaximumSize(QSize(300, 50))
        self.label_13.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_24.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.frame_pico_dia_2 = QFrame(self.frame_23)
        self.frame_pico_dia_2.setObjectName(u"frame_pico_dia_2")
        sizePolicy3.setHeightForWidth(self.frame_pico_dia_2.sizePolicy().hasHeightForWidth())
        self.frame_pico_dia_2.setSizePolicy(sizePolicy3)
        self.frame_pico_dia_2.setMinimumSize(QSize(580, 70))
        self.frame_pico_dia_2.setMaximumSize(QSize(580, 70))
        self.frame_pico_dia_2.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_pico_dia_2.setFrameShape(QFrame.StyledPanel)
        self.frame_pico_dia_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_pico_dia_2)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(28, 0, 28, 0)
        self.label_23 = QLabel(self.frame_pico_dia_2)
        self.label_23.setObjectName(u"label_23")
        sizePolicy3.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(sizePolicy3)
        self.label_23.setMinimumSize(QSize(350, 50))
        self.label_23.setMaximumSize(QSize(350, 50))
        self.label_23.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #151f28;\n"
"border: 5px solid black;\n"
"border-color: white;\n"
"color:white;\n"
"")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_pico_dia_2)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)
        self.label_24.setMinimumSize(QSize(170, 50))
        self.label_24.setMaximumSize(QSize(170, 50))
        self.label_24.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #151f28;\n"
"border: 5px solid black;\n"
"border-color: white;\n"
"color:white;\n"
"")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_24)


        self.verticalLayout_24.addWidget(self.frame_pico_dia_2, 0, Qt.AlignHCenter)


        self.horizontalLayout_9.addWidget(self.frame_23, 0, Qt.AlignHCenter)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)

        self.verticalLayout_8.addWidget(self.frame_19)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(2, 1)

        self.gridLayout_6.addWidget(self.frame_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_cuatro)
        self.page_cinco = QWidget()
        self.page_cinco.setObjectName(u"page_cinco")
        self.gridLayout_7 = QGridLayout(self.page_cinco)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.page_cinco)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setStyleSheet(u"background-color: rgb(113, 91, 255);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_7)
        self.label_7.setObjectName(u"label_7")
        sizePolicy1.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy1)
        self.label_7.setMinimumSize(QSize(0, 50))
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_7)

        self.frame_canvas4 = QFrame(self.frame_7)
        self.frame_canvas4.setObjectName(u"frame_canvas4")
        sizePolicy3.setHeightForWidth(self.frame_canvas4.sizePolicy().hasHeightForWidth())
        self.frame_canvas4.setSizePolicy(sizePolicy3)
        self.frame_canvas4.setMinimumSize(QSize(0, 0))
        self.frame_canvas4.setMaximumSize(QSize(16777215, 16777215))
        self.frame_canvas4.setStyleSheet(u"background-color: #FFEF65;")
        self.frame_canvas4.setFrameShape(QFrame.StyledPanel)
        self.frame_canvas4.setFrameShadow(QFrame.Raised)

        self.verticalLayout_10.addWidget(self.frame_canvas4)

        self.frame_16 = QFrame(self.frame_7)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy3.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy3)
        self.frame_16.setMinimumSize(QSize(0, 270))
        self.frame_16.setMaximumSize(QSize(16777215, 270))
        self.frame_16.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_15.setSpacing(9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 9, 9, 9)
        self.frame_26 = QFrame(self.frame_16)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy3.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy3)
        self.frame_26.setStyleSheet(u"")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_26)
        self.verticalLayout_22.setSpacing(6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(9, 9, 9, 9)
        self.label_36 = QLabel(self.frame_26)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font: 22000 6pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_22.addWidget(self.label_36)

        self.calendarioanual = QCalendarWidget(self.frame_26)
        self.calendarioanual.setObjectName(u"calendarioanual")
        sizePolicy3.setHeightForWidth(self.calendarioanual.sizePolicy().hasHeightForWidth())
        self.calendarioanual.setSizePolicy(sizePolicy3)
        self.calendarioanual.setMaximumSize(QSize(320, 200))
        self.calendarioanual.setStyleSheet(u"QCalendarWidget QWidget {\n"
"	 alternate-background-color: #ffffff;\n"
"}\n"
"\n"
"/* style for top navigation area ###############################################*/ \n"
"\n"
"#qt_calendar_navigationbar {\n"
"    background-color: #151f28;\n"
"	border: 2px solid  #ffef65;\n"
"	border-bottom: 0px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* style for month change buttons ############################################ */\n"
"\n"
"\n"
"\n"
"\n"
"/* Style for month and yeat buttons #################################### */\n"
"\n"
"#qt_calendar_yearbutton {\n"
"    color: #000000;\n"
"	margin:5px;\n"
"    border-radius: 5px;\n"
"	background-color: #e0e0e0;\n"
"	font-size: 13px;\n"
"	padding:0px 10px;\n"
"}\n"
"\n"
" #qt_calendar_monthbutton {\n"
"	width: 110px;\n"
"    color: #000000;\n"
"	font-size: 13px;\n"
"	margin:5px 0px;\n"
"    border-radius: 5px;\n"
"	background-color: #e0e0e0;\n"
"	padding:0px 2px;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:hover, \n"
"#qt_calendar_mont"
                        "hbutton:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#qt_calendar_yearbutton:pressed, \n"
"#qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/* Style for year input lineEdit ######################################*/\n"
"\n"
"#qt_calendar_yearedit {\n"
"    min-width: 53px;\n"
"    color: #fef128;\n"
"    background: transparent;\n"
"	font-size: 13px;\n"
"}\n"
"#qt_calendar_prevmonth, \n"
"#qt_calendar_nextmonth {\n"
"	/* border delete */\n"
"    border: none;  \n"
"  \n"
"	/* set background transparent */\n"
"    background-color: transparent; \n"
"	padding: 5px;\n"
"}\n"
"/* Style for year change buttons ######################################*/\n"
"\n"
"#qt_calendar_yearedit::up-button { \n"
"	image: url(:/icon/arrow-151-48.ico);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button { \n"
"	image: url(:/icon/arrow-213-48.ico);\n"
"    subcontrol-position: left; \n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button, \n"
""
                        "#qt_calendar_yearedit::up-button {\n"
"	width:10px;\n"
"	padding: 0px 5px;\n"
"	border-radius:3px;\n"
"}\n"
"\n"
"#qt_calendar_yearedit::down-button:hover, \n"
"#qt_calendar_yearedit::up-button:hover {\n"
"	background-color: #fef128;\n"
"}\n"
"\n"
"/* Style for month select menu ##################################### */\n"
"\n"
"#calendarWidget QToolButton QMenu {\n"
"     background-color: white;\n"
"\n"
"}\n"
"#calendarWidget QToolButton QMenu::item {\n"
"	/*padding: 10px;*/\n"
"}\n"
" #calendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"#calendarWidget QToolButton::menu-indicator {\n"
"	/* Remove toolButton arrow */\n"
"      /*image: none; */\n"
"	nosubcontrol-origin: margin;\n"
"	subcontrol-position: right center;\n"
"	margin-top: 10px;\n"
"	width:20px;\n"
"}\n"
"\n"
"/* Style for calendar table ########################################## */\n"
"#qt_calendar_calendarview {\n"
"	/* Remove the selected dashed box */\n"
"    outline: 0px;\n"
"	color: #000"
                        "000;\n"
"	border: 2px solid  #fef128;\n"
"	background-color: #e0e0e0;\n"
"	border-top: 0px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius: 5px;\n"
"	\n"
"	font: 733335 8pt \"Ubuntu Mono\";\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:hover {\n"
"   border-radius:5px;\n"
"	background-color:#aaffff;\n"
"}\n"
"\n"
"#qt_calendar_calendarview::item:selected {\n"
"    background-color: #55aa7f; \n"
"	border-radius:5px;\n"
"}")

        self.verticalLayout_22.addWidget(self.calendarioanual)


        self.horizontalLayout_15.addWidget(self.frame_26, 0, Qt.AlignHCenter)

        self.frame_27 = QFrame(self.frame_16)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy3.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy3)
        self.frame_27.setMinimumSize(QSize(600, 0))
        self.frame_27.setMaximumSize(QSize(600, 16777215))
        self.frame_27.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_27)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_39 = QLabel(self.frame_27)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setMinimumSize(QSize(300, 50))
        self.label_39.setMaximumSize(QSize(300, 50))
        self.label_39.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_19.addWidget(self.label_39, 0, Qt.AlignHCenter)

        self.frame_pico_dia_4 = QFrame(self.frame_27)
        self.frame_pico_dia_4.setObjectName(u"frame_pico_dia_4")
        sizePolicy3.setHeightForWidth(self.frame_pico_dia_4.sizePolicy().hasHeightForWidth())
        self.frame_pico_dia_4.setSizePolicy(sizePolicy3)
        self.frame_pico_dia_4.setMinimumSize(QSize(580, 70))
        self.frame_pico_dia_4.setMaximumSize(QSize(580, 70))
        self.frame_pico_dia_4.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_pico_dia_4.setFrameShape(QFrame.StyledPanel)
        self.frame_pico_dia_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_pico_dia_4)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(28, 0, 28, 0)
        self.label_40 = QLabel(self.frame_pico_dia_4)
        self.label_40.setObjectName(u"label_40")
        sizePolicy3.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy3)
        self.label_40.setMinimumSize(QSize(350, 50))
        self.label_40.setMaximumSize(QSize(350, 50))
        self.label_40.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #151f28;\n"
"border: 5px solid black;\n"
"border-color: white;\n"
"color:white;\n"
"")
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_40)

        self.label_41 = QLabel(self.frame_pico_dia_4)
        self.label_41.setObjectName(u"label_41")
        sizePolicy3.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy3)
        self.label_41.setMinimumSize(QSize(170, 50))
        self.label_41.setMaximumSize(QSize(170, 50))
        self.label_41.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #151f28;\n"
"border: 5px solid black;\n"
"border-color: white;\n"
"color:white;\n"
"")
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_41)


        self.verticalLayout_19.addWidget(self.frame_pico_dia_4, 0, Qt.AlignHCenter)


        self.horizontalLayout_15.addWidget(self.frame_27, 0, Qt.AlignHCenter)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)

        self.verticalLayout_10.addWidget(self.frame_16)


        self.gridLayout_7.addWidget(self.frame_7, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_cinco)
        self.page_seis = QWidget()
        self.page_seis.setObjectName(u"page_seis")
        self.verticalLayout_11 = QVBoxLayout(self.page_seis)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.page_seis)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 40))
        self.label_18.setMaximumSize(QSize(16777215, 40))
        self.label_18.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_12.addWidget(self.label_18)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy2.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy2)
        self.frame_9.setMinimumSize(QSize(0, 0))
        self.frame_9.setMaximumSize(QSize(16777215, 16777215))
        self.frame_9.setStyleSheet(u"background-color:#000000;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.VBL = QVBoxLayout()
        self.VBL.setObjectName(u"VBL")
        self.FeedLabel = QLabel(self.frame_9)
        self.FeedLabel.setObjectName(u"FeedLabel")
        sizePolicy1.setHeightForWidth(self.FeedLabel.sizePolicy().hasHeightForWidth())
        self.FeedLabel.setSizePolicy(sizePolicy1)
        self.FeedLabel.setStyleSheet(u"")

        self.VBL.addWidget(self.FeedLabel)


        self.verticalLayout_13.addLayout(self.VBL)


        self.verticalLayout_12.addWidget(self.frame_9, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy1.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy1)
        self.frame_12.setStyleSheet(u"background-color: #90CAF9;")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_12)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_22 = QLabel(self.frame_12)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_15.addWidget(self.label_22)

        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #ffef65;\n"
"color: BLACK;\n"
"border-radius: 5px; ")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_10)

        self.label_25 = QLabel(self.frame_12)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"border-radius: 5px; ")

        self.verticalLayout_15.addWidget(self.label_25)

        self.QLinferencia = QLabel(self.frame_12)
        self.QLinferencia.setObjectName(u"QLinferencia")
        self.QLinferencia.setStyleSheet(u"font: 22000 26pt \"Ubuntu Mono\";\n"
"background-color: #ffef65;\n"
"color: BLACK;\n"
"border-radius: 5px; ")

        self.verticalLayout_15.addWidget(self.QLinferencia)

        self.verticalLayout_15.setStretch(1, 1)

        self.verticalLayout_14.addWidget(self.frame_12)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.verticalLayout_12.setStretch(1, 5)
        self.verticalLayout_12.setStretch(2, 3)

        self.verticalLayout_11.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.page_seis)
        self.widget = QWidget()
        self.widget.setObjectName(u"widget")
        self.stackedWidget.addWidget(self.widget)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_contenedor)

        self.frame_elim_ref = QFrame(self.frame_inf)
        self.frame_elim_ref.setObjectName(u"frame_elim_ref")
        self.frame_elim_ref.setMinimumSize(QSize(0, 0))
        self.frame_elim_ref.setMaximumSize(QSize(0, 16777215))
        self.frame_elim_ref.setFrameShape(QFrame.StyledPanel)
        self.frame_elim_ref.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_elim_ref)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame9999 = QFrame(self.frame_elim_ref)
        self.frame9999.setObjectName(u"frame9999")
        sizePolicy.setHeightForWidth(self.frame9999.sizePolicy().hasHeightForWidth())
        self.frame9999.setSizePolicy(sizePolicy)
        self.frame9999.setMinimumSize(QSize(230, 0))
        self.frame9999.setMaximumSize(QSize(0, 16777215))
        self.frame9999.setStyleSheet(u"QFrame{\n"
"background-color:#e0e0e0;\n"
"}\n"
"QLineEdit{\n"
"border-radius: 10%;\n"
"background-color:#151f28;\n"
"\n"
"}\n"
"")
        self.frame9999.setFrameShape(QFrame.StyledPanel)
        self.frame9999.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame9999)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(17)
        self.gridLayout_4.setContentsMargins(0, 8, 0, 10)
        self.btn_eliminar = QPushButton(self.frame9999)
        self.btn_eliminar.setObjectName(u"btn_eliminar")
        self.btn_eliminar.setMinimumSize(QSize(180, 35))
        self.btn_eliminar.setMaximumSize(QSize(180, 35))
        self.btn_eliminar.setStyleSheet(u"QPushButton{\n"
"font:520 14pt \"Ubuntu Mono\";\n"
"background-color: #ffef65;\n"
"color: black;\n"
"border-radius: 10%;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"ICONOS/ICONO_BORRAR_REF.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_eliminar.setIcon(icon7)
        self.btn_eliminar.setIconSize(QSize(20, 20))

        self.gridLayout_4.addWidget(self.btn_eliminar, 5, 0, 1, 1)

        self.label_21 = QLabel(self.frame9999)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(180, 35))
        self.label_21.setMaximumSize(QSize(180, 35))
        self.label_21.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";")

        self.gridLayout_4.addWidget(self.label_21, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.cb_el_code_sus = QComboBox(self.frame9999)
        self.cb_el_code_sus.setObjectName(u"cb_el_code_sus")
        sizePolicy1.setHeightForWidth(self.cb_el_code_sus.sizePolicy().hasHeightForWidth())
        self.cb_el_code_sus.setSizePolicy(sizePolicy1)
        self.cb_el_code_sus.setMinimumSize(QSize(180, 35))
        self.cb_el_code_sus.setMaximumSize(QSize(180, 35))
        self.cb_el_code_sus.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";\n"
"\n"
"background-color: #ffffff;")

        self.gridLayout_4.addWidget(self.cb_el_code_sus, 3, 0, 1, 1)

        self.icono_new_ref_2 = QPushButton(self.frame9999)
        self.icono_new_ref_2.setObjectName(u"icono_new_ref_2")
        self.icono_new_ref_2.setMinimumSize(QSize(0, 0))
        self.icono_new_ref_2.setMaximumSize(QSize(16777215, 16777215))
        self.icono_new_ref_2.setStyleSheet(u"QPushButton{\n"
"background-color: #e0e0e0;\n"
"border-radius:0px;\n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"ICONOS/ICONO_BORRADOR.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icono_new_ref_2.setIcon(icon8)
        self.icono_new_ref_2.setIconSize(QSize(80, 80))

        self.gridLayout_4.addWidget(self.icono_new_ref_2, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.frame9999, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_elim_ref)

        self.frame_newref = QFrame(self.frame_inf)
        self.frame_newref.setObjectName(u"frame_newref")
        sizePolicy.setHeightForWidth(self.frame_newref.sizePolicy().hasHeightForWidth())
        self.frame_newref.setSizePolicy(sizePolicy)
        self.frame_newref.setMinimumSize(QSize(0, 0))
        self.frame_newref.setMaximumSize(QSize(0, 16777215))
        self.frame_newref.setStyleSheet(u"QFrame{\n"
"background-color:#e0e0e0;\n"
"}\n"
"QLineEdit{\n"
"border-radius: 10%;\n"
"background-color:#151f28;\n"
"\n"
"}\n"
"")
        self.frame_newref.setFrameShape(QFrame.StyledPanel)
        self.frame_newref.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_newref)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(17)
        self.gridLayout_3.setContentsMargins(0, 10, 0, 10)
        self.label_15 = QLabel(self.frame_newref)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(180, 35))
        self.label_15.setMaximumSize(QSize(180, 35))
        self.label_15.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";")

        self.gridLayout_3.addWidget(self.label_15, 6, 0, 1, 1)

        self.cb_uso = QComboBox(self.frame_newref)
        self.cb_uso.addItem("")
        self.cb_uso.addItem("")
        self.cb_uso.setObjectName(u"cb_uso")
        sizePolicy1.setHeightForWidth(self.cb_uso.sizePolicy().hasHeightForWidth())
        self.cb_uso.setSizePolicy(sizePolicy1)
        self.cb_uso.setMinimumSize(QSize(180, 35))
        self.cb_uso.setMaximumSize(QSize(180, 35))
        self.cb_uso.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";\n"
"\n"
"background-color: #ffffff;")

        self.gridLayout_3.addWidget(self.cb_uso, 5, 0, 1, 1)

        self.icono_new_ref = QPushButton(self.frame_newref)
        self.icono_new_ref.setObjectName(u"icono_new_ref")
        self.icono_new_ref.setMinimumSize(QSize(0, 0))
        self.icono_new_ref.setMaximumSize(QSize(16777215, 16777215))
        self.icono_new_ref.setStyleSheet(u"QPushButton{\n"
"background-color: #e0e0e0;\n"
"border-radius:0px;\n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"ICONOS/NEW_REF.png", QSize(), QIcon.Normal, QIcon.Off)
        self.icono_new_ref.setIcon(icon9)
        self.icono_new_ref.setIconSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.icono_new_ref, 1, 0, 1, 1)

        self.codigo_suscriptor = QLineEdit(self.frame_newref)
        self.codigo_suscriptor.setObjectName(u"codigo_suscriptor")
        sizePolicy1.setHeightForWidth(self.codigo_suscriptor.sizePolicy().hasHeightForWidth())
        self.codigo_suscriptor.setSizePolicy(sizePolicy1)
        self.codigo_suscriptor.setMinimumSize(QSize(180, 35))
        self.codigo_suscriptor.setMaximumSize(QSize(180, 35))
        font1 = QFont()
        font1.setFamily(u"Ubuntu Mono")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(62)
        self.codigo_suscriptor.setFont(font1)
        self.codigo_suscriptor.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";\n"
"color: #a6a6a6;")
        self.codigo_suscriptor.setMaxLength(32768)
        self.codigo_suscriptor.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.codigo_suscriptor, 3, 0, 1, 1)

        self.label_17 = QLabel(self.frame_newref)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMinimumSize(QSize(180, 35))
        self.label_17.setMaximumSize(QSize(180, 35))
        self.label_17.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";")

        self.gridLayout_3.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_16 = QLabel(self.frame_newref)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(180, 35))
        self.label_16.setMaximumSize(QSize(180, 35))
        self.label_16.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";")

        self.gridLayout_3.addWidget(self.label_16, 8, 0, 1, 1)

        self.cb_municipio = QComboBox(self.frame_newref)
        self.cb_municipio.addItem("")
        self.cb_municipio.addItem("")
        self.cb_municipio.addItem("")
        self.cb_municipio.setObjectName(u"cb_municipio")
        self.cb_municipio.setMinimumSize(QSize(180, 35))
        self.cb_municipio.setMaximumSize(QSize(180, 35))
        self.cb_municipio.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";\n"
"\n"
"background-color: #ffffff;")

        self.gridLayout_3.addWidget(self.cb_municipio, 9, 0, 1, 1)

        self.label_9 = QLabel(self.frame_newref)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(180, 35))
        self.label_9.setMaximumSize(QSize(180, 35))
        self.label_9.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";")

        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)

        self.anadir = QPushButton(self.frame_newref)
        self.anadir.setObjectName(u"anadir")
        self.anadir.setMinimumSize(QSize(180, 35))
        self.anadir.setMaximumSize(QSize(180, 35))
        self.anadir.setStyleSheet(u"QPushButton{\n"
"font:520 14pt \"Ubuntu Mono\";\n"
"background-color: #ffef65;\n"
"color: black;\n"
"border-radius: 10%;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u"ICONOS/A\u00d1ADIR_ARCHIVO_LOGO.png", QSize(), QIcon.Normal, QIcon.Off)
        self.anadir.setIcon(icon10)
        self.anadir.setIconSize(QSize(20, 20))

        self.gridLayout_3.addWidget(self.anadir, 11, 0, 1, 1)

        self.cb_categoria = QComboBox(self.frame_newref)
        self.cb_categoria.addItem("")
        self.cb_categoria.addItem("")
        self.cb_categoria.addItem("")
        self.cb_categoria.addItem("")
        self.cb_categoria.addItem("")
        self.cb_categoria.addItem("")
        self.cb_categoria.setObjectName(u"cb_categoria")
        self.cb_categoria.setMinimumSize(QSize(180, 35))
        self.cb_categoria.setMaximumSize(QSize(180, 35))
        self.cb_categoria.setStyleSheet(u"font: 500 14pt \"Ubuntu Mono\";\n"
"\n"
"background-color: #ffffff;")

        self.gridLayout_3.addWidget(self.cb_categoria, 7, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 10, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_newref, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_inf)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bt_menu.setText("")
        self.bt_atras.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">WATER METER</span></p></body></html>", None))
        self.bt_logosup.setText("")
        self.consumo_total_m.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">    Consumo total del mes    </p></body></html>", None))
        self.consumo_m_numero.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">12</p></body></html>", None))
        self.alerta_consumo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">111</p></body></html>", None))
        self.precio_consumo_total.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" color:#00ff00;\">Precio</span></p></body></html>", None))
        self.pushButton_2.setText("")
        self.btn_p1.setText(QCoreApplication.translate("MainWindow", u"Inicio", None))
        self.btn_p2.setText(QCoreApplication.translate("MainWindow", u"Ref Contadores", None))
        self.btn_p3.setText(QCoreApplication.translate("MainWindow", u"Medici\u00f3n Diaria", None))
        self.btn_p4.setText(QCoreApplication.translate("MainWindow", u"Medici\u00f3n Semanal", None))
        self.btn_p5.setText(QCoreApplication.translate("MainWindow", u"Medici\u00f3n Mensual", None))
        self.btn_p6.setText(QCoreApplication.translate("MainWindow", u"Medici\u00f3n Anual", None))
        self.btn_p7.setText(QCoreApplication.translate("MainWindow", u"Visualizaci\u00f3n", None))
        self.logo_uis.setText("")
        self.LOGO.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">DISE\u00d1O DE UN SISTEMA DIGITAL PARA LA LECTURA </p><p align=\"center\">DE CONTADORES DE AGUA POR MEDIO DE C\u00c1MARAS E IA</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Autores: Julio Andr\u00e9s Sanchez Abello </p><p align=\"center\">&amp; </p><p align=\"center\">Katherine Paola Parra Tarazona</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"UIS 2023", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Todos los derechos reservados", None))
        self.bt_newref.setText(QCoreApplication.translate("MainWindow", u"Nueva Referencia ", None))
        self.bt_x.setText(QCoreApplication.translate("MainWindow", u"Nueva Referencia ", None))
        self.btn_menu_elim_ref.setText(QCoreApplication.translate("MainWindow", u"Eliminar Datos", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"CONSUMO MENSUAL", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">SELECCIONA UN MES</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NOTIFICACIONES</p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Consumo mensual</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">V_MES</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"CONSUMO DEL D\u00cdA", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">SELECCIONA EL D\u00cdA</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NOTIFICACIONES</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Consumo diario</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">V_DIA</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"CONSUMO SEMANAL", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">SELECCIONA SEMANA</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NOTIFICACIONES</p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Consumo semanal</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">V_SEMANA</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CONSUMO DEL A\u00d1O", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">SELECCIONA EL A\u00d1O</span></p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NOTIFICACIONES</p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Consumo anual</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:600;\">V_A\u00d1O</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">VISUALIZACI\u00d3N DE \u00daLTIMA INFERENCIA</p></body></html>", None))
        self.FeedLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">TextLabel</p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">FECHA DE CAPTURA</p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tiempo de tomado de fotos", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">INFERENCIA</p></body></html>", None))
        self.QLinferencia.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">NO INFERENCIA, SE MUESTRA ANTERIOR IM\u00c1GEN INFERIDA</p></body></html>", None))
        self.btn_eliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">CODIGO SUSCRIPTOR</p></body></html>", None))
        self.icono_new_ref_2.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">CATEGOR\u00cdA</p></body></html>", None))
        self.cb_uso.setItemText(0, QCoreApplication.translate("MainWindow", u"RESIDENCIAL", None))
        self.cb_uso.setItemText(1, QCoreApplication.translate("MainWindow", u"RURAL", None))

        self.icono_new_ref.setText("")
        self.codigo_suscriptor.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">CODIGO SUSCRIPTOR</p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">MUNICIPIO</p></body></html>", None))
        self.cb_municipio.setItemText(0, QCoreApplication.translate("MainWindow", u"BUCARAMANGA", None))
        self.cb_municipio.setItemText(1, QCoreApplication.translate("MainWindow", u"FLORIDABLANCA", None))
        self.cb_municipio.setItemText(2, QCoreApplication.translate("MainWindow", u"GIR\u00d3N", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">USO</p></body></html>", None))
        self.anadir.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir", None))
        self.cb_categoria.setItemText(0, QCoreApplication.translate("MainWindow", u"ESTRATO 1", None))
        self.cb_categoria.setItemText(1, QCoreApplication.translate("MainWindow", u"ESTRATO 2", None))
        self.cb_categoria.setItemText(2, QCoreApplication.translate("MainWindow", u"ESTRATO 3", None))
        self.cb_categoria.setItemText(3, QCoreApplication.translate("MainWindow", u"ESTRATO 4", None))
        self.cb_categoria.setItemText(4, QCoreApplication.translate("MainWindow", u"ESTRATO 5", None))
        self.cb_categoria.setItemText(5, QCoreApplication.translate("MainWindow", u"ESTRATO 6", None))

    # retranslateUi

