# This is the UI for the Home Page
# The colors and font aren't 100% correct but will be fixed later


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 729)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("background-color: rgb(129, 163, 255)\n"
                                    "")
        self.groupBox.setObjectName("groupBox")
        self.title = QtWidgets.QLabel(self.groupBox)
        self.title.setGeometry(QtCore.QRect(160, 60, 141, 31))
        self.title.setStyleSheet("background-color:rgb(147, 255, 192)\n"
                                 "")
        self.title.setObjectName("title")
        self.pushButto_search = QtWidgets.QPushButton(self.groupBox)
        self.pushButto_search.setGeometry(QtCore.QRect(350, 20, 75, 23))
        self.pushButto_search.setStyleSheet(
            "background-color:rgb(147, 255, 192)")
        self.pushButto_search.setObjectName("pushButto_search")
        self.lineEdit_activities = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_activities.setGeometry(QtCore.QRect(40, 280, 341, 61))
        self.lineEdit_activities.setStyleSheet(
            "background-color:rgb(243, 255, 179)")
        self.lineEdit_activities.setObjectName("lineEdit_activities")
        self.textEdit_Nearby = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Nearby.setGeometry(QtCore.QRect(40, 340, 341, 61))
        self.textEdit_Nearby.setStyleSheet(
            "background-color:rgb(243, 255, 179)")
        self.textEdit_Nearby.setObjectName("textEdit_Nearby")
        self.textEdit_Map = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_Map.setGeometry(QtCore.QRect(40, 400, 341, 61))
        self.textEdit_Map.setStyleSheet("background-color:rgb(243, 255, 179)")
        self.textEdit_Map.setObjectName("textEdit_Map")
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setGeometry(QtCore.QRect(280, 460, 101, 23))
        self.pushButton_11.setStyleSheet("background-color:rgb(101, 111, 255)")
        self.pushButton_11.setObjectName("pushButton_11")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 120, 351, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.estiasi = QtWidgets.QPushButton(self.layoutWidget)
        self.estiasi.setStyleSheet("background-color: rgb(103, 255, 133)")
        self.estiasi.setObjectName("estiasi")
        self.horizontalLayout_2.addWidget(self.estiasi)
        self.flights = QtWidgets.QPushButton(self.layoutWidget)
        self.flights.setStyleSheet("background-color: rgb(103, 255, 133)")
        self.flights.setObjectName("flights")
        self.horizontalLayout_2.addWidget(self.flights)
        self.stay = QtWidgets.QPushButton(self.layoutWidget)
        self.stay.setStyleSheet("background-color: rgb(103, 255, 133)")
        self.stay.setObjectName("stay")
        self.horizontalLayout_2.addWidget(self.stay)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fun = QtWidgets.QPushButton(self.layoutWidget)
        self.fun.setStyleSheet("background-color: rgb(103, 255, 133)")
        self.fun.setObjectName("fun")
        self.horizontalLayout.addWidget(self.fun)
        self.transport = QtWidgets.QPushButton(self.layoutWidget)
        self.transport.setStyleSheet("background-color: rgb(103, 255, 133)")
        self.transport.setObjectName("transport")
        self.horizontalLayout.addWidget(self.transport)
        self.forum = QtWidgets.QPushButton(self.layoutWidget)
        self.forum.setStyleSheet("background-color: rgb(103, 255, 133)")
        self.forum.setObjectName("forum")
        self.horizontalLayout.addWidget(self.forum)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(40, 460, 239, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setStyleSheet("background-color:rgb(101, 111, 255)")
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_9.setStyleSheet("background-color:rgb(101, 111, 255)")
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_10.setStyleSheet("background-color:rgb(101, 111, 255)")
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_3.addWidget(self.pushButton_10)
        self.verticalLayout_2.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Home"))
        self.title.setText(_translate("MainWindow", "BookAll"))
        self.pushButto_search.setText(_translate("MainWindow", "Search"))
        self.lineEdit_activities.setText(
            _translate("MainWindow", "Δραστηριότητες"))
        self.textEdit_Nearby.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Προτάσεις για κοντινές δραστηριότητες</p>\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_Map.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                             "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                             "p, li { white-space: pre-wrap; }\n"
                                             "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                             "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Χάρτες</p>\n"
                                             "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_11.setText(_translate("MainWindow", "Profile"))
        self.estiasi.setText(_translate("MainWindow", "Εστίαση"))
        self.flights.setText(_translate("MainWindow", "Πτήσεις"))
        self.stay.setText(_translate("MainWindow", "Διαμονή"))
        self.fun.setText(_translate("MainWindow", "Διασκέδαση"))
        self.transport.setText(_translate("MainWindow", "Μεταφορές"))
        self.forum.setText(_translate("MainWindow", "Forum"))
        self.pushButton_8.setText(_translate("MainWindow", "Home"))
        self.pushButton_9.setText(_translate("MainWindow", "Search"))
        self.pushButton_10.setText(_translate("MainWindow", "Liked"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
