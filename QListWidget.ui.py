# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QListWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QListWidgetItems(object):
    def setupUi(self, QListWidgetItems):
        QListWidgetItems.setObjectName("QListWidgetItems")
        QListWidgetItems.resize(400, 300)
        self.listWidget = QtWidgets.QListWidget(QListWidgetItems)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 171, 71))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.listWidget_2 = QtWidgets.QListWidget(QListWidgetItems)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 100, 171, 41))
        self.listWidget_2.setObjectName("listWidget_2")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_2.addItem(item)

        self.retranslateUi(QListWidgetItems)
        QtCore.QMetaObject.connectSlotsByName(QListWidgetItems)

    def retranslateUi(self, QListWidgetItems):
        _translate = QtCore.QCoreApplication.translate
        QListWidgetItems.setWindowTitle(_translate("QListWidgetItems", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("QListWidgetItems", "WATT"))
        item = self.listWidget.item(1)
        item.setText(_translate("QListWidgetItems", "PyQt"))
        item = self.listWidget.item(2)
        item.setText(_translate("QListWidgetItems", "PyQt5"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)
        item = self.listWidget_2.item(0)
        item.setText(_translate("QListWidgetItems", "PyQt5 learnings"))
        self.listWidget_2.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QListWidgetItems = QtWidgets.QDialog()
    ui = Ui_QListWidgetItems()
    ui.setupUi(QListWidgetItems)
    QListWidgetItems.show()
    sys.exit(app.exec_())
