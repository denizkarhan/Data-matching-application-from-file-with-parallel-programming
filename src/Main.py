from PyQt5 import QtWidgets
from MainForm import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import sys, os, requests
import myThread, removeChildFile

class Window(QtWidgets.QMainWindow):
    def __init__(self, 	products = [ {'Product': 'FLAG', 'Issue': 'Communication tactics', 'Company': 'CURO'}, {'Product': 'Student Loan', 'Issue': 'Struggling repay loan', 'Company': 'Student Loan Direct'}, {'Product': 'Mortgage', 'Issue': 'Closing Mortgage', 'Company': 'Statebridge Company'},], C1 = 0, C2 = 2):
        
        super(Window, self). __init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        a = [1, 23]
        total_time = 0
        self.loadProducts(products, 0, 5, a, total_time)
        self.ui.Filter.clicked.connect(self.filtre)

        oImage = QImage("../img/image3.png") # -> or path to "./img/image.png)
        sImage = oImage.scaled(QSize(1920, 1080))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.label = QLabel('Test', self)
        self.label.setGeometry(50, 50, 200, 50)
        self.show()

    def loadProducts(self, products, C1, C2, Process_Time, total_time):
        k = 0
        NAME = ['Product',
                'Issue',
                'Company',
                'State',
                'Zip Code',
                'Complaint ID']

        THREADNAME = ['', 'Proccess Time']
        PROCESSNAME = ['', 'Total Proccess Time']

        self.ui.table.setRowCount(len(products))
        self.ui.table.setColumnCount(C2 - C1 + 2)
        self.ui.table.setHorizontalHeaderLabels(NAME[C1:(C2+1)] + ["Match"])
        self.ui.threadtable.setRowCount(len(Process_Time))
        self.ui.threadtable.setColumnCount(2)
        self.ui.threadtable.setColumnWidth(0,60)
        self.ui.threadtable.setColumnWidth(1,300)
        self.ui.threadtable.setHorizontalHeaderLabels(THREADNAME)
        self.ui.timeTable.setColumnCount(2)
        self.ui.timeTable.setColumnWidth(0,0)
        self.ui.timeTable.setColumnWidth(1,370)
        self.ui.timeTable.setRowCount(1)
        self.ui.timeTable.setHorizontalHeaderLabels(PROCESSNAME)
        
        for i in range(len(products)):
            self.ui.table.setColumnWidth(i, 150)
            
        Process_Time[0] = Process_Time[-1]
        for i in Process_Time:
            self.ui.threadtable.setItem(k, 0, QTableWidgetItem("Thread"))
            self.ui.threadtable.setItem(k, 1, QTableWidgetItem(i))
            k += 1
        
        k = 0
        rowIndex = 0
        for product in products:
            i = 0
            a = 0
            for i in range(C1, C2 + 1):
                self.ui.table.setItem(rowIndex, a, QTableWidgetItem(product.get(NAME[i])))
                a += 1
            self.ui.table.setItem(rowIndex, C2 - C1 + 1, QTableWidgetItem(product.get("Match")))
            rowIndex += 1
        
        try:
            for i in range(5):
                self.ui.table.removeRow(0)
        except:
            pass
        self.ui.timeTable.setItem(0, 1, QTableWidgetItem(str(total_time)))
        products.clear()

    def show_state(self,value):
        cb = self.sender()
        print(value, cb.text(), cb.isChecked())

    def filtre(self):
        exampledict = { "C1":0,
                        "C2":5,
                        "C3":0,
                        "C4":5,
                        "SameProduct": -1,
                        "match" : 0,
                        "complaint_id":-1,
                        "threadCount": 10}

        items = self.ui.groupRate.findChildren(QtWidgets.QRadioButton)
        for cb in items:
            if cb.isChecked() and cb.text() == "Hepsi":
                pass
            elif cb.isChecked() and cb.text() == "% 10 Percent or More":
                exampledict["match"] = 10
            elif cb.isChecked() and cb.text() == "% 20 Percent or More":
                exampledict["match"] = 20
            elif cb.isChecked() and cb.text() == "% 30 Percent or More":
                exampledict["match"] = 30
            elif cb.isChecked() and cb.text() == "% 40 Percent or More":
                exampledict["match"] = 40
            elif cb.isChecked() and cb.text() == "% 50 Percent or More":
                exampledict["match"] = 50
            elif cb.isChecked() and cb.text() == "% 60 Percent or More":
                exampledict["match"] = 60
            elif cb.isChecked() and cb.text() == "% 70 Percent or More":
                exampledict["match"] = 70
            elif cb.isChecked() and cb.text() == "% 80 Percent or More":
                exampledict["match"] = 80
            elif cb.isChecked() and cb.text() == "% 90 Percent or More":
                exampledict["match"] = 90
            elif cb.isChecked() and cb.text() == "% 100":
                exampledict["match"] = 100

        # Values that are 100% the same
        items1 = self.ui.groupRows.findChildren(QtWidgets.QRadioButton)
        for cb1 in items1:
            if cb1.isChecked() and cb1.text() == "None":
                exampledict["SameProduct"] = -1
            elif cb1.isChecked() and cb1.text() == "Product":
                exampledict["SameProduct"] = 0
            elif cb1.isChecked() and cb1.text() == "Issue":
                exampledict["SameProduct"] = 1
            elif cb1.isChecked() and cb1.text() == "Company":
                exampledict["SameProduct"] = 2
            elif cb1.isChecked() and cb1.text() == "State":
                exampledict["SameProduct"] = 3
            elif cb1.isChecked() and cb1.text() == "Zip Code":
                exampledict["SameProduct"] = 4
            elif cb1.isChecked() and cb1.text() == "Complaint ID":
                exampledict["SameProduct"] = 5

        # Range of Value to Search
        items2 = self.ui.groupRows2.findChildren(QtWidgets.QCheckBox)
        SearchRange = []
        for cb2 in items2:
            if cb2.isChecked() and cb2.text() == "None":
                SearchRange = [0, 1, 2, 3, 4, 5]
            elif cb2.isChecked() and cb2.text() == "Product":
                SearchRange.append(0)
            elif cb2.isChecked() and cb2.text() == "Issue":
                SearchRange.append(1)
            elif cb2.isChecked() and cb2.text() == "Company":
                SearchRange.append(2)
            elif cb2.isChecked() and cb2.text() == "State":
                SearchRange.append(3)
            elif cb2.isChecked() and cb2.text() == "Zip Code":
                SearchRange.append(4)
            elif cb2.isChecked() and cb2.text() == "Complaint ID":
                SearchRange.append(5)

        # Value Range to Display
        items3 = self.ui.groupRows3.findChildren(QtWidgets.QCheckBox)
        ViewRange = []
        for cb3 in items3:
            if cb3.isChecked() and cb3.text() == "None":
                ViewRange = [0, 1, 2, 3, 4, 5]
            elif cb3.isChecked() and cb3.text() == "Product":
                ViewRange.append(0)
            elif cb3.isChecked() and cb3.text() == "Issue":
                ViewRange.append(1)
            elif cb3.isChecked() and cb3.text() == "Company":
                ViewRange.append(2)
            elif cb3.isChecked() and cb3.text() == "State":
                ViewRange.append(3)
            elif cb3.isChecked() and cb3.text() == "Zip Code":
                ViewRange.append(4)
            elif cb3.isChecked() and cb3.text() == "Complaint ID":
                ViewRange.append(5)

        if self.ui.threadCount.text():
            exampledict["threadCount"] = self.ui.threadCount.text()
        
        if self.ui.CompID.text():
            exampledict["complaint_id"] = self.ui.CompID.text()

        if (len(ViewRange) > 0):
            ViewRange.sort()
            exampledict["C1"] = ViewRange[0]
            exampledict["C2"] = ViewRange[len(ViewRange) - 1]
        else:
            exampledict["C1"] = 0
            exampledict["C2"] = 5
        
        if (len(SearchRange) > 0):
            SearchRange.sort()
            exampledict["C3"] = SearchRange[0]
            exampledict["C4"] = SearchRange[len(SearchRange) - 1]
        else:
            exampledict["C3"] = 0
            exampledict["C4"] = 5

        DATA, Process_Time, line, total_time = myThread.start_find( exampledict.get("C1"),
                                                                    exampledict.get("C2"),
                                                                    exampledict.get("C3"),
                                                                    exampledict.get("C4"),
                                                                    exampledict.get("SameProduct"),
                                                                    exampledict.get("match"),
                                                                    exampledict.get("complaint_id"),
                                                                    exampledict.get("threadCount"))
        removeChildFile.removeFile()
        self.loadProducts(DATA, exampledict.get("C1"), exampledict.get("C2"), Process_Time, total_time)

def	app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
