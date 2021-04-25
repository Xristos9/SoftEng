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

	def loadData(self):
		pass
    	#data from the database
    	#sample data
    	#results = [{"Result 1":"Hotel Melanie", "Number":45, "Address":"New York"},{"Result 2":"Hotel", "Number":40, "Address":"LA"} ]
    	#row = 0
    	#self.tableWidget.setRowCount(len(results))
		#for result in results: 
			#self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(result["Result 1"]))
			#self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(result["Result 1"]))
			#row = row + 1

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



