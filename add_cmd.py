# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_cmd.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import json,sys,os


filePath = "config.json"


class Ui_SecondWindow(object):
    server_name, env = "",""
    def setupUi(self, MainWindow, env, server_name):
        self.server_name = server_name
        self.env = env
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(336, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tag_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.tag_lineEdit.setGeometry(QtCore.QRect(80, 50, 191, 21))
        self.tag_lineEdit.setObjectName("tag_lineEdit")
        self.cmd_textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.cmd_textEdit.setGeometry(QtCore.QRect(80, 90, 241, 161))
        self.cmd_textEdit.setObjectName("cmd_textEdit")
        self.tag_label = QtWidgets.QLabel(self.centralwidget)
        self.tag_label.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.tag_label.setObjectName("tag_label")
        self.cmd_label = QtWidgets.QLabel(self.centralwidget)
        self.cmd_label.setGeometry(QtCore.QRect(20, 100, 61, 16))
        self.cmd_label.setObjectName("cmd_label")
        self.execute_btn = QtWidgets.QPushButton(self.centralwidget)
        self.execute_btn.setGeometry(QtCore.QRect(80, 260, 75, 23))
        self.execute_btn.setObjectName("execute_btn")
        self.execute_btn.clicked.connect(self.execute_cmd)
        
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(170, 260, 75, 23))
        self.cancel_btn.setObjectName("cancel_btn")
        self.cancel_btn.clicked.connect(lambda:MainWindow.destroy())
        # self.cancel_btn.hide()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Custom Commands"))
        MainWindow.setWindowFlags(MainWindow.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.tag_label.setText(_translate("MainWindow", "Tag:"))
        self.cmd_label.setText(_translate("MainWindow", "Command:"))
        self.execute_btn.setText(_translate("MainWindow", "Execute"))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel"))     
        
    def execute_cmd(self):
        tag = self.tag_lineEdit.text()
        cmd_text = self.cmd_textEdit.toPlainText()
        
        with open(filePath,"r") as fp:
                information = json.load(fp)
                cmnds = information[self.env][self.server_name]['commands']
                print(cmnds)
                cmnds.update({tag : [cmd_text]})
            
        with open(filePath, 'w') as fp:
                json.dump(information, fp, indent=4)
        self.tag_lineEdit.setText("")
        self.cmd_textEdit.setText("")

        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
