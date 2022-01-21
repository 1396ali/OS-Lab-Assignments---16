from random import randint
import sqlite3
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader



class Contact(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load("design.ui")
        self.ui.show()

        self.con = sqlite3.connect("data.db")
        self.my_cursor = self.con.cursor()


        self.load()

        self.ui.btn_1.clicked.connect(self.insert)
        self.ui.btn_2.clicked.connect(self.refresh)
        self.ui.btn_3.clicked.connect(self.delete)
        self.ui.btn_4.clicked.connect(self.delete_all)
        self.ui.btn_5.clicked.connect(self.dark)
        self.ui.btn_6.clicked.connect(self.white)
        self.ui.btn_7.clicked.connect(self.clear)
        self.ui.btn_8.clicked.connect(self.exit_0)


    def load(self):
        self.my_cursor.execute("SELECT * FROM contacts")

        res = self.my_cursor.fetchall()

        for i in res:
            label = QLabel()
            label.setText(i[0]+"                    " + i[1]+'               |            '+i[2]+'            |           '+i[3]+'            |        '+i[4])
            self.ui.v_lay.addWidget(label)
            
        print('load ok')


    def refresh(self):
        for i in reversed(range(self.ui.v_lay.count())): 
            self.ui.v_lay.itemAt(i).widget().setParent(None)

        print('refresh ok')

        self.load()


    def insert(self):
        id = randint(1,999)
        name = self.ui.line_1.text()
        family = self.ui.line_2.text()
        number = self.ui.line_3.text()
        email = self.ui.line_4.text()
        
        self.my_cursor.execute(f"INSERT INTO contacts (id,name,family,number,email) VALUES({id},'{name}','{family}','{number}','{email}')")

        self.con.commit()

        print('add ok')

        self.clear()
        self.refresh()


    def delete(self):
        id = self.ui.line_5.text()
        self.my_cursor.execute(f"DELETE FROM contacts WHERE(id == {id})")
        
        self.con.commit()

        self.ui.line_5.setText('')
        
        print('delete ok')

        self.refresh()


    def delete_all(self):
        self.my_cursor.execute("DELETE FROM contacts ")
        self.con.commit()

        print('delete* ok')

        self.refresh()


    def dark(self):
        self.ui.setStyleSheet("background-color: gray;")

        print('dark ok')


    def white(self):
        self.ui.setStyleSheet("background-color: white;")

        print('white ok')


    def clear(self):
        self.ui.line_1.setText('')
        self.ui.line_2.setText('')
        self.ui.line_3.setText('')
        self.ui.line_4.setText('')
        self.ui.line_5.setText('')

        print('clear ok')


    def exit_0(self):
        print('Bye')
        final_app.quit()



final_app = QApplication()
main_window = Contact()
final_app.exec()