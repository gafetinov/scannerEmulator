# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './views/design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(288, 449)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.codesList = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.codesList.setObjectName("codesList")
        self.verticalLayout.addWidget(self.codesList)
        self.scanButton = QtWidgets.QPushButton(self.centralwidget)
        self.scanButton.setObjectName("scanButton")
        self.verticalLayout.addWidget(self.scanButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.scanButton.setText(_translate("MainWindow", "Сканировать"))
