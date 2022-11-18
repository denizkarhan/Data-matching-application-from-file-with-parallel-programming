from PyQt5 import QtWidgets
from MainForm import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem
import sys, os, myThread, removeChildFile

class Window(QtWidgets.QMainWindow):
    def __init__(self, 	products = [ {'Product': 'FLAG', 'Issue': 'Communication tactics', 'Company': 'CURO'}, {'Product': 'Student Loan', 'Issue': 'Struggling repay loan', 'Company': 'Student Loan Direct'}, {'Product': 'Mortgage', 'Issue': 'Closing Mortgage', 'Company': 'Statebridge Company'},], C1 = 0, C2 = 2):
        super(Window, self). __init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadProducts(products, C1, C2)
        self.ui.Filtrele.clicked.connect(self.filtre)

    def loadProducts(self, products, C1, C2):
        NAME = ['Product','Issue','Company', 'State', 'Complaint ID', 'Zip Code']
        self.ui.table.setRowCount(len(products))
        self.ui.table.setColumnCount(len(products[0]))
        self.ui.table.setHorizontalHeaderLabels(NAME[C1:C2+1])

        for i in range(len(products)):
            self.ui.table.setColumnWidth(i,150)

        rowIndex = 0
        for product in products:
            for i in range(C1, C2 + 1):
                self.ui.table.setItem(rowIndex, i, QTableWidgetItem(product[NAME[i]]))
            rowIndex += 1

    def show_state(self,value):
        cb = self.sender()
        print(value)
        print(cb.text())
        print(cb.isChecked())

    def filtre(self):
        exampledict = {"C1":0, "C2":5, "SameProduct": -1, "match" : 0, "complaint_id":-1, "threadCount": 10}
        result = ''
        items = self.ui.groupOran.findChildren(QtWidgets.QRadioButton)
        for cb in items:
            if cb.isChecked() and cb.text() == "Hepsi":
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 10 ve Üzeri":
                exampledict["match"] = 10
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 20 ve Üzeri":
                exampledict["match"] = 20
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 30 ve Üzeri":
                exampledict["match"] = 30
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 40 ve Üzeri":
                exampledict["match"] = 40
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 50 ve Üzeri":
                exampledict["match"] = 50
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 60 ve Üzeri":
                exampledict["match"] = 60
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 70 ve Üzeri":
                exampledict["match"] = 70
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 80 ve Üzeri":
                exampledict["match"] = 80
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 90 ve Üzeri":
                exampledict["match"] = 90
                result += cb.text() + '\n'
            elif cb.isChecked() and cb.text() == "% 100":
                exampledict["match"] = 100
                result += cb.text() + '\n'
 
        items1 = self.ui.groupRows.findChildren(QtWidgets.QCheckBox)
        for cb1 in items1:
            if cb1.isChecked() and cb1.text() == "Hepsi":
                exampledict["SameProduct"] = -1
                result += cb1.text() + '\n'
            elif cb1.isChecked() and cb1.text() == "Product":
                exampledict["SameProduct"] = 0
                result += cb1.text() + '\n'
            elif cb1.isChecked() and cb1.text() == "Issue":
                exampledict["SameProduct"] = 1
                result += cb1.text() + '\n'
            elif cb1.isChecked() and cb1.text() == "Company":
                exampledict["SameProduct"] = 2
                result += cb1.text() + '\n'
            elif cb1.isChecked() and cb1.text() == "State":
                exampledict["SameProduct"] = 3
                result += cb1.text() + '\n'
            elif cb1.isChecked() and cb1.text() == "Complaint ID":
                exampledict["SameProduct"] = 4
                result += cb1.text() + '\n'
            elif cb1.isChecked() and cb1.text() == "Zip Code":
                exampledict["SameProduct"] = 5
                result += cb1.text() + '\n'

        items2 = self.ui.groupRows2.findChildren(QtWidgets.QCheckBox)
        gosterilenAralik = []
        for cb2 in items2:
            if cb2.isChecked() and cb2.text() == "Hepsi":
                gosterilenAralik = [0,1,2,3,4,5]
                result += cb2.text() + '\n'
            elif cb2.isChecked() and cb2.text() == "Product":
                gosterilenAralik.append(0)
                result += cb2.text() + '\n'
            elif cb2.isChecked() and cb2.text() == "Issue":
                gosterilenAralik.append(1)
                result += cb2.text() + '\n'
            elif cb2.isChecked() and cb2.text() == "Company":
                gosterilenAralik.append(2)
                result += cb2.text() + '\n'
            elif cb2.isChecked() and cb2.text() == "State":
                gosterilenAralik.append(3)
                result += cb2.text() + '\n'
            elif cb2.isChecked() and cb2.text() == "Complaint ID":
                gosterilenAralik.append(4)
                result += cb2.text() + '\n'
            elif cb2.isChecked() and cb2.text() == "Zip Code":
                gosterilenAralik.append(5)
                result += cb2.text() + '\n'

        self.ui.label.setText(result)
        if self.ui.threadCount.text():
            exampledict["threadCount"] = self.ui.threadCount.text()
        if self.ui.CompID.text():
            exampledict["complaint_id"] = self.ui.CompID.text()
        if (len(gosterilenAralik)):
            gosterilenAralik.sort()
            exampledict["C1"] = gosterilenAralik[0]
            exampledict["C2"] = gosterilenAralik[-1]
        print(exampledict)
        DATA = myThread.start_find(exampledict.get("C1"), exampledict.get("C2"), exampledict.get("SameProduct"), exampledict.get("match"), exampledict.get("complaint_id"), exampledict.get("threadCount"))
        removeChildFile.removeFile()
        self.loadProducts(DATA, gosterilenAralik[0], gosterilenAralik[-1])

def	app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()
