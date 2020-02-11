import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from test_ui import Ui_MainWindow
import pandas as pd



class mymainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mymainwindow,self).__init__(parent)
        self.setupUi(self)
        self.display()
        self.read_file.clicked.connect(self.readfile_)
        self.bt_openfile.clicked.connect(self.btn_clear)
        self.bt_openfile.clicked.connect(self.btn_file_open)
        self.start.clicked.connect(self.run_)


    def display(self):
        self.keywords_display.setText('温州,台州,杭州,宁波,信阳,驻马店,合肥,阜阳,南昌')
        self.columns_display.setText('从何地返苏？（一直在苏填“无”）,有无重点地区关联史（含往返、途经、接触）？,籍贯')


    def readfile_(self):
        self.df = pd.read_excel(self.filename_get)
        self.list_ = self.df.columns.tolist()
        if len(self.list_)!=0:
            self.columns_name.setText('读取成功')

    def btn_clear(self):
        self.filename.clear()

    def btn_file_open(self):
        self.filename_get, filetype = QFileDialog.getOpenFileName(self, 'openfile',
                                                                  "./","ALL Files (*);;Excel(*.xlsx)")
        self.filename.setText(self.filename_get)


    def run_(self):
        self.keywords_get = self.keywords.toPlainText()
        self.columns_get = self.columns.toPlainText()
        keyword_get = self.keywords_get.split(',')
        column_get = self.columns_get.split(',')
        if self.keywords_get == "":
            keyword_get = ['温州', '台州', '杭州', '宁波', '信阳', '驻马店', '合肥', '阜阳', '南昌']
            print(keyword_get)
        if self.columns_get == '':
            column_get = ['从何地返苏？（一直在苏填“无”）', '有无重点地区关联史（含往返、途经、接触）？', '籍贯']
            print(column_get)
        for i in range(len(self.df)):
            for k in range(len(column_get)):
                for j in range(len(keyword_get)):
                    if (keyword_get[j] in self.df[column_get[k]][i]):
                        self.df[column_get[k]][i] = self.df[column_get[k]][i] + '+注意'
        print(self.filename_get)
        filename_out = 'processed.xlsx'
        self.df.to_excel(filename_out, index=False)








if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = mymainwindow()
    myWin.show()
    sys.exit(app.exec())
