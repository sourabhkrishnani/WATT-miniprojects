# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student_details.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(573, 376)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(140, 20, 281, 41))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(140, 80, 281, 41))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(140, 140, 281, 41))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(140, 210, 281, 41))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Proceed"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "\" Enter yorn name \"\n"
""))
        self.plainTextEdit_2.setPlainText(_translate("Dialog", "\" Enter your roll num\""))
        self.plainTextEdit_3.setPlainText(_translate("Dialog", "\" Enter your current CGPA \""))
        self.comboBox.setItemText(0, _translate("Dialog", "Python"))
        self.comboBox.setItemText(1, _translate("Dialog", "java"))
        self.comboBox.setItemText(2, _translate("Dialog", "c++"))
        self.comboBox.setItemText(3, _translate("Dialog", "c"))
        self.comboBox.setItemText(4, _translate("Dialog", "php"))
        self.comboBox.setItemText(5, _translate("Dialog", "kotlin"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
