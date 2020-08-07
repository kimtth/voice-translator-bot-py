# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'botBotZwZUtS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
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
        MainWindow.setFixedSize(275, 586)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(275, 586))
        icon = QIcon()
        # added by me
        abs_path = os.path.abspath("./design/translator-ico.png")
        icon.addFile(abs_path, QSize(), QIcon.Normal, QIcon.Off)
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
        # added by me
        abs_path = os.path.abspath("./design/mic_icon.png")
        icon1.addFile(abs_path, QSize(), QIcon.Normal, QIcon.Off)
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

class UI_Action:
    def __init__(self, qt_ui):
        self.qt = qt_ui
        self.font_size = 8
        self.current_tab_index = 0
        self.current_tab_widget = object
        self.test_data_tab_one()
        self.action_tab_change()

        self.action_record_button()
        self.action_font_up_button()
        self.action_font_down_button()
        self.action_menu_save()
        self.action_menu_exit()

    def test_data_tab_one(self):
        jp_file = open('./design/sample_jp.vot', 'r', encoding='utf-8')
        en_file = open('./design/sample_en.vot', 'r', encoding='utf-8')
        self.qt.enTextEdit.setPlainText(en_file.read())
        self.qt.jaTextEdit.setPlainText(jp_file.read())

    def test_data_tab_two(self):
        jp_file = open('./design/sample_jp.vot', 'r', encoding='utf-8')
        en_file = open('./design/sample_en.vot', 'r', encoding='utf-8')
        self.qt.enTextEdit_2.setPlainText(en_file.read())
        self.qt.jaTextEdit_2.setPlainText(jp_file.read())

    def action_tab_change(self):
        # self.qt.tabWidget.blockSignals(True)  # just for not showing the initial message
        self.qt.tabWidget.currentChanged.connect(lambda: self.tab_change())

    def action_font_up_button(self):
        self.qt.fontUpButton.clicked.connect(lambda: self.button_font_size_up())

    def action_font_down_button(self):
        self.qt.fontDownButton.clicked.connect(lambda: self.button_font_size_down())

    def action_record_button(self):
        self.qt.recordButton.clicked.connect(lambda: self.button_record())

    def action_menu_save(self):
        self.qt.actionSave.triggered.connect(lambda: self.menu_save())

    def action_menu_exit(self):
        self.qt.actionExit.triggered.connect(lambda: self.menu_exit())

    def tab_change(self):
        current_index = self.qt.tabWidget.currentIndex()
        current_widget = self.qt.tabWidget.currentWidget()
        self.current_tab_index = current_index
        self.current_tab_widget = current_widget

        if current_index == 0:
            self.test_data_tab_one()
        elif current_index == 1:
            self.test_data_tab_two()

        self.action_font_size_setter()

    def menu_exit(self):
        QCoreApplication.quit()

    def menu_save(self):
        QMessageBox.information(self.qt.centralwidget, "Information", "Being created...")

    def button_font_size_up(self):
        self.font_size += 2
        self.action_font_size_setter()

    def action_font_size_setter(self):
        if self.current_tab_index == 0:
            font = self.qt.enTextEdit.font()  # current font
            font.setPointSize(self.font_size)  # change it's size
            self.qt.enTextEdit.setFont(font)  # set font
            font = self.qt.jaTextEdit.font()
            font.setPointSize(self.font_size)
            self.qt.jaTextEdit.setFont(font)
        elif self.current_tab_index == 1:
            font = self.qt.enTextEdit_2.font()  # current font
            font.setPointSize(self.font_size)  # change it's size
            self.qt.enTextEdit_2.setFont(font)  # set font
            font = self.qt.jaTextEdit_2.font()
            font.setPointSize(self.font_size)
            self.qt.jaTextEdit_2.setFont(font)

    def button_font_size_down(self):
        self.font_size -= 2
        self.action_font_size_setter()

    def button_record(self):
        QMessageBox.information(self.qt.centralwidget, "Information", "Being created...")


if __name__ == "__main__":
    app = QApplication()
    MainWindow = QMainWindow()  # <-- Instantiate QMainWindow object.
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    action = UI_Action(ui)

    MainWindow.show()
    app.exec_()