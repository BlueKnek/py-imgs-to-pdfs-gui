# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img = QtWidgets.QGraphicsView(self.centralwidget)
        self.img.setObjectName("img")
        self.horizontalLayout.addWidget(self.img)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.current = QtWidgets.QLabel(self.centralwidget)
        self.current.setObjectName("current")
        self.verticalLayout.addWidget(self.current)
        self.group = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group.sizePolicy().hasHeightForWidth())
        self.group.setSizePolicy(sizePolicy)
        self.group.setObjectName("group")
        self.verticalLayout.addWidget(self.group)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.last = QtWidgets.QPushButton(self.centralwidget)
        self.last.setObjectName("last")
        self.gridLayout.addWidget(self.last, 1, 0, 1, 1)
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        self.prev.setObjectName("prev")
        self.gridLayout.addWidget(self.prev, 0, 0, 1, 1)
        self.new_ = QtWidgets.QPushButton(self.centralwidget)
        self.new_.setObjectName("new_")
        self.gridLayout.addWidget(self.new_, 1, 1, 1, 1)
        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setObjectName("next")
        self.gridLayout.addWidget(self.next, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.generate = QtWidgets.QPushButton(self.centralwidget)
        self.generate.setObjectName("generate")
        self.verticalLayout.addWidget(self.generate)
        self.progress = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setProperty("value", 24)
        self.progress.setObjectName("progress")
        self.verticalLayout.addWidget(self.progress)
        self.list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setObjectName("list")
        self.verticalLayout.addWidget(self.list)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 29))
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
        self.current.setText(_translate("MainWindow", "TextLabel"))
        self.last.setText(_translate("MainWindow", "Last"))
        self.prev.setText(_translate("MainWindow", "<"))
        self.new_.setText(_translate("MainWindow", "New"))
        self.next.setText(_translate("MainWindow", ">"))
        self.generate.setText(_translate("MainWindow", "Generate PDFs"))

