import sys
import demo as dm
import hashingPassword as hp
from Connector import mydb
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccButton.clicked.connect(self.gotocreate)
        # connects the button with a function

    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()
        # connect with database here
        
        cursor = mydb.cursor()# connect with database here
        exists = '''SELECT COUNT(*) FROM users WHERE Usersusername = %s'''
        cursor.execute(exists, (username, ))
        count = cursor.fetchone()

        if count[0] == 0:
            QMessageBox.about(self, "Error", "Username does not exist!")
        else:
            word = '''SELECT Userspwd FROM users WHERE Usersusername = %s''' #return from select is a tuple
            cursor.execute(word, (username, ))
            storedPass = cursor.fetchone()
            if hp.verify_password(storedPass[0], password):
                id = '''SELECT UsersId FROM users WHERE Usersusername = %s '''
                cursor.execute(id, (username, ))
                storedId = cursor.fetchone()
                global ID 
                ID = storedId[0]
                print("Stored : ", storedId[0] , "tuple: ", storedId , "ID" , ID)
                print(type(ID))
                role ='''SELECT role_id FROM user_roles WHERE user_id = %s '''
                cursor.execute(role, (ID,))
                storedRole = cursor.fetchone()
                ROLE = storedRole[0]
                print(type(ROLE), ROLE)
                
                if ROLE == 0:
                    self.gotohomescreen()
                elif ROLE == 1:
                    pass 
            else:
                QMessageBox.about(self, "Error", "Wrong password! ")
                
    def gotocreate(self):
        createacc = CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentWidget(createacc)

    def gotohomescreen(self):
        #exec('HomeScreen.py')
        homescreen = HomeScreen()
        widget.addWidget(homescreen)
        widget.setCurrentWidget(homescreen)
        print("Successfully logged in")


class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc, self).__init__()
        loadUi("Register.ui", self)
        self.signupbutton.clicked.connect(self.registration)
        self.gotologinButton.clicked.connect(self.gotologin)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.repeatpassword.setEchoMode(QtWidgets.QLineEdit.Password)

    # Checkboxes
        self.checkBox.stateChanged.connect(self.uncheck)
        self.checkBox2.stateChanged.connect(self.uncheck)

    def registration(self):
        username = self.username.text() #username from register form
        email = self.email.text() #email from register form
        password = self.password.text()
        repeatpassword = self.repeatpassword.text()

        cursor = mydb.cursor()# connect with database here
        exists = '''SELECT COUNT(*) FROM users WHERE Usersusername = %s OR Usersemail = %s'''
        cursor.execute(exists, (username, email))
        count = cursor.fetchone()

        print(type(count[0]))
        print(count[0] == 1)
        print(count[0] == 0)

        if count[0] == 1:
            QMessageBox.about(self, "Error", "Username or email already exists")
        else:
            if dm.check_blank(username,email,password,repeatpassword) != True or (self.checkBox.isChecked() == False and self.checkBox2.isChecked() == False):
                QMessageBox.about(self, "Error", "Fill all the lines and Checkboxes")
            else:
                if password != repeatpassword:
                    QMessageBox.about(self, "Error", "Password don't match!")
                elif dm.checker(password) != True:
                    QMessageBox.about(self, "Error", "Password must contain at least 8 characters, one number, one capital and a special character.")
                elif dm.valemail(email) is not True:
                    QMessageBox.about(self, "Error", "Email doesn't exist or is not in the right structure!")
                else:  # Resize
                    password_hash = hp.hash_password(password)# utf-8
                    insert = '''INSERT INTO users(Usersusername, Usersemail, Userspwd) VALUES('{}', '{}', '{}')'''.format(username,email,password_hash)#alternative way of structing sql INSERT query
                    cursor.execute(insert) 
                    mydb.commit() #only for INSERT
                    
                    select = '''SELECT UsersId FROM users WHERE Usersusername = %s''' 
                    cursor.execute(select, (username,)) # username passes to %s as a string
                    result = cursor.fetchone() #user Id to result (tuple)

                    if self.checkBox.isChecked():
                        cursor.execute('''INSERT INTO user_roles(user_id, role_id) VALUES (%d, 0) ''' %result)
                        mydb.commit() #result is a tuple with one integer element and passes as a digit number with %d
                    elif self.checkBox2.isChecked():
                        cursor.execute('''INSERT INTO user_roles(user_id, role_id) VALUES (%d, 1) ''' %result)
                        mydb.commit()

                    self.gotologin()
                
    def uncheck(self, state): #Explaination
        if state == Qt.Checked:
            if self.sender() == self.checkBox:
                self.checkBox2.setChecked(False)
            elif self.sender() == self.checkBox2:
                self.checkBox.setChecked(False) 
    
    def gotologin(self):
        login = Login()
        widget.addWidget(login)
        widget.setCurrentWidget(login)


class HomeScreen(QDialog):
    def __init__(self):
        super(HomeScreen, self).__init__()
        loadUi("HomeScreen.ui", self)
        
        self.FlightsButton.clicked.connect(self.createSearch)
        #self.ForumsButton.clicked.connect(self.createSearch)
        #self.HomeButton.clicked.connect(self.createSearch)
        self.SearchButton.clicked.connect(self.createSearch)
        
        #self.FavoritesButton.clicked.connect(self.createSearch)
        #self.ProfileButton.clicked.connect(self.createSearch)

        # ComboBoxes
        self.comboBoxAccomodation.currentIndexChanged.connect(self.combochanged)
        self.comboBoxAttractions.currentIndexChanged.connect(self.combochanged)
        self.comboBoxRestaurants.currentIndexChanged.connect(self.combochanged)
        self.comboBoxTransport.currentIndexChanged.connect(self.combochanged)

    def combochanged(self):
        print(self.comboBoxAccomodation.currentIndex())
        index = self.createSearch()
        if self.comboBoxAccomodation.currentIndex() == 1:
            pass
        elif self.comboBoxAccomodation.currentIndex() == 2:
            pass
        elif self.comboBoxAccomodation.currentIndex() == 3:
            pass
        elif self.comboBoxAccomodation.currentIndex() == 4:
            pass
        print("value Changed")

    def createSearch(self):
        search = Search()
        widget.addWidget(search)
        widget.setCurrentWidget(search)
        print('hello') 

class Search(QDialog):
    def __init__(self):
        super(Search, self).__init__()
        loadUi("Search.ui", self)



app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(421)
widget.setFixedHeight(721)
widget.show()
app.exec_()
