import sys
from PyQt5 import QtWidgets
import untitled as design
class ExamleApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        self.Add.clicked.connect(self.click0)
        self.list = []
        self.listView = []
    def click0(self):
        if not self.text.toPlainText()=='' and not self.text2.toPlainText()=='':
            by = {'text':self.text.toPlainText(), 'date':self.text2.toPlainText()}
            self.list.append(by)
            self.listView.append(str(by))
            self.screen.clear()
            self.screen.insertItems(0,self.listView)
            self.text.setText('')
            self.text2.setText('')
    def __init__(self):
        self.add_items()
        self.itemClicked.connect(self.item_click)
                            


app=QtWidgets.QApplication(sys.argv)
window=ExamleApp()
window.show()
app.exec_()