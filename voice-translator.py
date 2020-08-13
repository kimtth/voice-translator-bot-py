# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'botBotZwZUtS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import os
import time

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, Slot)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from azure.cognitiveservices.speech import SpeechRecognizer

import api.speech_api as api
import sys
from api.speech_worker import SpeechContinuousWorker


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath("./design")

    return os.path.join(base_path, relative_path)


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
        abs_path = resource_path("translator-ico.png")
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
        # added by me --start
        self.recordContinualButton = QPushButton(self.centralwidget)
        self.recordContinualButton.setObjectName(u"recordButton")
        self.recordContinualButton.setGeometry(QRect(120, 520, 75, 23))
        abs_path = resource_path("mic_icon.png")
        self.recordButton.setCheckable(True)
        self.recordButton.setStyleSheet("QPushButton:checked {color: white; background-color: green;}")
        self.recordContinualButton.setCheckable(True)
        self.recordContinualButton.setStyleSheet("QPushButton:checked {color: white; background-color: green;}")
        icon1.addFile(abs_path, QSize(), QIcon.Normal, QIcon.Off)
        self.recordButton.setIcon(icon1)
        # added by me --end
        self.recordContinualButton.setIcon(icon1)
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EnJaTab),
                                  QCoreApplication.translate("MainWindow", u"English \u2192 \u65e5\u672c\u8a9e", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.JaEnTab),
                                  QCoreApplication.translate("MainWindow", u"\u65e5\u672c\u8a9e \u2192 English", None))
        self.recordButton.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.recordContinualButton.setText(QCoreApplication.translate("MainWindow", u"Non-Stop", None))
        self.fontUpButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.fontDownButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi


class UI_Action:
    def __init__(self, qt_ui):
        self.qt = qt_ui
        self.font_size = 8
        self.current_tab_index = 0
        # self.current_tab_widget = object
        self.speech_recognizer = object
        self.worker = SpeechContinuousWorker()
        self.payload = PlainTextPayLoad(qt_ui, self.worker)
        # self.test_data_tab_one()
        self.action__init__()

    def action__init__(self):
        self.action_tab_change()
        self.action_record_button()
        self.action_continual_record_button()
        self.action_font_up_button()
        self.action_font_down_button()
        self.action_menu_save()
        self.action_menu_exit()

    def action_tab_change(self):
        self.qt.tabWidget.currentChanged.connect(lambda: self.tab_switch_lang_mode())

    def action_font_up_button(self):
        self.qt.fontUpButton.clicked.connect(lambda: self.button_font_size_up())

    def action_font_down_button(self):
        self.qt.fontDownButton.clicked.connect(lambda: self.button_font_size_down())

    def action_continual_record_button(self):
        self.qt.recordContinualButton.clicked.connect(lambda: self.button_continual_record())

    def action_record_button(self):
        self.qt.recordButton.clicked.connect(lambda: self.button_record())

    def action_menu_save(self):
        self.qt.actionSave.triggered.connect(lambda: self.menu_save())

    def action_menu_exit(self):
        self.qt.actionExit.triggered.connect(lambda: self.menu_exit())

    def tab_switch_lang_mode(self):
        current_index = self.qt.tabWidget.currentIndex()
        # current_widget = self.qt.tabWidget.currentWidget()
        self.current_tab_index = current_index

        if self.qt.recordContinualButton.isChecked():
            self.set_record_continual_default_checked()
            QMessageBox.information(self.qt.centralwidget, "Information", "Recording was terminated.")
            # self.qt.recordContinualButton.click() # Trigger click programmatically

        self.action_font_size_setter()

    def menu_exit(self):
        QCoreApplication.quit()

    def menu_save(self):
        # QMessageBox.information(self.qt.centralwidget, "Information", "Being created...")
        tabData = {}
        textData_enJa = {}
        textData_enJa['en'] = self.qt.enTextEdit.toPlainText()
        textData_enJa['ja'] = self.qt.jaTextEdit.toPlainText()
        tabData['EnJaTab'] = textData_enJa

        textData_jaEn = {}
        textData_jaEn['en'] = self.qt.enTextEdit_2.toPlainText()
        textData_jaEn['ja'] = self.qt.jaTextEdit_2.toPlainText()
        tabData['JaEnTab'] = textData_jaEn

        self.action_save_file(tabData)

    def action_save_file(self, tab_data):
        file_name = QFileDialog.getSaveFileName(self.qt.centralwidget, caption='Save File', filter="Text (*.txt)",
                                                options=QFileDialog.DontUseNativeDialog)
        if file_name[0].endswith(".txt"):
            file_path = file_name[0]
        else:
            file_path = file_name[0] + ".txt"

        if file_path:
            with open(file_path, 'w', encoding='utf8') as f:
                print(tab_data, file=f)

    def button_font_size_up(self):
        self.font_size += 2
        self.action_font_size_setter()

    def button_font_size_down(self):
        if self.font_size > 3:
            self.font_size -= 2
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

    def button_record(self):
        if self.qt.recordButton.isChecked():
            self.call_speech_once_sdk()
        else:
            self.set_record_default_checked()

    def button_continual_record(self):
        if self.qt.recordContinualButton.isChecked():
            self.call_speech_continual_sdk()
        else:
            self.set_record_continual_default_checked()

    def set_record_continual_default_checked(self):
        self.qt.recordContinualButton.setChecked(False)
        if hasattr(self.speech_recognizer, 'stop_continuous_recognition'):
            self.speech_recognizer.stop_continuous_recognition()

    def set_record_default_checked(self):
        self.qt.recordButton.setChecked(False)

    def call_speech_once_sdk(self):
        if self.qt.recordButton.isChecked():
            text, lang = api.speech_recognize_once_with_auto_language_detection_from_mic \
                (speech_recognizer=self.worker.speech_recognize_generator_auto_detect(), ui_callback=self.set_record_default_checked)
            if text:
                self.action_set_plaintext(text, lang)

    def action_set_plaintext(self, text, lang):
        if str(lang).strip() == 'ja-JP':
            self.payload.set_tab_ja_en(text, lang)
        else:
            self.payload.set_tab_en_ja(text, lang)

    def call_speech_continual_sdk(self):
        if self.qt.recordContinualButton.isChecked():
            current_index = self.qt.tabWidget.currentIndex()
            if current_index == 0:
                if self.qt.recordContinualButton.isChecked():
                    print('>--english mode')
                    self.speech_recognizer = self.worker.speech_recognize_generator_english_detect()
                    self.worker.speech_recognize_continual_from_mic \
                        (speech_recognizer=self.speech_recognizer,
                         ui_callback=self.set_record_continual_default_checked)
            elif current_index == 1:
                if self.qt.recordContinualButton.isChecked():
                    print('>--japanese mode')
                    self.speech_recognizer = self.worker.speech_recognize_generator_japanese_detect()
                    self.worker.speech_recognize_continual_from_mic \
                        (speech_recognizer=self.speech_recognizer,
                         ui_callback=self.set_record_continual_default_checked)


