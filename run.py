import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from test_ui import Ui_MainWindow
import pandas as pd
import mark

class mymainwindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(mymainwindow,self).__init__(parent)
        self.setupUi(self)
        self.read_file.clicked.connect(self.readfile_)
        self.bt_openfile.clicked.connect(self.btn_clear)
        self.bt_openfile.clicked.connect(self.btn_file_open)
        self.bt_opendatabase.clicked.connect(self.btn_database_open)
        self.bt_readdatabase.clicked.connect(self.btn_database_read)
        self.bt_read_columns.clicked.connect(self.btn_read_columns)
        self.start.clicked.connect(self.run_)

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

    def btn_database_open(self):
        self.database_name, filetype = QFileDialog.getOpenFileName(self, 'open database', "./", "All Files (*);;Txt(*.txt)")
        self.keywords.setText(self.database_name)

    def btn_database_read(self):
        self.keywords_get = mark.readtxt(self.database_name)
        show_keywords = " ".join(str(i) for i in self.keywords_get)
        self.keywords_display.setText(show_keywords)

    def btn_read_columns(self):
        columns = self.list_
        column = "\n".join(str(i) for i in columns)
        print(column)
        self.columns_display.setText(column)

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








if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = mymainwindow()
    myWin.show()
    sys.exit(app.exec())
