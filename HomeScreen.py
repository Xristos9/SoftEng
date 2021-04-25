import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi

class HomeScreen(QDialog):
    def __init__(self):
        super(HomeScreen,self).__init__()
        loadUi("HomeScreen.ui", self)

        self.FlightsButton.clicked.connect(self.searchForm)
        self.ForumsButton.clicked.connect(self.searchForm)
        self.HomeButton.clicked.connect(self.searchForm)
        self.SearchButton.clicked.connect(self.searchForm)
        self.FavoritesButton.clicked.connect(self.searchForm)
        self.ProfileButton.clicked.connect(self.searchForm)

        self.comboBoxAccomodation.currentIndexChanged.connect(self.combochanged)
        self.comboBoxAttractions.currentIndexChanged.connect(self.combochanged)
        self.comboBoxRestaurants.currentIndexChanged.connect(self.combochanged)
        self.comboBoxTransport.currentIndexChanged.connect(self.combochanged)


    def combochanged(self):
        self.AccomodationButton.clicked.connect(self.searchForm)
        self.AttractionsButton.clicked.connect(self.searchForm)
        self.RestaurantsButton.clicked.connect(self.searchForm)
        self.TransportButton.clicked.connect(self.searchForm)
        print("value Changed")

    def searchForm(self):
        print("Main Button Clicked")    
