from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1769, 998)
        
        font = QtGui.QFont()
        font.setPointSize(9)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Filter = QtWidgets.QPushButton(self.centralwidget)
        self.Filter.setGeometry(QtCore.QRect(310, 440, 531, 41))
        self.Filter.setCheckable(False)
        self.Filter.setAutoRepeat(False)
        self.Filter.setAutoExclusive(False)
        self.Filter.setObjectName("Filter")
        
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(60, 490, 1141, 371))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1139, 369))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        
        self.horizontalLayout_2.addWidget(self.table)

        self.table.setObjectName("table")
        self.table.setColumnCount(0)
        self.table.setRowCount(0)
        
        self.scrollArea_3 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_3.setGeometry(QtCore.QRect(1230, 490, 521, 371))
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 519, 369))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        
        self.threadtable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents_3)
        
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        
        self.horizontalLayout.addWidget(self.threadtable)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.groupRate = QtWidgets.QGroupBox(self.centralwidget)
        self.groupRate.setGeometry(QtCore.QRect(20, 40, 241, 391))
        self.groupRate.setObjectName("groupRate")
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupRate)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 60, 171, 331))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.cb0 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb0.setObjectName("cb0")
        
        self.cb10 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb10.setObjectName("cb10")
        
        self.cb20 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb20.setObjectName("cb20")
        
        self.cb30 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb30.setObjectName("cb30")
        
        self.cb40 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb40.setObjectName("cb40")
                
        self.cb50 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb50.setObjectName("cb50")
        
        self.cb60 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb60.setObjectName("cb60")
        
        self.cb70 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb70.setObjectName("cb70")
                
        self.cb80 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb80.setObjectName("cb80")
        
        self.cb90 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb90.setObjectName("cb90")
        
        self.cb100 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.cb100.setObjectName("cb100")

        self.layoutSimilar = QtWidgets.QGridLayout(self.verticalLayoutWidget)
        self.layoutSimilar.setObjectName("layoutSimilar")
        self.layoutSimilar.setContentsMargins(5, 5, 5, 5)
        self.layoutSimilar.addWidget(self.cb0, 0, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb10, 1, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb20, 2, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb30, 3, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb40, 4, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb50, 5, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb60, 6, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb70, 7, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb80, 8, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb90, 9, 0, 1, 1)
        self.layoutSimilar.addWidget(self.cb100, 10, 0, 1, 1)

        self.threadtable.setObjectName("threadtable")
        self.threadtable.setColumnCount(0)
        self.threadtable.setRowCount(0)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(930, 0, 311, 91))
        self.label.setText("")
        self.label.setObjectName("label")
        
        self.groupInput = QtWidgets.QGroupBox(self.centralwidget)
        self.groupInput.setGeometry(QtCore.QRect(1010, 40, 301, 391))
        self.groupInput.setObjectName("groupInput")
        
        self.threadCount = QtWidgets.QLineEdit(self.groupInput)
        self.threadCount.setGeometry(QtCore.QRect(40, 70, 171, 31))
        self.threadCount.setObjectName("threadCount")
        
        self.CompID = QtWidgets.QLineEdit(self.groupInput)
        self.CompID.setGeometry(QtCore.QRect(40, 140, 171, 31))
        self.CompID.setObjectName("CompID")
        
        self.label_2 = QtWidgets.QLabel(self.groupInput)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 141, 16))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.groupInput)
        self.label_3.setGeometry(QtCore.QRect(40, 50, 171, 16))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.groupRows = QtWidgets.QGroupBox(self.centralwidget)
        self.groupRows.setGeometry(QtCore.QRect(510, 40, 251, 391))
        self.groupRows.setObjectName("groupRows")

        self.groupRows2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupRows2.setGeometry(QtCore.QRect(260, 40, 251, 391))
        self.groupRows2.setObjectName("groupRows2")
        
        self.groupRows3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupRows3.setGeometry(QtCore.QRect(760, 40, 251, 391))
        self.groupRows3.setObjectName("groupRows3")
        
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupRows)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 60, 160, 331))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupRows2)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(50, 60, 160, 331))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupRows3)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(40, 60, 160, 331))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        
        self.checkBox_8 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_11.setObjectName("checkBox_11")      
        self.checkBox_12 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.checkBox_14.setObjectName("checkBox_14")
        
        self.radioButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioButton_7.setObjectName("radioButton_7")
        
        self.checkBox_29 = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_29.setObjectName("checkBox_29")
        self.checkBox_30 = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_30.setObjectName("checkBox_30")
        self.checkBox_31 = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_31.setObjectName("checkBox_31")
        self.checkBox_32 = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_32.setObjectName("checkBox_32")
        self.checkBox_33 = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_33.setObjectName("checkBox_33")
        self.checkBox_34 = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_34.setObjectName("checkBox_34")
        self.checkBox_35 = QtWidgets.QCheckBox(self.gridLayoutWidget_5)
        self.checkBox_35.setObjectName("checkBox_35")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.addWidget(self.radioButton, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.radioButton_2, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.radioButton_3, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.radioButton_4, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.radioButton_5, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.radioButton_6, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.radioButton_7, 0, 0, 1, 1)

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.addWidget(self.checkBox_13, 4, 0, 1, 1)
        self.gridLayout_2.addWidget(self.checkBox_11, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.checkBox_10, 3, 0, 1, 1)
        self.gridLayout_2.addWidget(self.checkBox_9, 5, 0, 1, 1)
        self.gridLayout_2.addWidget(self.checkBox_8, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.checkBox_12, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.checkBox_14, 6, 0, 1, 1)

        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.addWidget(self.checkBox_29, 1, 0, 1, 1)
        self.gridLayout_5.addWidget(self.checkBox_30, 5, 0, 1, 1)
        self.gridLayout_5.addWidget(self.checkBox_31, 3, 0, 1, 1)
        self.gridLayout_5.addWidget(self.checkBox_33, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.checkBox_32, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.checkBox_34, 4, 0, 1, 1)
        self.gridLayout_5.addWidget(self.checkBox_35, 6, 0, 1, 1)

        self.timeTable = QtWidgets.QTableWidget(self.centralwidget)
        self.timeTable.setGeometry(QtCore.QRect(1340, 380, 401, 61))
        self.timeTable.setObjectName("timeTable")
        self.timeTable.setColumnCount(0)
        self.timeTable.setRowCount(0)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1769, 26))
        self.menubar.setObjectName("menubar")
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setMenuBar(self.menubar) 
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setStatusBar(self.statusbar)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Filter.setText(_translate("MainWindow", "Filter"))
        self.groupRate.setTitle(_translate("MainWindow", "Percentage of Searched Range"))

        self.cb0.setText(_translate("MainWindow", "All"))
        self.cb10.setText(_translate("MainWindow", "% 10 Percent or More"))
        self.cb20.setText(_translate("MainWindow", "% 20 Percent or More"))
        self.cb30.setText(_translate("MainWindow", "% 30 Percent or More"))
        self.cb40.setText(_translate("MainWindow", "% 40 Percent or More"))
        self.cb50.setText(_translate("MainWindow", "% 50 Percent or More"))
        self.cb60.setText(_translate("MainWindow", "% 60 Percent or More"))
        self.cb70.setText(_translate("MainWindow", "% 70 Percent or More"))
        self.cb80.setText(_translate("MainWindow", "% 80 Percent or More"))
        self.cb90.setText(_translate("MainWindow", "% 90 Percent or More"))
        self.cb100.setText(_translate("MainWindow", "% 100"))
        
        self.groupInput.setTitle(_translate("MainWindow", "Input"))
        
        self.label_2.setText(_translate("MainWindow", "Enter Complaint ID:"))
        self.label_3.setText(_translate("MainWindow", "Enter Thread Sayisini:"))
        
        self.groupRows.setTitle(_translate("MainWindow", "Same Column Similarity"))
        self.groupRows2.setTitle(_translate("MainWindow", "Search Range"))
        self.groupRows3.setTitle(_translate("MainWindow", "View Range"))
        
        self.checkBox_8.setText(_translate("MainWindow", "Product"))
        self.checkBox_9.setText(_translate("MainWindow", "Zip Code"))
        self.checkBox_10.setText(_translate("MainWindow", "Company"))
        self.checkBox_11.setText(_translate("MainWindow", "Issue"))
        self.checkBox_12.setText(_translate("MainWindow", "All"))
        self.checkBox_13.setText(_translate("MainWindow", "State"))
        self.checkBox_14.setText(_translate("MainWindow", "Complaint ID"))
        
        self.checkBox_29.setText(_translate("MainWindow", "Product"))
        self.checkBox_30.setText(_translate("MainWindow", "Zip Code"))
        self.checkBox_31.setText(_translate("MainWindow", "Company"))
        self.checkBox_32.setText(_translate("MainWindow", "Issue"))
        self.checkBox_33.setText(_translate("MainWindow", "All"))
        self.checkBox_34.setText(_translate("MainWindow", "State"))
        self.checkBox_35.setText(_translate("MainWindow", "Complaint ID"))
        
        self.radioButton.setText(_translate("MainWindow", "Zip Code"))
        self.radioButton_2.setText(_translate("MainWindow", "Complaint ID"))
        self.radioButton_3.setText(_translate("MainWindow", "State"))
        self.radioButton_4.setText(_translate("MainWindow", "Company"))
        self.radioButton_5.setText(_translate("MainWindow", "Issue"))
        self.radioButton_6.setText(_translate("MainWindow", "Product"))
        self.radioButton_7.setText(_translate("MainWindow", "None"))
