from PyQt5 import QtWidgets
from MainForm import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import sys, os, myThread, removeChildFile, requests

class Window(QtWidgets.QMainWindow):
    def __init__(self, 	products = [ {'Product': 'FLAG', 'Issue': 'Communication tactics', 'Company': 'CURO'}, {'Product': 'Student Loan', 'Issue': 'Struggling repay loan', 'Company': 'Student Loan Direct'}, {'Product': 'Mortgage', 'Issue': 'Closing Mortgage', 'Company': 'Statebridge Company'},], C1 = 0, C2 = 2):
        super(Window, self). __init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        a=[1,23]
        total_time = 0
        self.loadProducts(products, 0, 5, a, total_time)
        self.ui.Filtrele.clicked.connect(self.filtre)

        oImage = QImage("image3.png")
        sImage = oImage.scaled(QSize(1920,1080))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.label = QLabel('Test', self)
        self.label.setGeometry(50,50,200,50)
        self.show()

    def loadProducts(self, products, C1, C2, Process_Time, total_time):
        NAME = ['Product','Issue','Company', 'State', 'Zip Code', 'Complaint ID']
        THREADNAME = ['','Çalışma Süresi']
        PROCESSNAME = ['','Toplam İşlem Zamanı']
        self.ui.table.setRowCount(len(products))
        self.ui.table.setColumnCount(C2 - C1 + 2)
        self.ui.table.setHorizontalHeaderLabels(NAME[C1:(C2+1)]+["Match"])
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
        
        
        i = 0
        for i in range(len(products)):
            self.ui.table.setColumnWidth(i,150)
        k=0
        Process_Time[0] = Process_Time[-1]
        for i in Process_Time:
            self.ui.threadtable.setItem(k, 0, QTableWidgetItem("Thread"))
            self.ui.threadtable.setItem(k, 1, QTableWidgetItem(i))
            k+=1
        k=0
        rowIndex = 0
        for product in products:
            i = 0
            a = 0
            for i in range(C1, C2 + 1):
                self.ui.table.setItem(rowIndex, a, QTableWidgetItem(product.get(NAME[i])))
                a+=1
            self.ui.table.setItem(rowIndex, C2 - C1 + 1, QTableWidgetItem(product.get("Match")))
            rowIndex += 1
        rowIndex = 0
        try:
            self.ui.table.removeRow(0)
            self.ui.table.removeRow(0)
            self.ui.table.removeRow(0)
            self.ui.table.removeRow(0)
            self.ui.table.removeRow(0)
        except:
            pass
        self.ui.timeTable.setItem(rowIndex, 1, QTableWidgetItem(str(total_time)))
        products.clear()

    def show_state(self,value):
        cb = self.sender()
        print(value)
        print(cb.text())
        print(cb.isChecked())

    def filtre(self):
        exampledict = {"C1":0, "C2":5, "C3":0, "C4":5, "SameProduct": -1, "match" : 0, "complaint_id":-1, "threadCount": 10}
        items = self.ui.groupOran.findChildren(QtWidgets.QRadioButton)
        for cb in items:
            if cb.isChecked() and cb.text() == "Hepsi":
                pass
            elif cb.isChecked() and cb.text() == "% 10 ve Üzeri":
                exampledict["match"] = 10
            elif cb.isChecked() and cb.text() == "% 20 ve Üzeri":
                exampledict["match"] = 20
            elif cb.isChecked() and cb.text() == "% 30 ve Üzeri":
                exampledict["match"] = 30
            elif cb.isChecked() and cb.text() == "% 40 ve Üzeri":
                exampledict["match"] = 40
            elif cb.isChecked() and cb.text() == "% 50 ve Üzeri":
                exampledict["match"] = 50
            elif cb.isChecked() and cb.text() == "% 60 ve Üzeri":
                exampledict["match"] = 60
            elif cb.isChecked() and cb.text() == "% 70 ve Üzeri":
                exampledict["match"] = 70
            elif cb.isChecked() and cb.text() == "% 80 ve Üzeri":
                exampledict["match"] = 80
            elif cb.isChecked() and cb.text() == "% 90 ve Üzeri":
                exampledict["match"] = 90
            elif cb.isChecked() and cb.text() == "% 100":
                exampledict["match"] = 100

        # %100 aynı sütunlar
        items1 = self.ui.groupRows.findChildren(QtWidgets.QRadioButton)
        for cb1 in items1:
            if cb1.isChecked() and cb1.text() == "Hiçbiri":
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

        # Aranılan Aralık
        items2 = self.ui.groupRows2.findChildren(QtWidgets.QCheckBox)
        arananAralik = []
        for cb2 in items2:
            if cb2.isChecked() and cb2.text() == "Hepsi":
                arananAralik = [0,1,2,3,4,5]
            elif cb2.isChecked() and cb2.text() == "Product":
                arananAralik.append(0)
            elif cb2.isChecked() and cb2.text() == "Issue":
                arananAralik.append(1)
            elif cb2.isChecked() and cb2.text() == "Company":
                arananAralik.append(2)
            elif cb2.isChecked() and cb2.text() == "State":
                arananAralik.append(3)
            elif cb2.isChecked() and cb2.text() == "Zip Code":
                arananAralik.append(4)
            elif cb2.isChecked() and cb2.text() == "Complaint ID":
                arananAralik.append(5)

        # Gösterilen Aralık
        items3 = self.ui.groupRows3.findChildren(QtWidgets.QCheckBox)
        gosterilenAralik = []
        for cb3 in items3:
            if cb3.isChecked() and cb3.text() == "Hepsi":
                gosterilenAralik = [0,1,2,3,4,5]
            elif cb3.isChecked() and cb3.text() == "Product":
                gosterilenAralik.append(0)
            elif cb3.isChecked() and cb3.text() == "Issue":
                gosterilenAralik.append(1)
            elif cb3.isChecked() and cb3.text() == "Company":
                gosterilenAralik.append(2)
            elif cb3.isChecked() and cb3.text() == "State":
                gosterilenAralik.append(3)
            elif cb3.isChecked() and cb3.text() == "Zip Code":
                gosterilenAralik.append(4)
            elif cb3.isChecked() and cb3.text() == "Complaint ID":
                gosterilenAralik.append(5)

        if self.ui.threadCount.text():
            exampledict["threadCount"] = self.ui.threadCount.text()
        if self.ui.CompID.text():
            exampledict["complaint_id"] = self.ui.CompID.text()
        if (len(gosterilenAralik) > 0):
            gosterilenAralik.sort()
            exampledict["C1"] = gosterilenAralik[0]
            exampledict["C2"] = gosterilenAralik[len(gosterilenAralik) - 1]
        else:
            exampledict["C1"] = 0
            exampledict["C2"] = 5
        
        if (len(arananAralik) > 0):
            arananAralik.sort()
            exampledict["C3"] = arananAralik[0]
            exampledict["C4"] = arananAralik[len(arananAralik) - 1]
        else:
            exampledict["C3"] = 0
            exampledict["C4"] = 5

        print(exampledict)
        DATA, Process_Time, line, total_time = myThread.start_find(exampledict.get("C1"), exampledict.get("C2"), exampledict.get("C3"), exampledict.get("C4"),exampledict.get("SameProduct"), exampledict.get("match"), exampledict.get("complaint_id"), exampledict.get("threadCount"))
        removeChildFile.removeFile()
        self.loadProducts(DATA, exampledict.get("C1"), exampledict.get("C2"), Process_Time, total_time)

        
def	app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
