# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterEP.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(872, 460)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.spinFreiePercent = QtWidgets.QSpinBox(Form)
        self.spinFreiePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinFreiePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFreiePercent.setReadOnly(True)
        self.spinFreiePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinFreiePercent.setMaximum(100)
        self.spinFreiePercent.setObjectName("spinFreiePercent")
        self.gridLayout.addWidget(self.spinFreiePercent, 6, 4, 1, 1)
        self.spinFreieSpent = QtWidgets.QSpinBox(Form)
        self.spinFreieSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinFreieSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFreieSpent.setReadOnly(True)
        self.spinFreieSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinFreieSpent.setMaximum(999999)
        self.spinFreieSpent.setObjectName("spinFreieSpent")
        self.gridLayout.addWidget(self.spinFreieSpent, 6, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 3, 1, 1)
        self.spinUeberFertigkeitenSpent = QtWidgets.QSpinBox(Form)
        self.spinUeberFertigkeitenSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUeberFertigkeitenSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUeberFertigkeitenSpent.setReadOnly(True)
        self.spinUeberFertigkeitenSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUeberFertigkeitenSpent.setMaximum(999999)
        self.spinUeberFertigkeitenSpent.setObjectName("spinUeberFertigkeitenSpent")
        self.gridLayout.addWidget(self.spinUeberFertigkeitenSpent, 9, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 11, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 5, 1, 1)
        self.spinTalentePercent = QtWidgets.QSpinBox(Form)
        self.spinTalentePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinTalentePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinTalentePercent.setReadOnly(True)
        self.spinTalentePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinTalentePercent.setMaximum(100)
        self.spinTalentePercent.setObjectName("spinTalentePercent")
        self.gridLayout.addWidget(self.spinTalentePercent, 5, 4, 1, 1)
        self.labelUeber3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelUeber3.setFont(font)
        self.labelUeber3.setObjectName("labelUeber3")
        self.gridLayout.addWidget(self.labelUeber3, 10, 1, 1, 1)
        self.spinUeberTalenteSpent = QtWidgets.QSpinBox(Form)
        self.spinUeberTalenteSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUeberTalenteSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUeberTalenteSpent.setReadOnly(True)
        self.spinUeberTalenteSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUeberTalenteSpent.setMaximum(999999)
        self.spinUeberTalenteSpent.setObjectName("spinUeberTalenteSpent")
        self.gridLayout.addWidget(self.spinUeberTalenteSpent, 10, 3, 1, 1)
        self.spinVorteilePercent = QtWidgets.QSpinBox(Form)
        self.spinVorteilePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinVorteilePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinVorteilePercent.setReadOnly(True)
        self.spinVorteilePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinVorteilePercent.setMaximum(100)
        self.spinVorteilePercent.setObjectName("spinVorteilePercent")
        self.gridLayout.addWidget(self.spinVorteilePercent, 2, 4, 1, 1)
        self.spinVorteileSpent = QtWidgets.QSpinBox(Form)
        self.spinVorteileSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinVorteileSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinVorteileSpent.setReadOnly(True)
        self.spinVorteileSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinVorteileSpent.setMaximum(99999999)
        self.spinVorteileSpent.setObjectName("spinVorteileSpent")
        self.gridLayout.addWidget(self.spinVorteileSpent, 2, 3, 1, 1)
        self.spinAttributePercent = QtWidgets.QSpinBox(Form)
        self.spinAttributePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinAttributePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinAttributePercent.setReadOnly(True)
        self.spinAttributePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinAttributePercent.setMaximum(100)
        self.spinAttributePercent.setObjectName("spinAttributePercent")
        self.gridLayout.addWidget(self.spinAttributePercent, 1, 4, 1, 1)
        self.spinUebernatuerlichSpent = QtWidgets.QSpinBox(Form)
        self.spinUebernatuerlichSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUebernatuerlichSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUebernatuerlichSpent.setReadOnly(True)
        self.spinUebernatuerlichSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUebernatuerlichSpent.setMaximum(999999)
        self.spinUebernatuerlichSpent.setObjectName("spinUebernatuerlichSpent")
        self.gridLayout.addWidget(self.spinUebernatuerlichSpent, 7, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 1, 1, 1)
        self.spinProfanSpent = QtWidgets.QSpinBox(Form)
        self.spinProfanSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinProfanSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinProfanSpent.setReadOnly(True)
        self.spinProfanSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinProfanSpent.setMaximum(999999)
        self.spinProfanSpent.setObjectName("spinProfanSpent")
        self.gridLayout.addWidget(self.spinProfanSpent, 3, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)
        self.spinUeberTalentePercent = QtWidgets.QSpinBox(Form)
        self.spinUeberTalentePercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUeberTalentePercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUeberTalentePercent.setReadOnly(True)
        self.spinUeberTalentePercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUeberTalentePercent.setMaximum(100)
        self.spinUeberTalentePercent.setObjectName("spinUeberTalentePercent")
        self.gridLayout.addWidget(self.spinUeberTalentePercent, 10, 4, 1, 1)
        self.labelUeber2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelUeber2.setFont(font)
        self.labelUeber2.setObjectName("labelUeber2")
        self.gridLayout.addWidget(self.labelUeber2, 9, 1, 1, 1)
        self.spinProfanPercent = QtWidgets.QSpinBox(Form)
        self.spinProfanPercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinProfanPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinProfanPercent.setReadOnly(True)
        self.spinProfanPercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinProfanPercent.setMaximum(100)
        self.spinProfanPercent.setObjectName("spinProfanPercent")
        self.gridLayout.addWidget(self.spinProfanPercent, 3, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        self.spinAttributeSpent = QtWidgets.QSpinBox(Form)
        self.spinAttributeSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinAttributeSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinAttributeSpent.setReadOnly(True)
        self.spinAttributeSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinAttributeSpent.setMaximum(99999999)
        self.spinAttributeSpent.setObjectName("spinAttributeSpent")
        self.gridLayout.addWidget(self.spinAttributeSpent, 1, 3, 1, 1)
        self.spinUebernatuerlichPercent = QtWidgets.QSpinBox(Form)
        self.spinUebernatuerlichPercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUebernatuerlichPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUebernatuerlichPercent.setReadOnly(True)
        self.spinUebernatuerlichPercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUebernatuerlichPercent.setMaximum(100)
        self.spinUebernatuerlichPercent.setObjectName("spinUebernatuerlichPercent")
        self.gridLayout.addWidget(self.spinUebernatuerlichPercent, 7, 4, 1, 1)
        self.spinUeberFertigkeitenPercent = QtWidgets.QSpinBox(Form)
        self.spinUeberFertigkeitenPercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinUeberFertigkeitenPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinUeberFertigkeitenPercent.setReadOnly(True)
        self.spinUeberFertigkeitenPercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinUeberFertigkeitenPercent.setMaximum(100)
        self.spinUeberFertigkeitenPercent.setObjectName("spinUeberFertigkeitenPercent")
        self.gridLayout.addWidget(self.spinUeberFertigkeitenPercent, 9, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)
        self.spinFertigkeitenSpent = QtWidgets.QSpinBox(Form)
        self.spinFertigkeitenSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinFertigkeitenSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFertigkeitenSpent.setReadOnly(True)
        self.spinFertigkeitenSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinFertigkeitenSpent.setMaximum(999999)
        self.spinFertigkeitenSpent.setObjectName("spinFertigkeitenSpent")
        self.gridLayout.addWidget(self.spinFertigkeitenSpent, 4, 3, 1, 1)
        self.spinTalenteSpent = QtWidgets.QSpinBox(Form)
        self.spinTalenteSpent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinTalenteSpent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinTalenteSpent.setReadOnly(True)
        self.spinTalenteSpent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinTalenteSpent.setMaximum(999999)
        self.spinTalenteSpent.setObjectName("spinTalenteSpent")
        self.gridLayout.addWidget(self.spinTalenteSpent, 5, 3, 1, 1)
        self.labelUeber1 = QtWidgets.QLabel(Form)
        self.labelUeber1.setObjectName("labelUeber1")
        self.gridLayout.addWidget(self.labelUeber1, 7, 1, 1, 1)
        self.spinFertigkeitenPercent = QtWidgets.QSpinBox(Form)
        self.spinFertigkeitenPercent.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinFertigkeitenPercent.setAlignment(QtCore.Qt.AlignCenter)
        self.spinFertigkeitenPercent.setReadOnly(True)
        self.spinFertigkeitenPercent.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinFertigkeitenPercent.setMaximum(100)
        self.spinFertigkeitenPercent.setObjectName("spinFertigkeitenPercent")
        self.gridLayout.addWidget(self.spinFertigkeitenPercent, 4, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.spinAttributeSpent, self.spinAttributePercent)
        Form.setTabOrder(self.spinAttributePercent, self.spinVorteileSpent)
        Form.setTabOrder(self.spinVorteileSpent, self.spinVorteilePercent)
        Form.setTabOrder(self.spinVorteilePercent, self.spinProfanSpent)
        Form.setTabOrder(self.spinProfanSpent, self.spinProfanPercent)
        Form.setTabOrder(self.spinProfanPercent, self.spinFertigkeitenSpent)
        Form.setTabOrder(self.spinFertigkeitenSpent, self.spinFertigkeitenPercent)
        Form.setTabOrder(self.spinFertigkeitenPercent, self.spinTalenteSpent)
        Form.setTabOrder(self.spinTalenteSpent, self.spinTalentePercent)
        Form.setTabOrder(self.spinTalentePercent, self.spinFreieSpent)
        Form.setTabOrder(self.spinFreieSpent, self.spinFreiePercent)
        Form.setTabOrder(self.spinFreiePercent, self.spinUebernatuerlichSpent)
        Form.setTabOrder(self.spinUebernatuerlichSpent, self.spinUebernatuerlichPercent)
        Form.setTabOrder(self.spinUebernatuerlichPercent, self.spinUeberFertigkeitenSpent)
        Form.setTabOrder(self.spinUeberFertigkeitenSpent, self.spinUeberFertigkeitenPercent)
        Form.setTabOrder(self.spinUeberFertigkeitenPercent, self.spinUeberTalenteSpent)
        Form.setTabOrder(self.spinUeberTalenteSpent, self.spinUeberTalentePercent)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.spinFreiePercent.setSuffix(_translate("Form", " %)"))
        self.spinFreiePercent.setPrefix(_translate("Form", "("))
        self.spinFreieSpent.setSuffix(_translate("Form", " EP"))
        self.label_4.setText(_translate("Form", "    --> Freie Fertigkeiten"))
        self.spinUeberFertigkeitenSpent.setSuffix(_translate("Form", " EP"))
        self.spinTalentePercent.setSuffix(_translate("Form", " %)"))
        self.spinTalentePercent.setPrefix(_translate("Form", "("))
        self.labelUeber3.setText(_translate("Form", "    --> Talente"))
        self.spinUeberTalenteSpent.setSuffix(_translate("Form", " EP"))
        self.spinVorteilePercent.setSuffix(_translate("Form", " %"))
        self.spinVorteileSpent.setSuffix(_translate("Form", " EP"))
        self.spinAttributePercent.setSuffix(_translate("Form", " %"))
        self.spinUebernatuerlichSpent.setSuffix(_translate("Form", " EP"))
        self.label_3.setText(_translate("Form", "Profane Fertigkeiten und Talente"))
        self.spinProfanSpent.setSuffix(_translate("Form", " EP"))
        self.label_2.setText(_translate("Form", "Vorteile"))
        self.spinUeberTalentePercent.setSuffix(_translate("Form", " %)"))
        self.spinUeberTalentePercent.setPrefix(_translate("Form", "("))
        self.labelUeber2.setText(_translate("Form", "    --> Fertigkeiten"))
        self.spinProfanPercent.setSuffix(_translate("Form", " %"))
        self.label.setText(_translate("Form", "Attribute"))
        self.spinAttributeSpent.setSuffix(_translate("Form", " EP"))
        self.spinUebernatuerlichPercent.setSuffix(_translate("Form", " %"))
        self.spinUeberFertigkeitenPercent.setSuffix(_translate("Form", " %)"))
        self.spinUeberFertigkeitenPercent.setPrefix(_translate("Form", "("))
        self.label_8.setText(_translate("Form", "    --> Fertigkeiten"))
        self.label_9.setText(_translate("Form", "    --> Talente"))
        self.spinFertigkeitenSpent.setSuffix(_translate("Form", " EP"))
        self.spinTalenteSpent.setSuffix(_translate("Form", " EP"))
        self.labelUeber1.setText(_translate("Form", "Übernatürliche Fertigkeiten und Talente"))
        self.spinFertigkeitenPercent.setSuffix(_translate("Form", " %)"))
        self.spinFertigkeitenPercent.setPrefix(_translate("Form", "("))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
