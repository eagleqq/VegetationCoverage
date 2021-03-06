# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1213, 739)
        MainWindow.setStyleSheet("font: 75 14pt \"Aharoni\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(500, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_path = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_path.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_path.setStyleSheet("font: 75 9pt \"Aharoni\";")
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.horizontalLayout.addWidget(self.lineEdit_path)
        self.pushButton_select = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_select.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton_select.setObjectName("pushButton_select")
        self.horizontalLayout.addWidget(self.pushButton_select)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget_img = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_img.setStyleSheet("font: 9pt \"新宋体\";")
        self.listWidget_img.setObjectName("listWidget_img")
        self.verticalLayout.addWidget(self.listWidget_img)
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab_2)
        self.lcdNumber.setMinimumSize(QtCore.QSize(0, 138))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lcdNumber.setFont(font)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcdNumber.setLineWidth(5)
        self.lcdNumber.setMidLineWidth(1)
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.verticalLayout_2.addWidget(self.lcdNumber)
        self.graphicsView2 = QtWidgets.QGraphicsView(self.tab_2)
        self.graphicsView2.setObjectName("graphicsView2")
        self.verticalLayout_2.addWidget(self.graphicsView2)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_zoomin = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zoomin.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_zoomin.setStyleSheet("font: 12pt \"新宋体\";")
        self.pushButton_zoomin.setObjectName("pushButton_zoomin")
        self.horizontalLayout_3.addWidget(self.pushButton_zoomin)
        self.pushButton_zoomout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_zoomout.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_zoomout.setStyleSheet("font: 12pt \"新宋体\";")
        self.pushButton_zoomout.setObjectName("pushButton_zoomout")
        self.horizontalLayout_3.addWidget(self.pushButton_zoomout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1213, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "图片选择"))
        self.pushButton_select.setText(_translate("MainWindow", "选择图片文件夹"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "检测图"))
        self.pushButton_zoomin.setText(_translate("MainWindow", "缩小图片"))
        self.pushButton_zoomout.setText(_translate("MainWindow", "放大图片"))

