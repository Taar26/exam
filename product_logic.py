import product
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys
import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="morgushko"
)
mycursor = mydb.cursor()



class Graph(QtWidgets.QMainWindow, QApplication, QTableWidget, QTableWidgetItem,product.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.resseting)
        self.pushButton_3.clicked.connect(self.delete)
        count = 0
        mycursor.execute(" SELECT * FROM Products LIMIT 5")
        for i in mycursor:
            self.tableWidget.insertRow(count)
            self.tableWidget.setItem(count,0, QtWidgets.QTableWidgetItem(i[2]))
            self.tableWidget.setItem(count,1, QtWidgets.QTableWidgetItem(i[3]))
            self.tableWidget.setItem(count,2, QtWidgets.QTableWidgetItem(i[4]))
            self.tableWidget.setItem(count,3, QtWidgets.QTableWidgetItem(str(i[5])))
            self.tableWidget.setItem(count,4, QtWidgets.QTableWidgetItem(str(i[6])))
            self.tableWidget.setItem(count,5, QtWidgets.QTableWidgetItem(str(i[7])))
            self.tableWidget.setItem(count,6, QtWidgets.QTableWidgetItem(str(i[8])))
            self.tableWidget.setItem(count,7, QtWidgets.QTableWidgetItem(str(i[9])))
            self.tableWidget.setItem(count,8, QtWidgets.QTableWidgetItem(str(i[10])))
            count +=1
        # for row in range(5):
        #     for col in range(3):
        #         item = QTableWidgetItem(f"row {row}, col {col}")
        #         self.setItem(row, col, item)
        # self.cellClicked.connect(self.on_cell_clicked)

    # def on_cell_clicked(self, row, column):
    #     print(f"Clicked row {row}")
    #     # Здесь можно сохранить номер выделенной строки в переменную

    def insert(self):
        sql = "INSERT INTO Products (Наименование, Тип_продукта, Описание, Изображение, Размер_упаковки, Вес_без_упаковки, Вес_c_упаковки, Сертификат_качества, Номер_качества) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (self.lineEdit.text(), self.comboBox.currentText(), self.plainTextEdit.toPlainText(), "-", str(self.spinBox_2.value()) + "x" + str(self.spinBox_3.value()) + "x" + str(self.spinBox_4.value()), self.spinBox_5.value(), self.spinBox_6.value(), "-", self.lineEdit_2.text())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    def resseting(self):
        sql = "UPDATE Products SET Наименование =  %s, Тип_продукта = %s, Описание = %s, Изображение = %s, Размер_упаковки = %s, Вес_без_упаковки = %s, Вес_c_упаковки = %s, Сертификат_качества = %s, Номер_качества = %s WHERE Код_материала = " + str(self.tableWidget.selectionModel().selectedIndexes())
        val = (self.lineEdit.text(), self.comboBox.currentText(), self.plainTextEdit.toPlainText(), "-", str(self.spinBox_2.value()) + "x" + str(self.spinBox_3.value()) + "x" + str(self.spinBox_4.value()), self.spinBox_5.value(), self.spinBox_6.value(), "-", self.lineEdit_2.text())
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    def delete(self):
        print("Удалить")

    
def main():
    app = QtWidgets.QApplication(sys.argv)
    Window = Graph()
    Window.show()
    app.exec_()
if __name__  == "__main__":
    main()