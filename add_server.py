# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json,os,sys
filePath = "config.json"

class Ui_AddServerWindow(object):
    env = ""
    def setupUi(self, MainWindow, env):
        self.env = env
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 360)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(20, 10, 351, 31))
        self.title_label.setObjectName("title_label")
        self.title_label.setStyleSheet('font-size:16px')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 261, 16))
        self.label.setObjectName("label")
        self.label.setStyleSheet('font-size:14px')
        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setGeometry(QtCore.QRect(20, 100, 81, 16))
        self.ip_label.setObjectName("ip_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(20, 220, 61, 16))
        self.pass_label.setObjectName("pass_label")
        self.user_label = QtWidgets.QLabel(self.centralwidget)
        self.user_label.setGeometry(QtCore.QRect(20, 180, 51, 16))
        self.user_label.setObjectName("user_label")
        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setGeometry(QtCore.QRect(20, 140, 71, 16))
        self.port_label.setObjectName("port_label")
        self.status_label = QtWidgets.QLabel(self.centralwidget)
        self.status_label.setGeometry(QtCore.QRect(120, 290, 191, 16))
        self.status_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setObjectName("status_label")
        
        self.ip_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_lineEdit.setGeometry(QtCore.QRect(170, 100, 181, 20))
        self.ip_lineEdit.setObjectName("ip_lineEdit")
        self.port_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.port_lineEdit.setGeometry(QtCore.QRect(170, 140, 181, 20))
        self.port_lineEdit.setObjectName("port_lineEdit")
        self.user_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.user_lineEdit.setGeometry(QtCore.QRect(170, 180, 181, 20))
        self.user_lineEdit.setObjectName("user_lineEdit")
        self.pass_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_lineEdit.setGeometry(QtCore.QRect(170, 220, 181, 20))
        self.pass_lineEdit.setObjectName("pass_lineEdit")
        self.flag_label = QtWidgets.QLabel(self.centralwidget)
        self.flag_label.setGeometry(QtCore.QRect(0, 300, 401, 16))
        self.flag_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.flag_label.setAlignment(QtCore.Qt.AlignCenter)
        self.flag_label.setObjectName("flag_label")
        
        
        
        self.cred_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cred_btn.setGeometry(QtCore.QRect(170, 260, 75, 23))
        self.cred_btn.setObjectName("cred_btn")
        self.cred_btn.clicked.connect(self.onSubmitClicked)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
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
        
        self.title_label.setText(_translate("MainWindow", "Add New Server For "))
        self.label.setText(_translate("MainWindow", "Server Credentials"))
        self.ip_label.setText(_translate("MainWindow", "Server\'s IP:"))
        self.pass_label.setText(_translate("MainWindow", "Password:"))
        self.user_label.setText(_translate("MainWindow", "User:"))
        self.port_label.setText(_translate("MainWindow", "Port:"))
        self.cred_btn.setText(_translate("MainWindow", "Submit"))
  
    def onSubmitClicked(self):
        ip = self.ip_lineEdit.text()
        port = int(self.port_lineEdit.text())
        user = self.user_lineEdit.text()
        password = self.pass_lineEdit.text()
        cred =[ip,port,user,password]
        
        data = {ip : {"creds": cred, "commands":{}}}
        print(self.env)
        # print(data)
        with open(filePath,"r") as fp:
                information = json.load(fp)
                cmnds = information[self.env]
                print(cmnds)
                cmnds.update(data)
            
        with open(filePath, 'w') as fp:
                json.dump(information, fp, indent=4)
        
        self.isInsertedSuccessfully()
        
    def isInsertedSuccessfully(self):
        ip = self.ip_lineEdit.text()
        f = open("config.json")
        data = json.load(f)
        x = []
        is_inserted = False
        for index, item in data[self.env].items():
           
            if index == ip :
                 self.flag_label.setText("Data inserted successfully!")
                 self.flag_label.setStyleSheet("color: green;")
                 self.ip_lineEdit.clear()
                 self.port_lineEdit.clear()
                 self.user_lineEdit.clear()
                 self.pass_lineEdit.clear()
                 is_inserted = True
        
        if is_inserted == False :
            self.flag_label.setText("Data insertion failed")
            self.flag_label.setStyleSheet("color: red;")
        
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
