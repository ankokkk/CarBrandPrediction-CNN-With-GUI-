# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:30:15 2021

@author: utku
"""

from car_predict import Ui_Carpred
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog,QMessageBox,QProgressBar
from PyQt5.QtCore import QTime,Qt,QDate,QTimer
from PyQt5.QtGui import QPixmap
import os

class PredWindow(QtWidgets.QMainWindow,Ui_Carpred):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.path = " "
        self.st = 0
        self.bar = 0
        
        self.actionRemove.triggered.connect(self.Remove)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionExit_2.triggered.connect(self.exitFile)
        self.actionTime.triggered.connect(self.showTime)
        self.actionDate.triggered.connect(self.showDate)
        self.actionAbout.triggered.connect(self.showHelp)
        self.actionBrands.triggered.connect(self.showBrands)
        self.pushButton_2.clicked.connect(self.LoadImage)
        self.pushButton.clicked.connect(self.predict)
        self.actionAdd_Image.triggered.connect(self.LoadImage)
        
        self.bar = 0
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(0)
        timer = QTimer(self)
        timer.timeout.connect(self.step)
        timer.start(1000) 
        
        self.show() 
        
    def step(self):
        if self.bar == 1:
            self.progressBar.setValue(self.progressBar.value() + 20)
        
    def Remove(self):
        self.textEdit.clear()
        self.st = 0
        
    def openFile(self):
        filename = QFileDialog.getOpenFileName(self,"Open File",os.getenv("HOME"))
        
        if filename[0]:
            f = open(filename[0],"r+")
        
            with f:
                data = f.read()
                
                self.textBrowser.setText(data)
                
    def saveFile(self):
        filename = QFileDialog.getSaveFileName(self,"Save File",os.getenv("HOME"))
        
        with open(filename[0],"w") as f:
            text = self.textBrowser.toPlainText()
            f.write(text)
            QMessageBox.about(self,"Save File","File Saved Successfully!")
    
    def exitFile(self):
        self.close()
        
    def showTime(self):
        time = QTime.currentTime()
        self.textBrowser.setText(time.toString(Qt.DefaultLocaleLongDate))
        
    def showDate(self):
        date = QDate.currentDate()
        self.textBrowser.setText(date.toString(Qt.DefaultLocaleLongDate))
     
    def showHelp(self):
        self.textBrowser.setText("This program predicts the car brand, model and year. It makes estimates among 48 brands and 271 models (based on the years 2008-2021).")
    
    def showBrands(self):
        self.textBrowser.setText("Brands:Alfa Romeo,Aston Martin,Audi,BMW,Bentley,Bugatti,Cadillac,Chevrolet,Chrysler,Citroen,Dacia,Dodge,Ferrari,Fiat,Ford,Honda,Hyundai,Infiniti,Jaguar,Jeep,Kia,Koenigsegg,Lamborghini,Land Rover,Lexus,Lincoln,Lotus,Maserati,Mazda,McLaren,Mercedes,Mini,Mitsubishi,Nissan,Opel,Pagani,Peugeot,Porsche,Renault,Rolls,Royce,Seat,Skoda,Ssangyong,Subaru,Tesla,Toyota,Volkswagen,Volvo ")
        
    def LoadImage(self):
        imagename = QFileDialog.getOpenFileName(self,"Open File","c\\","Image files (*.jpg *)")
        imagepath = imagename[0]
        pixmap = QPixmap(imagepath)
        pixmap = pixmap.scaled(370,360,Qt.KeepAspectRatio)
        self.label.setPixmap(QPixmap(pixmap))
        self.st = 1
        self.textBrowser.clear()
        self.path = imagepath
     
    def predict(self):
        
        if self.st == 0:
            self.textBrowser.setText("Please load image!")
             
        else:
            self.bar = 1
            from project import prediction
            model5, year3_name, brand5, brand5_name, year3, model5_name = prediction(self.path)
            
            self.textBrowser_3.setText("1. "+str(brand5_name[0])+" (%"+str(brand5[0])+")\n\n "+str(model5_name[0][0])+" (%"+str(model5[0][0])+")\n "
                                      +str(model5_name[0][1])+" (%"+str(model5[0][1])+")\n "+str(model5_name[0][2])+" (%"+str(model5[0][2])+")\n "
                                      +str(model5_name[0][3])+" (%"+str(model5[0][3])+")\n "+str(model5_name[0][4])+" (%"+str(model5[0][4])+")\n "
                                      +"\n\nEstimated year:\n "+str(year3_name[0])+" (%"+str(year3[0])+")\n "+str(year3_name[1])+" (%"+str(year3[1])+")\n "
                                      +str(year3_name[2])+" (%"+str(year3[2])+")")
             
            self.textBrowser_4.setText("2. "+str(brand5_name[1])+" (%"+str(brand5[1])+")\n\n "+str(model5_name[1][0])+" (%"+str(model5[1][0])+")\n "
                                      +str(model5_name[1][1])+" (%"+str(model5[1][1])+")\n "+str(model5_name[1][2])+" (%"+str(model5[1][2])+")\n "
                                      +str(model5_name[1][3])+" (%"+str(model5[1][3])+")\n "+str(model5_name[1][4])+" (%"+str(model5[1][4])+")\n ")
            
            self.textBrowser_5.setText("3. "+str(brand5_name[2])+" (%"+str(brand5[2])+")\n\n "+str(model5_name[2][0])+" (%"+str(model5[2][0])+")\n "
                                      +str(model5_name[2][1])+" (%"+str(model5[2][1])+")\n "+str(model5_name[2][2])+" (%"+str(model5[2][2])+")\n "
                                      +str(model5_name[2][3])+" (%"+str(model5[2][3])+")\n "+str(model5_name[2][4])+" (%"+str(model5[2][4])+")\n ")
          
            self.textBrowser_6.setText("4. "+str(brand5_name[3])+" (%"+str(brand5[3])+")\n\n "+str(model5_name[3][0])+" (%"+str(model5[3][0])+")\n "
                                      +str(model5_name[3][1])+" (%"+str(model5[3][1])+")\n "+str(model5_name[3][2])+" (%"+str(model5[3][2])+")\n "
                                      +str(model5_name[3][3])+" (%"+str(model5[3][3])+")\n "+str(model5_name[3][4])+" (%"+str(model5[3][4])+")\n ")
           
            self.textBrowser_7.setText("5. "+str(brand5_name[4])+" (%"+str(brand5[4])+")\n\n "+str(model5_name[4][0])+" (%"+str(model5[4][0])+")\n "
                                      +str(model5_name[4][1])+" (%"+str(model5[4][1])+")\n "+str(model5_name[4][2])+" (%"+str(model5[4][2])+")\n "
                                      +str(model5_name[4][3])+" (%"+str(model5[4][3])+")\n "+str(model5_name[4][4])+" (%"+str(model5[4][4])+")\n ")
               
            self.progressBar.setValue(100)  
        

    
    
    