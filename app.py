import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QTableWidget,QTableWidgetItem,QPushButton,QPlainTextEdit, QDialog, QComboBox, QCheckBox
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

        self.all_chk = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"all_days_chk")
        self.all_chk.clicked.connect(self.check_all_days)
    
        

        
    @pyqtSlot()
    def apply_changes(self):
        self.get_all_options()
        
   
    def get_all_options(self):
        self.get_location()
        self.get_category()
        self.get_professor()
        self.get_days()
        

    def get_time_available(self):
        pass
    def get_time_from(self):
        pass
    def get_time_to(self):
        pass
    
    def get_category(self):
       # category = self.ui.category_grpbox.findChild(QComboBox,"category_comb")
       # category_text = str(category.currentText())
        print(self.get_cwtext(self.ui.category_grpbox,QComboBox,"category_comb"))

    def get_location(self):
        print(self.get_cwtext(self.ui.location_grpbox,QComboBox,"location_comb"))
        
    
    def get_days(self):
        
        print(self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"all_days_chk"))
        print(self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"monday_chk"))
        print(self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"tues_chk"))
        print(self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"wed_chk"))
        print(self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"thurs_chk"))
        print(self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"fri_chk"))
    
    @pyqtSlot()
    def check_all_days(self):
        all_is_checked = self.get_checkbox_helper(self.ui.days_available_grpbox,QCheckBox,"all_days_chk")
        if all_is_checked:
            self.check_rest()
        
    def check_rest(self):
        monday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"monday_chk")
        tuesday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"tues_chk")
        wednesday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"wed_chk")
        thursday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"thurs_chk")
        friday = self.get_child_widget(self.ui.days_available_grpbox,QCheckBox,"fri_chk")
        
        monday.setChecked(True)
        tuesday.setChecked(True)
        wednesday.setChecked(True)
        thursday.setChecked(True)
        friday.setChecked(True)
        
        #immediately update gui to reflect changes
        #note: choice of monday is arbitrary
        monday.repaint()
        
            

    def get_child_widget(self,parent,child_widget_type,child_name):
        child = parent.findChild(child_widget_type,child_name)
        return child

        

    def get_checkbox_helper(self,parent,child_widget_type,child_name):
        child = parent.findChild(child_widget_type,child_name)
        child_is_checked = child.isChecked()
        return child_is_checked

    def get_professor(self):
        print(self.get_cwtext(self.ui.professor_grpbox,QComboBox,"professor_comb"))

    def get_cwtext(self,parent,child_widget_type,child_name):
        child = parent.findChild(child_widget_type,child_name)
        child_text = str(child.currentText())
        return child_text


def main():
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
