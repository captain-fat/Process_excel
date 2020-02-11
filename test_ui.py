# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(649, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.filename = QtWidgets.QTextEdit(self.centralwidget)
        self.filename.setGeometry(QtCore.QRect(10, 40, 121, 51))
        self.filename.setObjectName("filename")
        self.keywords = QtWidgets.QTextEdit(self.centralwidget)
        self.keywords.setGeometry(QtCore.QRect(290, 30, 121, 61))
        self.keywords.setObjectName("keywords")
        self.columns = QtWidgets.QTextEdit(self.centralwidget)
        self.columns.setGeometry(QtCore.QRect(10, 240, 111, 51))
        self.columns.setObjectName("columns")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(540, 270, 91, 41))
        self.start.setObjectName("start")
        self.keywords_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.keywords_display.setGeometry(QtCore.QRect(440, 30, 171, 71))
        self.keywords_display.setObjectName("keywords_display")
        self.columns_display = QtWidgets.QTextBrowser(self.centralwidget)
        self.columns_display.setGeometry(QtCore.QRect(190, 230, 221, 81))
        self.columns_display.setObjectName("columns_display")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 20, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 10, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 31, 16))
        self.label_3.setObjectName("label_3")
        self.read_file = QtWidgets.QPushButton(self.centralwidget)
        self.read_file.setGeometry(QtCore.QRect(540, 207, 93, 41))
        self.read_file.setObjectName("read_file")
        self.columns_name = QtWidgets.QTextBrowser(self.centralwidget)
        self.columns_name.setGeometry(QtCore.QRect(10, 100, 121, 61))
        self.columns_name.setObjectName("columns_name")
        self.bt_openfile = QtWidgets.QPushButton(self.centralwidget)
        self.bt_openfile.setGeometry(QtCore.QRect(140, 40, 93, 61))
        self.bt_openfile.setObjectName("bt_openfile")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 649, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filename.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.keywords.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.columns.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'SimSun\';\"><br /></p></body></html>"))
        self.start.setText(_translate("MainWindow", "开始"))
        self.label.setText(_translate("MainWindow", "文件名"))
        self.label_2.setText(_translate("MainWindow", "关键词"))
        self.label_3.setText(_translate("MainWindow", "字段"))
        self.read_file.setText(_translate("MainWindow", "读取文件"))
        self.bt_openfile.setText(_translate("MainWindow", "打开"))
