# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_resultWindow(object):
    def setupUi(self, resultWindow):
        resultWindow.setObjectName("resultWindow")
        resultWindow.resize(188, 129)
        resultWindow.setMinimumSize(QtCore.QSize(188, 129))
        resultWindow.setMaximumSize(QtCore.QSize(188, 129))
        resultWindow.setAccessibleDescription("")
        self.label = QtWidgets.QLabel(resultWindow)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 111))
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(resultWindow)
        QtCore.QMetaObject.connectSlotsByName(resultWindow)

    def retranslateUi(self, resultWindow):
        _translate = QtCore.QCoreApplication.translate
        resultWindow.setWindowTitle(_translate("resultWindow", "Wyniki"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    resultWindow = QtWidgets.QWidget()
    ui = Ui_resultWindow()
    ui.setupUi(resultWindow)
    resultWindow.show()
    sys.exit(app.exec_())

