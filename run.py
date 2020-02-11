import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QGroupBox, QGridLayout, QCheckBox
from test_ui import Ui_MainWindow, Ui_Dialog
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
        #self.bt_read_columns.clicked.connect(self.btn_read_columns)
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

    #读取DF中的列明并显示在文本框中
    def btn_read_columns(self):
        columns = self.list_
        column = "\n".join(str(i) for i in columns)
        print(column)
        self.columns_display.setText(column)

    #程序运行按钮，根绝关键词文本框，在特定列中查找，若含有这些关键词，则在该单元格文本后添加"+注意"，最后保存在当前目录下
    def run_(self):
        self.columns_get = self.columns.toPlainText()
        column_get = self.columns_get.split(',')
        if self.columns_get == '':
            column_get = ['从何地返苏？（一直在苏填“无”）', '有无重点地区关联史（含往返、途经、接触）？', '籍贯']
            print(column_get)
        for i in range(len(self.df)):
            for k in range(len(column_get)):
                for j in range(len(self.keywords_get)):
                    if (self.keywords_get[j] in self.df[column_get[k]][i]):
                        self.df[column_get[k]][i] = self.df[column_get[k]][i] + '+注意'
        filename_out = 'processed.xlsx'
        self.df.to_excel(filename_out, index=False)
        if os.path.isfile(filename_out):
            QMessageBox.information(self, "结果", "处理成功",
                                    QMessageBox.Yes)
        else:
            QMessageBox.information(self, "结果", "处理失败",
                                    QMessageBox.yes)

#添加对话框，实现对读取DF的列进行动态选择
class mydialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()

        self.columns = ['q','q','w','q']
        self.setupUi(self)

    def initUI(self):
        len_list = len(self.columns)
        position_list = [[i, j] for i in range(int(len_list)/4 +1) for j in range(4)]
        pGroupBox = QGroupBox(u"游戏选择")
        pGrid = QGridLayout()
        print("dir(pGrid) %s" % dir(pGrid))
        pGrid.setSpacing(10)

        for position_list, columns in zip(position_list, self.columns):
            print("sGame %s" % columns)
            pCheck = QCheckBox(columns)
            pGrid.addWidget(pCheck, position_list[0], columns[1])
            pCheck.stateChanged.connect(lambda: self.__onCheck(columns))

        pGroupBox.setLayout(pGrid)
        self.setLayout(pGrid)

    def __onCheck(self, value):
        print("onCheck:value %s" % value)

    def __onGroup(self, value):
        print("onGroup:value %s" % value)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = mymainwindow()
    myDia = mydialog()
    myWin.show()
    myWin.bt_read_columns.clicked.connect(myDia.show)

    sys.exit(app.exec())
