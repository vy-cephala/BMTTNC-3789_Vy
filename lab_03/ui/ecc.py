# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "../platforms"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 290, 91, 21))
        self.label_3.setObjectName("label_3")
        self.txtplaintext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtplaintext.setGeometry(QtCore.QRect(130, 100, 561, 131))
        self.txtplaintext.setObjectName("txtplaintext")
        self.txtcptext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txtcptext.setGeometry(QtCore.QRect(130, 280, 561, 131))
        self.txtcptext.setObjectName("txtcptext")
        self.btnsign = QtWidgets.QPushButton(self.centralwidget)
        self.btnsign.setGeometry(QtCore.QRect(150, 440, 93, 28))
        self.btnsign.setObjectName("btnsign")
        self.btnverify = QtWidgets.QPushButton(self.centralwidget)
        self.btnverify.setGeometry(QtCore.QRect(500, 440, 93, 28))
        self.btnverify.setObjectName("btnverify")
        self.btngenerate = QtWidgets.QPushButton(self.centralwidget)
        self.btngenerate.setGeometry(QtCore.QRect(450, 20, 93, 28))
        self.btngenerate.setObjectName("btngenerate")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label.setText(_translate("MainWindow", "ECC CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Information:"))
        self.label_3.setText(_translate("MainWindow", "Signature:"))
        self.btnsign.setText(_translate("MainWindow", "Sign"))
        self.btnverify.setText(_translate("MainWindow", "Verify"))
        self.btngenerate.setText(_translate("MainWindow", "Generate keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
