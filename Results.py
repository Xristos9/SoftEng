import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class MainWindow(QDialog):
	def __init__(self):
		super(MainWindow, self).__init__()
		loadUi("Results.ui", self)

		self.tableWidget.setColumnWidth(0,300)
		self.tableWidget.setColumnWidth(1,600)
		self.tableWidget2.setColumnWidth(0,300)
		self.tableWidget2.setColumnWidth(1,600)
		self.tableWidget3.setColumnWidth(0,300)
		self.tableWidget3.setColumnWidth(1,600)
		
		#self.HomeButton.clicked.connect(self.clicked)
    	#self.SearchButton.clicked.connect(self.clicked)
    	#self.FavoritesButton.clicked.connect(self.clicked)
    	#self.ProfileButton.clicked.connect(self.clicked)
		
	def clicked(self):
		
		print("Main Button Clicked")


app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(721)
widget.setFixedWidth(421)
widget.show()
sys.exit(app.exec_())



