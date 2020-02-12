import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog
from PyQt5 import QtWidgets, QtCore
from mainwindow import Ui_MainWindow
from dialog import Ui_Dialog
import pandas as pd
import mark
import os

class mymainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mymainwindow,self).__init__(parent)
        self.setupUi(self)
        self.read_file.clicked.connect(self.readfile_)
        self.bt_openfile.clicked.connect(self.btn_clear)
        self.bt_openfile.clicked.connect(self.btn_file_open)
        self.bt_opendatabase.clicked.connect(self.btn_database_open)
        self.bt_readdatabase.clicked.connect(self.btn_database_read)
        self.bt_read_columns.clicked.connect(self.btn_read_columns_)
        self.start.clicked.connect(self.run_)

    #根据输入的文件名读取excel作为df
    def readfile_(self):
        self.df = pd.read_excel(self.filename_get)
        self.list_ = self.df.columns.tolist()
        if len(self.list_)!=0:
            self.columns_name.setText('读取成功')

    #按钮使用前清空文本框
    def btn_clear(self):
        self.filename.clear()

    #选中excel文件，获取文件绝对路径，并显示在文本框中
    def btn_file_open(self):
        self.filename_get, filetype = QFileDialog.getOpenFileName(self, 'openfile',
                                                                  "./","ALL Files (*);;Excel(*.xlsx)")
        self.filename.setText(self.filename_get)

    #选中关键词文本文件，并显示路径在文本框中
    def btn_database_open(self):
        self.database_name, filetype = QFileDialog.getOpenFileName(self, 'open database', "./", "All Files (*);;Txt(*.txt)")
        self.keywords.setText(self.database_name)

    #读取关键词文本文件，并显示这些关键词在文本框中
    def btn_database_read(self):
        self.keywords_get = mark.readtxt(self.database_name)
        show_keywords = " ".join(str(i) for i in self.keywords_get)
        self.keywords_display.setText(show_keywords)

    #直接访问另一个类，实现字段的选择
    def btn_read_columns_(self):
        self.mywidget = mywidget(self.list_)
        self.mywidget.show()
        self.mywidget.mySignal.connect(self.dis_read_columns)

    #读取选中的字段并显示在文本框中
    def dis_read_columns(self, connect):
        self.columns_display.setText(connect)

    #程序运行按钮，根绝关键词文本框，在特定列中查找，若含有这些关键词，则在该单元格文本后添加"+注意"，最后保存在当前目录下
    def run_(self):
        addwords = self.addwords.toPlainText()
        column_get = self.mywidget.checklist
        for i in range(len(self.df)):
            for k in range(len(column_get)):
                for j in range(len(self.keywords_get)):
                    if (self.keywords_get[j] in self.df[column_get[k]][i]):
                        self.df[column_get[k]][i] = self.df[column_get[k]][i] + addwords
        filename_out = 'processed.xlsx'
        self.df.to_excel(filename_out, index=False)
        if os.path.isfile(filename_out):
            QMessageBox.information(self, "结果", "处理成功",
                                    QMessageBox.Yes)
        else:
            QMessageBox.information(self, "结果", "处理失败",
                                    QMessageBox.yes)

#添加对话框，实现对读取DF的列进行动态选择
class mywidget(QtWidgets.QWidget):
    mySignal = pyqtSignal(str)
    def __init__(self, column):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        columns = column
        id_ = range(len(columns))
        for id_, text in zip(id_, columns):
            checkBox = QtWidgets.QCheckBox(text, self)
            checkBox.id_ = id_
            checkBox.stateChanged.connect(self.checkcheck)
            layout.addWidget(checkBox)
        self.checklist = []
        self.bottom = QtWidgets.QPushButton('确定')
        layout.addWidget(self.bottom)

        self.bottom.clicked.connect(self.confirm)
        self.bottom.clicked.connect(self.close)
        self.setLayout(layout)


    def checkcheck(self, state):
        checkbox = self.sender()
        if state == QtCore.Qt.Checked:
            if checkbox.text() not in self.checklist:
                self.checklist.append(checkbox.text())
        if state == QtCore.Qt.Unchecked:
            if checkbox.text() in self.checklist:
                self.checklist.remove(checkbox.text())

    def confirm(self):
        if not self.checklist:
            QMessageBox.critical(self, "错误", "请选择字段")
        else:
            checkout = " ".join(str(i) for i in self.checklist)
            self.mySignal.emit(checkout)









if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = mymainwindow()
    myWin.show()

    sys.exit(app.exec())
