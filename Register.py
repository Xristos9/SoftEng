import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui", self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccButton.clicked.connect(self.gotocreate)

    def loginfunction(self):
        username = self.username.text()
        password = self.password.text()
        print("Successfully logged in with username: ", username, "and password :", password)

    def gotocreate(self):
    	createacc = CreateAcc()
    	widget.addWidget(createacc)
    	widget.setCurrentIndex(widget.currentIndex() + 1)	

class CreateAcc(QDialog):
	def __init__(self):
		super(CreateAcc, self).__init__()
		loadUi("Register.ui", self)
		self.signupbutton.clicked.connect(self.createaccfunction)

	def createaccfunction(self):
		username = self.username.text()
		email = self.email.text()
		phone = self.phoneNumber.text()

		if self.password.text() == self.repeatpassword.text():
			password = self.password.text()
			print("Successfully created an Account with username: ", username, "and password:", password )

app = QApplication(sys.argv)
mainwindow = Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(421)
widget.setFixedHeight(721)
widget.show()
app.exec_()