import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget
from gui import Ui_Form
from resultWindow import Ui_resultWindow
from dataWindow import Ui_dataWindow
import zipfile
import threading
import glob
import shutil
import os
import numpy as np
import algorithm as ahp
import csv
 
class GuiProgram(Ui_Form):
    def __init__(self, dialog):
        Ui_Form.__init__(self)
        self.setupUi(dialog)
        pixmap = QtGui.QPixmap("obrazki\\zdj4.jpg")
        self.label_pic1.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\zdj3.png")
        self.label_pic2.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\zdj1.png")
        self.label1.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\zdj2.png")
        self.label2.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis1.png")
        self.opis1.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis2.png")
        self.opis2.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis3.png")
        self.opis3.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis4.png")
        self.opis4.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis5.png")
        self.opis5.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis6.png")
        self.opis6.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis7.png")
        self.opis7.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis8.png")
        self.opis8.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis9.png")
        self.opis9.setPixmap(pixmap)
        pixmap = QtGui.QPixmap("obrazki\\opis10.png")
        self.opis10.setPixmap(pixmap)

        #------------------------------------------------------------------
        #Test działania slidera
    
        self.button1.clicked.connect(self.button1Fun)
        self.button2.clicked.connect(self.openDataWindow)
    def button1Fun(self):
        ahp_obj = ahp.algorithm(prog.horizontalSlider1.value(), 
                                prog.horizontalSlider2.value(), 
                                prog.horizontalSlider3.value(), 
                                prog.horizontalSlider4.value(), 
                                prog.horizontalSlider5.value(), 
                                prog.horizontalSlider6.value(), 
                                prog.horizontalSlider7.value(), 
                                prog.horizontalSlider8.value(), 
                                prog.horizontalSlider9.value(), 
                                prog.horizontalSlider10.value())
        self.resultWindow=QtWidgets.QWidget()
        self.ui = ui = Ui_resultWindow()
        self.ui.setupUi(self.resultWindow)
        self.resultWindow.show()
        self.ui.label.setText(ahp_obj.oblicz())
        #-----------------------------------------------------------------
    def button11Fun(self):
        self.ui.label.setText("Masa ziarna:")
        _translate = QtCore.QCoreApplication.translate
        with open('macierz1.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            x=1
            for row in csvreader:
                if(x==1):
                    self.ui.pushButtonx11.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx12.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx13.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx14.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx15.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx16.setText(_translate("Form", row[5]))
                if(x==2):
                    self.ui.pushButtonx21.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx22.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx23.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx24.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx25.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx26.setText(_translate("Form", row[5]))
                if(x==3):
                    self.ui.pushButtonx31.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx32.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx33.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx34.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx35.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx36.setText(_translate("Form", row[5]))
                if(x==4):
                    self.ui.pushButtonx41.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx42.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx43.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx44.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx45.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx46.setText(_translate("Form", row[5]))
                if(x==5):
                    self.ui.pushButtonx51.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx52.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx53.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx54.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx55.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx56.setText(_translate("Form", row[5]))
                if(x==6):
                    self.ui.pushButtonx61.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx62.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx63.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx64.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx65.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx66.setText(_translate("Form", row[5]))
                x=x+1

    def button22Fun(self):
        self.ui.label.setText("Wydajność mąki:")
        _translate = QtCore.QCoreApplication.translate
        with open('macierz2.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            x=1
            for row in csvreader:
                if(x==1):
                    self.ui.pushButtonx11.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx12.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx13.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx14.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx15.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx16.setText(_translate("Form", row[5]))
                if(x==2):
                    self.ui.pushButtonx21.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx22.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx23.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx24.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx25.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx26.setText(_translate("Form", row[5]))
                if(x==3):
                    self.ui.pushButtonx31.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx32.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx33.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx34.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx35.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx36.setText(_translate("Form", row[5]))
                if(x==4):
                    self.ui.pushButtonx41.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx42.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx43.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx44.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx45.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx46.setText(_translate("Form", row[5]))
                if(x==5):
                    self.ui.pushButtonx51.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx52.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx53.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx54.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx55.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx56.setText(_translate("Form", row[5]))
                if(x==6):
                    self.ui.pushButtonx61.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx62.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx63.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx64.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx65.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx66.setText(_translate("Form", row[5]))
                x=x+1
    def button33Fun(self):
        self.ui.label.setText("Tolerancja na zakwaszenie:")
        _translate = QtCore.QCoreApplication.translate
        with open('macierz3.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            x=1
            for row in csvreader:
                if(x==1):
                    self.ui.pushButtonx11.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx12.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx13.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx14.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx15.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx16.setText(_translate("Form", row[5]))
                if(x==2):
                    self.ui.pushButtonx21.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx22.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx23.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx24.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx25.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx26.setText(_translate("Form", row[5]))
                if(x==3):
                    self.ui.pushButtonx31.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx32.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx33.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx34.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx35.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx36.setText(_translate("Form", row[5]))
                if(x==4):
                    self.ui.pushButtonx41.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx42.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx43.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx44.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx45.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx46.setText(_translate("Form", row[5]))
                if(x==5):
                    self.ui.pushButtonx51.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx52.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx53.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx54.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx55.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx56.setText(_translate("Form", row[5]))
                if(x==6):
                    self.ui.pushButtonx61.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx62.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx63.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx64.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx65.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx66.setText(_translate("Form", row[5]))
                x=x+1
    def button44Fun(self):
        self.ui.label.setText("Odporność na choroby:")
        _translate = QtCore.QCoreApplication.translate
        with open('macierz4.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            x=1
            for row in csvreader:
                if(x==1):
                    self.ui.pushButtonx11.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx12.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx13.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx14.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx15.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx16.setText(_translate("Form", row[5]))
                if(x==2):
                    self.ui.pushButtonx21.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx22.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx23.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx24.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx25.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx26.setText(_translate("Form", row[5]))
                if(x==3):
                    self.ui.pushButtonx31.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx32.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx33.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx34.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx35.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx36.setText(_translate("Form", row[5]))
                if(x==4):
                    self.ui.pushButtonx41.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx42.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx43.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx44.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx45.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx46.setText(_translate("Form", row[5]))
                if(x==5):
                    self.ui.pushButtonx51.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx52.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx53.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx54.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx55.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx56.setText(_translate("Form", row[5]))
                if(x==6):
                    self.ui.pushButtonx61.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx62.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx63.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx64.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx65.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx66.setText(_translate("Form", row[5]))
                x=x+1
    def button55Fun(self):
        self.ui.label.setText("Tolerancja na temperature:")
        _translate = QtCore.QCoreApplication.translate
        with open('macierz5.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=';')
            x=1
            for row in csvreader:
                if(x==1):
                    self.ui.pushButtonx11.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx12.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx13.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx14.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx15.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx16.setText(_translate("Form", row[5]))
                if(x==2):
                    self.ui.pushButtonx21.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx22.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx23.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx24.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx25.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx26.setText(_translate("Form", row[5]))
                if(x==3):
                    self.ui.pushButtonx31.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx32.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx33.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx34.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx35.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx36.setText(_translate("Form", row[5]))
                if(x==4):
                    self.ui.pushButtonx41.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx42.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx43.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx44.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx45.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx46.setText(_translate("Form", row[5]))
                if(x==5):
                    self.ui.pushButtonx51.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx52.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx53.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx54.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx55.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx56.setText(_translate("Form", row[5]))
                if(x==6):
                    self.ui.pushButtonx61.setText(_translate("Form", row[0]))
                    self.ui.pushButtonx62.setText(_translate("Form", row[1]))
                    self.ui.pushButtonx63.setText(_translate("Form", row[2]))
                    self.ui.pushButtonx64.setText(_translate("Form", row[3]))
                    self.ui.pushButtonx65.setText(_translate("Form", row[4]))
                    self.ui.pushButtonx66.setText(_translate("Form", row[5]))
                x=x+1
                
    def openDataWindow(self):
        self.dataWindow=QtWidgets.QWidget()
        self.ui = ui = Ui_dataWindow()
        self.ui.setupUi(self.dataWindow)
        self.dataWindow.show()
        self.ui.pushButton11.clicked.connect(self.button11Fun)
        self.ui.pushButton22.clicked.connect(self.button22Fun)
        self.ui.pushButton33.clicked.connect(self.button33Fun)
        self.ui.pushButton44.clicked.connect(self.button44Fun)
        self.ui.pushButton55.clicked.connect(self.button55Fun)
        
        
     
        
        
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QMainWindow()
    prog = GuiProgram(dialog)
    dialog.show()
    sys.exit(app.exec_())