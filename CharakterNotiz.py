# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterNotiz.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_formNotiz(object):
    def setupUi(self, formBeschreibung):
        formBeschreibung.setObjectName("formBeschreibung")
        formBeschreibung.setGeometry(QtCore.QRect(0, 0, 872, 460))
        self.gridLayout_3 = QtWidgets.QGridLayout(formBeschreibung)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.teNotiz = QtWidgets.QPlainTextEdit(formBeschreibung)
        self.teNotiz.setMinimumSize(QtCore.QSize(0, 0))
        self.teNotiz.setObjectName("teNotiz")
        self.gridLayout.addWidget(self.teNotiz, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(formBeschreibung)
        QtCore.QMetaObject.connectSlotsByName(formBeschreibung)

    def retranslateUi(self, formBeschreibung):
        _translate = QtCore.QCoreApplication.translate
        formBeschreibung.setWindowTitle(_translate("formNotiz", "Notiz"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    formBeschreibung = QtWidgets.QWidget()
    ui = Ui_formNotiz()
    ui.setupUi(formBeschreibung)
    formBeschreibung.show()
    sys.exit(app.exec_())
