# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BillingvAIHrY.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(591, 323)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 551, 31))
        font = QFont()
        font.setFamilies([u"Perpetua"])
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(17, 131, 112);\n"
"border-radius: 5px;")
        self.error_label = QLabel(self.centralwidget)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setGeometry(QRect(110, 170, 351, 16))
        font1 = QFont()
        font1.setBold(False)
        self.error_label.setFont(font1)
        self.error_label.setStyleSheet(u"color: red;")
        self.error_label.setAlignment(Qt.AlignCenter)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 140, 551, 141))
        self.groupBox.setStyleSheet(u"border-style: solid;\n"
"border-width: 0.5px;\n"
"border-color: rgb(17, 131, 112);\n"
"border-radius: 5px;")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(450, 20, 91, 101))
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 91, 101))
        icon = QIcon(QIcon.fromTheme(u"folder"))
        self.pushButton.setIcon(icon)
        self.outputFileBox = QGroupBox(self.groupBox)
        self.outputFileBox.setObjectName(u"outputFileBox")
        self.outputFileBox.setGeometry(QRect(110, 70, 331, 51))
        self.outputFileBox.setAlignment(Qt.AlignCenter)
        self.outputFileText = QPlainTextEdit(self.outputFileBox)
        self.outputFileText.setObjectName(u"outputFileText")
        self.outputFileText.setEnabled(True)
        self.outputFileText.setGeometry(QRect(10, 15, 311, 31))
        self.fileInputBox = QGroupBox(self.groupBox)
        self.fileInputBox.setObjectName(u"fileInputBox")
        self.fileInputBox.setGeometry(QRect(110, 20, 331, 51))
        self.fileInputBox.setAlignment(Qt.AlignCenter)
        self.inputFileText = QPlainTextEdit(self.fileInputBox)
        self.inputFileText.setObjectName(u"inputFileText")
        self.inputFileText.setEnabled(True)
        self.inputFileText.setGeometry(QRect(10, 15, 311, 31))
        self.inputFileText.setReadOnly(False)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(20, 50, 551, 80))
        self.groupBox_2.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(17, 131, 112);\n"
"border-radius: 5px;")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.categoryInput = QPlainTextEdit(self.groupBox_2)
        self.categoryInput.setObjectName(u"categoryInput")
        self.categoryInput.setEnabled(True)
        self.categoryInput.setGeometry(QRect(10, 30, 381, 31))
        self.categoryInput.setReadOnly(False)
        self.selectButton = QPushButton(self.groupBox_2)
        self.selectButton.setObjectName(u"selectButton")
        self.selectButton.setGeometry(QRect(400, 30, 141, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Please enter raw attendace file to generate Attendancec Billing Report", None))
        self.error_label.setText("")
        self.groupBox.setTitle("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Upload", None))
        self.outputFileBox.setTitle(QCoreApplication.translate("MainWindow", u"Enter Ouput File name", None))
        self.outputFileText.setPlainText(QCoreApplication.translate("MainWindow", u"Sample.xlsx", None))
        self.fileInputBox.setTitle(QCoreApplication.translate("MainWindow", u"File Input", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Upload a category file to classify the report", None))
        self.selectButton.setText(QCoreApplication.translate("MainWindow", u"Select", None))
    # retranslateUi