class PlainTextPayLoad:
    def __init__(self, qt, worker):
        self.tabWidget = qt.tabWidget
        self.tab_enJa_en = qt.enTextEdit
        self.tab_enJa_ja = qt.jaTextEdit
        self.str_separator = ': '
        self.tab_jaEn_en = qt.enTextEdit_2
        self.tab_jaEn_ja = qt.jaTextEdit_2
        self.worker = worker
        self.worker.text_result_lang.connect(self.set_tab_result)

    # Signal Receiver - Slot
    @Slot(object)
    def set_tab_result(self, result):
        text = result['text']
        lang = result['lang']

        if lang == 'ja-JP':
            self.set_tab_ja_en(text, lang)
        else:
            self.set_tab_en_ja(text, lang)

    def set_tab_en_ja(self, result, lang):
        timestamp = time.strftime("%H:%M:%S")
        self.tabWidget.setCurrentIndex(0)

        if result:
            time.sleep(0.1)
            self.tab_enJa_en.appendPlainText(timestamp + self.str_separator + result)
            translate_result = api.translation_once_from_text(result, lang)
            time.sleep(0.1)
            self.tab_enJa_ja.appendPlainText(timestamp + self.str_separator + translate_result)

    def set_tab_ja_en(self, result, lang):
        timestamp = time.strftime("%H:%M:%S")
        self.tabWidget.setCurrentIndex(1)

        if result:
            time.sleep(0.1)
            self.tab_jaEn_ja.appendPlainText(timestamp + self.str_separator + result)
            translate_result = api.translation_once_from_text(result, lang)
            time.sleep(0.1)
            self.tab_jaEn_en.appendPlainText(timestamp + self.str_separator + translate_result)


if __name__ == "__main__":
    app = QApplication()
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    action = UI_Action(ui)

    MainWindow.show()
    app.exec_()
