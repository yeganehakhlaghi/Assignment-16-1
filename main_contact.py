from cProfile import label
import sqlite3
from unittest import loader
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader
from numpy import delete
from numpy import delete
import qdarkstyle



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
        self.ui.Mod_Butt.clicked.connect(self.Dark)


        self.id=0

        self.Load_Data()

    def Load_Data(self):
        self.my_cursor.execute("SELECT * FROM person")
        result = self.my_cursor.fetchall()
        
        
        
        for item in result:
            label = QLabel()
            self.id+=1
            try:
                label.setText(item[1] + " " + item[2] + " : " + item[4])
            except:
                label.setText(item[1] + " : " + item[4])
            self.ui.verticalLayout.addWidget(label)

        print("Load successfully")

    def add(self):
        self.id+=1
        name=self.ui.Name_Line.text()
        last_name = self.ui.Family_Line.text()
        mobile_number = self.ui.Phon_Line.text()
        self.my_cursor.execute(f"INSERT INTO person(id,name,family,mobile_numbe) VALUES({self.id},'{name}','{last_name}','{mobile_number}')") 
        #PRIMARY KEY (id)""")
        self.ui.Name_Line.setText("")
        self.ui.Family_Line.setText("")
        self.ui.Phon_Line.setText("")

        #self.Load_Data()
        # self.my_cursor.execute("SELECT * FROM person")
        # result = self.my_cursor.fetchall()
        # for item in result:
        #     if item[1]==name:
        #         label = QLabel()
        #         try:
        #             label.setText(item[1] + " " + item[2] + " : " + item[4])
        #         except:
        #             label.setText(item[1] + " : " + item[4])
        #         self.ui.verticalLayout.addWidget(label)

        label= QLabel()
        label.setText(name + " " + last_name + " : " + mobile_number)
        self.ui.verticalLayout.addWidget(label)

        self.conn.commit()
        #self.conn.close()


    def delete(self):
        name=self.ui.DelName_Line.text()
        self.my_cursor.execute(f"DELETE FROM person WHERE name == '{name}'")
        self.conn.commit()
        #self.conn.close()
        self.ui.DelName_Line.setText("")

        #self.Load_Data()



    def delete_all(self):
        self.my_cursor.execute("DELETE FROM person")
        self.conn.commit()
        label= QLabel()
        label.setText("All your contacts have been deleted")
        self.ui.verticalLayout.addWidget(label)
        self.conn.close()
        

    def Dark(self):
        app.setStyleSheet(qdarkstyle.load_stylesheet())
        #pass


app=QApplication()
main_window = MainWindow()
app.exec()