# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\phant\Documents\NCKU\Biomedical\HW1\fulltext.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.file = QtWidgets.QLabel(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(10, 10, 61, 21))
        self.file.setObjectName("file")
        self.Filepath = QtWidgets.QLineEdit(self.centralwidget)
        self.Filepath.setGeometry(QtCore.QRect(80, 10, 481, 21))
        self.Filepath.setObjectName("Filepath")
        self.Choose = QtWidgets.QPushButton(self.centralwidget)
        self.Choose.setGeometry(QtCore.QRect(570, 10, 75, 23))
        self.Choose.setObjectName("Choose")
        self.TextBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.TextBrowser.setGeometry(QtCore.QRect(280, 40, 451, 511))
        self.TextBrowser.setObjectName("TextBrowser")
        self.Parse = QtWidgets.QPushButton(self.centralwidget)
        self.Parse.setGeometry(QtCore.QRect(650, 10, 75, 23))
        self.Parse.setObjectName("Parse")
        self.doc = QtWidgets.QLabel(self.centralwidget)
        self.doc.setGeometry(QtCore.QRect(10, 40, 71, 16))
        self.doc.setObjectName("doc")
        self.find = QtWidgets.QLabel(self.centralwidget)
        self.find.setGeometry(QtCore.QRect(10, 260, 51, 21))
        self.find.setObjectName("find")
        self.KeyWord = QtWidgets.QLineEdit(self.centralwidget)
        self.KeyWord.setGeometry(QtCore.QRect(10, 280, 151, 21))
        self.KeyWord.setObjectName("KeyWord")
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(170, 280, 61, 23))
        self.Search.setObjectName("Search")
        self.Cal = QtWidgets.QLabel(self.centralwidget)
        self.Cal.setGeometry(QtCore.QRect(10, 475, 261, 81))
        self.Cal.setText("")
        self.Cal.setObjectName("Cal")
        self.DoclistWidget = QtWidgets.QListWidget(self.centralwidget)
        self.DoclistWidget.setGeometry(QtCore.QRect(10, 60, 256, 192))
        self.DoclistWidget.setObjectName("DoclistWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 25))
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
        self.file.setText(_translate("MainWindow", "File name"))
        self.Choose.setText(_translate("MainWindow", "..."))
        self.Parse.setText(_translate("MainWindow", "Load"))
        self.doc.setText(_translate("MainWindow", "Documents"))
        self.find.setText(_translate("MainWindow", "Search"))
        self.Search.setText(_translate("MainWindow", "Find"))

