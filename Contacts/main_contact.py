import sqlite3
from unittest import loader
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.conn=sqlite3.connect("main.db")
        self.my_cursor=self.conn.cursor()

        loader = QUiLoader()

        self.ui = loader.load("Contact.ui")
        self.ui.show()

        self.ui.Add_Butt.clicked.connect(self.add)
        self.ui.Delete_Butt.clicked.connect(self.delete)
        self.ui.DeleteAll_Butt.clicked.connect(self.delete_all)




        self.Load_Data()

    def Load_Data(self):
        self.my_cursor.execute("SELECT * FROM person")
        result = self.my_cursor.fetchall()
        
        
        
        for item in result:
            label = QLabel()
            try:
                label.setText(item[1] + " " + item[2] + " : " + item[4])
            except:
                label.setText(item[1] + " : " + item[4])
            self.ui.verticalLayout.addWidget(label)

        print("Load successfully")

    def add(self):
        self.name=




app=QApplication()
main_window = MainWindow()
app.exec()