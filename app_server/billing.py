# Form implementation generated from reading ui file 'Billing.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 399)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Perpetua")
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(17, 131, 112);\n"
"border-radius: 5px;")
        self.label.setObjectName("label")
        self.error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(110, 170, 351, 16))
        font = QtGui.QFont()
        font.setBold(False)
        self.error_label.setFont(font)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setText("")
        self.error_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 140, 551, 141))
        self.groupBox.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(17, 131, 112);\n"
"border-radius: 5px;")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 20, 91, 101))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 91, 101))
        self.pushButton.setToolTip("")
        icon = QtGui.QIcon.fromTheme("folder")
        self.pushButton.setIcon(icon)
        self.pushButton.setObjectName("pushButton")
        self.outputFileBox = QtWidgets.QGroupBox(parent=self.groupBox)
        self.outputFileBox.setGeometry(QtCore.QRect(110, 70, 331, 51))
        self.outputFileBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.outputFileBox.setObjectName("outputFileBox")
        self.outputFileText = QtWidgets.QPlainTextEdit(parent=self.outputFileBox)
        self.outputFileText.setEnabled(True)
        self.outputFileText.setGeometry(QtCore.QRect(10, 15, 311, 31))
        self.outputFileText.setObjectName("outputFileText")
        self.fileInputBox = QtWidgets.QGroupBox(parent=self.groupBox)
        self.fileInputBox.setGeometry(QtCore.QRect(110, 20, 331, 51))
        self.fileInputBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fileInputBox.setObjectName("fileInputBox")
        self.inputFileText = QtWidgets.QPlainTextEdit(parent=self.fileInputBox)
        self.inputFileText.setEnabled(True)
        self.inputFileText.setGeometry(QtCore.QRect(10, 15, 311, 31))
        self.inputFileText.setReadOnly(False)
        self.inputFileText.setObjectName("inputFileText")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 50, 551, 80))
        self.groupBox_2.setStyleSheet("border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(17, 131, 112);\n"
"border-radius: 5px;")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.categoryInput = QtWidgets.QPlainTextEdit(parent=self.groupBox_2)
        self.categoryInput.setEnabled(True)
        self.categoryInput.setGeometry(QtCore.QRect(10, 30, 381, 31))
        self.categoryInput.setReadOnly(False)
        self.categoryInput.setObjectName("categoryInput")
        self.selectButton = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.selectButton.setGeometry(QtCore.QRect(400, 30, 141, 31))
        self.selectButton.setObjectName("selectButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please enter raw attendace file to generate Attendancec Billing Report"))
        self.pushButton_2.setText(_translate("MainWindow", "Generate"))
        self.pushButton.setText(_translate("MainWindow", "Upload"))
        self.outputFileBox.setTitle(_translate("MainWindow", "Enter Ouput File name"))
        self.outputFileText.setPlainText(_translate("MainWindow", "Sample.xlsx"))
        self.fileInputBox.setTitle(_translate("MainWindow", "File Input"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Upload a category file to classify the report"))
        self.selectButton.setText(_translate("MainWindow", "Select"))