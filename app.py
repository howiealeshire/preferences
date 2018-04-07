import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox
from dialog import Ui_Dialog
from PyQt5.QtCore import pyqtSlot


class Dialog(QDialog):
    def __init__(self):
        super(Dialog,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.buttons = self.ui.buttonBox.buttons()
        self.apply_button = self.buttons[2]
        self.cancel_button = self.buttons[1]
        self.ok_button = self.buttons[0]
        
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        self.apply_button.clicked.connect(self.apply_changes)
        

        
    @pyqtSlot()
    def apply_changes(self):
        self.get_category()
        
   
    def get_all_options(self):
        pass
    
    def get_time_available(self):
        pass
    def get_time_from(self):
        pass
    def get_time_to(self):
        pass
    
    def get_category(self):
        category = self.ui.category_grpbox.findChild(QComboBox,"category_comb")
        category_text = str(category.currentText())
        print(category_text)

    def get_location(self):
        pass
    
    def get_days(self):
        pass

def main():
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
