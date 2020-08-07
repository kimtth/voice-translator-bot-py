# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'botBot.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(275, 586)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(275, 586))
        icon = QIcon()
        icon.addFile(u"translator-ico.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 281, 521))
        self.tabWidget.setMaximumSize(QSize(281, 521))
        self.EnJaTab = QWidget()
        self.EnJaTab.setObjectName(u"EnJaTab")
        self.enTextEdit = QPlainTextEdit(self.EnJaTab)
        self.enTextEdit.setObjectName(u"enTextEdit")
        self.enTextEdit.setGeometry(QRect(0, 0, 271, 241))
        self.enTextEdit.setAutoFillBackground(False)
        self.jaTextEdit = QPlainTextEdit(self.EnJaTab)
        self.jaTextEdit.setObjectName(u"jaTextEdit")
        self.jaTextEdit.setGeometry(QRect(0, 250, 271, 241))
        self.tabWidget.addTab(self.EnJaTab, "")
        self.JaEnTab = QWidget()
        self.JaEnTab.setObjectName(u"JaEnTab")
        self.enTextEdit_2 = QPlainTextEdit(self.JaEnTab)
        self.enTextEdit_2.setObjectName(u"enTextEdit_2")
        self.enTextEdit_2.setGeometry(QRect(0, 250, 271, 241))
        self.jaTextEdit_2 = QPlainTextEdit(self.JaEnTab)
        self.jaTextEdit_2.setObjectName(u"jaTextEdit_2")
        self.jaTextEdit_2.setGeometry(QRect(0, 0, 271, 241))
        self.tabWidget.addTab(self.JaEnTab, "")
        self.recordButton = QPushButton(self.centralwidget)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setGeometry(QRect(200, 520, 75, 23))
        icon1 = QIcon()
        icon1.addFile(u"mic_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.recordButton.setIcon(icon1)
        self.fontUpButton = QPushButton(self.centralwidget)
        self.fontUpButton.setObjectName(u"fontUpButton")
        self.fontUpButton.setGeometry(QRect(0, 520, 21, 23))
        self.fontDownButton = QPushButton(self.centralwidget)
        self.fontDownButton.setObjectName(u"fontDownButton")
        self.fontDownButton.setGeometry(QRect(20, 520, 21, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 275, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Voice Translator", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EnJaTab), QCoreApplication.translate("MainWindow", u"English \u2192 \u65e5\u672c\u8a9e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.JaEnTab), QCoreApplication.translate("MainWindow", u"\u65e5\u672c\u8a9e \u2192 English", None))
        self.recordButton.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.fontUpButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.fontDownButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

