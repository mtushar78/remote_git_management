# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gii_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from typing import List
from add_cmd import Ui_SecondWindow
from add_server import Ui_AddServerWindow
import git 
server_1 = git.RemoteCon()
global flag
import json


class Ui_MainWindow(object):
    flag=1
    env_index=""
    cred_index = ""
    configs={}
    
    def __init__(self):
        self.flag=0
        self.load_json_config()
    def load_json_config(self):
        f = open("config.json")
        self.configs = json.load(f)
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(481, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.env_list = QtWidgets.QComboBox(self.centralwidget)
        self.env_list.setGeometry(QtCore.QRect(100, 40, 169, 20))
        self.env_list.setObjectName("env_list")
        self.env_list.addItems(self.dropDownENV())
        self.env_list.currentIndexChanged.connect(self.onIndexChanged_ENV)
        
        self.serverList = QtWidgets.QComboBox(self.centralwidget)
        self.serverList.setGeometry(QtCore.QRect(100, 80, 169, 20))
        self.serverList.setObjectName("serverList")
        self.serverList.addItems(self.dropDownSERVER()) #calling dropDown method
        
        self.commandList = QtWidgets.QComboBox(self.centralwidget)
        self.commandList.setGeometry(QtCore.QRect(100, 130, 169, 20))
        self.commandList.setObjectName("commandList")
        
        
        self.textEdit = QtWidgets.QTextBrowser(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(1, 200, 479, 271))
        self.textEdit.setObjectName("textEdit")
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setGeometry(QtCore.QRect(100, 170, 171, 23))
        self.runButton.setObjectName("runButton")
        self.runButton.setEnabled(False)
        
        self.addCommandBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addCommandBtn.setGeometry(QtCore.QRect(300, 130, 151, 23))
        self.addCommandBtn.setObjectName("addCommandBtn")
        self.addCommandBtn.clicked.connect(self.newWindow)
        self.addCommandBtn.setEnabled(False)
        
        self.check_con = QtWidgets.QPushButton(self.centralwidget)
        self.check_con.setGeometry(QtCore.QRect(300, 80, 71, 23))
        self.check_con.setObjectName("check_con")
        self.check_con.clicked.connect(self.connect)
        
        self.add_new_connection = QtWidgets.QPushButton(self.centralwidget)
        self.add_new_connection.setGeometry(QtCore.QRect(380, 80, 71, 23))
        self.add_new_connection.setObjectName("add_new_connection")
        self.add_new_connection.clicked.connect(self.addNewconnection)
        
        self.reload = QtWidgets.QPushButton(self.centralwidget)
        self.reload.setGeometry(QtCore.QRect(300, 170, 151, 23))
        self.reload.setObjectName("reload")
        self.reload.clicked.connect(self.reload_func)
        
        self.server_label = QtWidgets.QLabel(self.centralwidget)
        self.server_label.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.server_label.setObjectName("server_label")
        self.command_label = QtWidgets.QLabel(self.centralwidget)
        self.command_label.setGeometry(QtCore.QRect(30, 130, 61, 16))
        self.command_label.setObjectName("command_label")
        self.env_label = QtWidgets.QLabel(self.centralwidget)
        self.env_label.setGeometry(QtCore.QRect(30, 40, 61, 16))
        self.env_label.setObjectName("env_label")
        
        self.con_status = QtWidgets.QLabel(self.centralwidget)
        self.con_status.setGeometry(QtCore.QRect(10, 500, 101, 20))
        self.con_status.setObjectName("con_status")
        
        self.con_label = QtWidgets.QLabel(self.centralwidget)
        self.con_label.setGeometry(QtCore.QRect(120, 500, 251, 16))
        self.con_label.setObjectName("con_label")
        self.con_label.setText("Disconnected")
        self.con_label.setStyleSheet("color: red;")
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.runButton.clicked.connect(self.b1_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SSH Management Tool"))
        MainWindow.setWindowIcon(QtGui.QIcon('logo.jpg'))
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
    
        self.runButton.setText(_translate("MainWindow", "Run"))
        self.env_label.setText(_translate("MainWindow", "Environment:"))
        self.server_label.setText(_translate("MainWindow", "Server:"))
        self.command_label.setText(_translate("MainWindow", "Command:"))
        self.con_status.setText(_translate("MainWindow", "Connection Status:"))
        self.addCommandBtn.setText(_translate("MainWindow", "Add Command"))
        self.check_con.setText(_translate("MainWindow", "Connect"))
        self.add_new_connection.setText(_translate("MainWindow", "Add New"))
        self.reload.setText(_translate("MainWindow", "Reload"))
    def b1_clicked(self): # when RUN button is clicked
        res = self.showResut()
        self.textEdit.setPlainText(res)
    def dropDownENV(self): #ip lists for drow down
        url = []
        for index,item in self.configs.items():
            url.append(index) 
        return url
    def dropDownSERVER(self):  
        selected = self.env_list.currentText()
        url = []
        if selected != '':
            self.serverList.clear()
            for index,item in self.configs[selected].items():
                url.append(index)     
        return url
    
    def onIndexChanged_ENV(self):  
        selected = self.env_list.currentText()
        self.env_index = selected
        if selected != '':
            self.serverList.clear()
            url = []
            for index,item in self.configs[selected].items():
                url.append(index)     
            self.serverList.addItems(url)
    
    def dropDownCommand(self):#ip lists for drow down
        url = []
        if (self.env_index != '' and self.cred_index !=''):
            for index,item in self.configs[self.env_index][self.cred_index]['commands'].items():
                url.append(index) 
            self.commandList.clear()
            self.commandList.addItems(url)
            self.addCommandBtn.setEnabled(True)
            self.runButton.setEnabled(True)
    def listToString(self,s): 
        # initialize an empty string
        str1 = ""       
        # traverse in the string  
        for ele in s: 
            str1 += str(ele)
        # return string  
        return str1
    def showResut(self): #command execution
        selected = self.commandList.currentText()
        command = self.configs[self.env_index][self.cred_index]['commands'][selected]
        s = server_1.execute_commands(command)
        return self.listToString(s)
      
    
    def connect(self):
        # if (self.flag == 0):
        if not server_1.check_connection_status():
            self.env_index = str(self.env_list.currentText())            
            self.cred_index = str(self.serverList.currentText())
            creds = self.configs[self.env_index][self.cred_index]['creds']
            x = server_1.connect(creds)
            if x[0]==1:
                self.dropDownCommand()
                self.con_label.setText(x[1])
                self.con_label.setStyleSheet("color: Green;")
            else:
                self.commandList.clear()
                self.addCommandBtn.setEnabled(False)
                self.runButton.setEnabled(False)
                self.textEdit.setPlainText("")
                self.con_label.setText(x[1])
                self.con_label.setStyleSheet("color: red;")
        else:
            server_1.disconnect()
            self.runButton.setEnabled(False)
            self.addCommandBtn.setEnabled(False)
            self.commandList.clear()
            self.textEdit.setPlainText("")
            self.con_label.setText("Disonnected")
            self.con_label.setStyleSheet("color: red;")
            self.connect()
    def newWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SecondWindow()
        self.ui.setupUi(self.window, self.env_index, self.cred_index)
        self.window.show()
        
    def addNewconnection(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AddServerWindow()
        self.env_index = self.env_list.currentText()
        self.ui.setupUi(self.window, self.env_index)
        self.window.show()
    def reload_func(self):
        self.load_json_config()
        selected = self.env_list.currentText()
        if selected != '':
            self.serverList.clear()
        url = []
        for index,item in self.configs[selected].items():
            url.append(index)  
        self.serverList.addItems(url)
        self.commandList.clear()
        self.textEdit.clear()
        self.addCommandBtn.setEnabled(False)
        self.runButton.setEnabled(False)
        self.disconnect()
    def disconnect(self):
        if server_1.check_connection_status():
            server_1.disconnect()
        
        self.con_label.setText("Disconnected")
        self.con_label.setStyleSheet("color: red;")
        
        
    
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
