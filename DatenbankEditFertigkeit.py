# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankEditFertigkeit.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_talentDialog(object):
    def setupUi(self, talentDialog):
        talentDialog.setObjectName("talentDialog")
        talentDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        talentDialog.resize(440, 550)
        self.gridLayout_2 = QtWidgets.QGridLayout(talentDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.nameEdit = QtWidgets.QLineEdit(talentDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboAttribut1 = QtWidgets.QComboBox(talentDialog)
        self.comboAttribut1.setMinimumSize(QtCore.QSize(45, 0))
        self.comboAttribut1.setObjectName("comboAttribut1")
        self.comboAttribut1.addItem("")
        self.comboAttribut1.addItem("")
        self.comboAttribut1.addItem("")
        self.comboAttribut1.addItem("")
        self.comboAttribut1.addItem("")
        self.comboAttribut1.addItem("")
        self.comboAttribut1.addItem("")
        self.comboAttribut1.addItem("")
        self.horizontalLayout.addWidget(self.comboAttribut1)
        self.label_6 = QtWidgets.QLabel(talentDialog)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.comboAttribut2 = QtWidgets.QComboBox(talentDialog)
        self.comboAttribut2.setMinimumSize(QtCore.QSize(45, 0))
        self.comboAttribut2.setObjectName("comboAttribut2")
        self.comboAttribut2.addItem("")
        self.comboAttribut2.addItem("")
        self.comboAttribut2.addItem("")
        self.comboAttribut2.addItem("")
        self.comboAttribut2.addItem("")
        self.comboAttribut2.addItem("")
        self.comboAttribut2.addItem("")
        self.comboAttribut2.addItem("")
        self.horizontalLayout.addWidget(self.comboAttribut2)
        self.label_7 = QtWidgets.QLabel(talentDialog)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.comboAttribut3 = QtWidgets.QComboBox(talentDialog)
        self.comboAttribut3.setMinimumSize(QtCore.QSize(45, 0))
        self.comboAttribut3.setObjectName("comboAttribut3")
        self.comboAttribut3.addItem("")
        self.comboAttribut3.addItem("")
        self.comboAttribut3.addItem("")
        self.comboAttribut3.addItem("")
        self.comboAttribut3.addItem("")
        self.comboAttribut3.addItem("")
        self.comboAttribut3.addItem("")
        self.comboAttribut3.addItem("")
        self.horizontalLayout.addWidget(self.comboAttribut3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(talentDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.labelKampffertigkeit = QtWidgets.QLabel(talentDialog)
        self.labelKampffertigkeit.setObjectName("labelKampffertigkeit")
        self.gridLayout.addWidget(self.labelKampffertigkeit, 4, 0, 1, 1)
        self.comboKampffertigkeit = QtWidgets.QComboBox(talentDialog)
        self.comboKampffertigkeit.setObjectName("comboKampffertigkeit")
        self.comboKampffertigkeit.addItem("")
        self.comboKampffertigkeit.addItem("")
        self.comboKampffertigkeit.addItem("")
        self.gridLayout.addWidget(self.comboKampffertigkeit, 4, 2, 1, 1)
        self.labelVoraussetzungen = QtWidgets.QLabel(talentDialog)
        self.labelVoraussetzungen.setObjectName("labelVoraussetzungen")
        self.gridLayout.addWidget(self.labelVoraussetzungen, 4, 0, 1, 1)
        self.voraussetzungenEdit = QtWidgets.QPlainTextEdit(talentDialog)
        self.voraussetzungenEdit.setObjectName("voraussetzungenEdit")
        self.gridLayout.addWidget(self.voraussetzungenEdit, 4, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(talentDialog)
        self.label_2.setMinimumSize(QtCore.QSize(110, 0))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(talentDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.textEdit = QtWidgets.QPlainTextEdit(talentDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 5, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(talentDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.steigerungsfaktorEdit = QtWidgets.QSpinBox(talentDialog)
        self.steigerungsfaktorEdit.setSuffix("")
        self.steigerungsfaktorEdit.setMinimum(1)
        self.steigerungsfaktorEdit.setMaximum(4)
        self.steigerungsfaktorEdit.setSingleStep(1)
        self.steigerungsfaktorEdit.setProperty("value", 2)
        self.steigerungsfaktorEdit.setObjectName("steigerungsfaktorEdit")
        self.horizontalLayout_2.addWidget(self.steigerungsfaktorEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(talentDialog)
        self.label_12.setMinimumSize(QtCore.QSize(110, 0))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.sortierungEdit = QtWidgets.QSpinBox(talentDialog)
        self.sortierungEdit.setSuffix("")
        self.sortierungEdit.setMinimum(-1)
        self.sortierungEdit.setMaximum(999)
        self.sortierungEdit.setSingleStep(1)
        self.sortierungEdit.setProperty("value", -1)
        self.sortierungEdit.setObjectName("sortierungEdit")
        self.horizontalLayout_12.addWidget(self.sortierungEdit)
        self.gridLayout.addLayout(self.horizontalLayout_12, 6, 2, 1, 1)
        self.warning = QtWidgets.QLabel(talentDialog)
        self.warning.setVisible(False)
        self.warning.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")
        self.gridLayout.addWidget(self.warning, 0, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(talentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(talentDialog)
        self.buttonBox.accepted.connect(talentDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(talentDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(talentDialog)
        talentDialog.setTabOrder(self.nameEdit, self.steigerungsfaktorEdit)
        talentDialog.setTabOrder(self.steigerungsfaktorEdit, self.comboAttribut1)
        talentDialog.setTabOrder(self.comboAttribut1, self.comboAttribut2)
        talentDialog.setTabOrder(self.comboAttribut2, self.comboAttribut3)
        talentDialog.setTabOrder(self.comboAttribut3, self.comboKampffertigkeit)
        talentDialog.setTabOrder(self.comboKampffertigkeit, self.voraussetzungenEdit)
        talentDialog.setTabOrder(self.voraussetzungenEdit, self.textEdit)

    def retranslateUi(self, talentDialog):
        _translate = QtCore.QCoreApplication.translate
        talentDialog.setWindowTitle(_translate("talentDialog", "Sephrasto - Fertigkeit bearbeiten..."))
        self.comboAttribut1.setItemText(0, _translate("talentDialog", "KO"))
        self.comboAttribut1.setItemText(1, _translate("talentDialog", "MU"))
        self.comboAttribut1.setItemText(2, _translate("talentDialog", "GE"))
        self.comboAttribut1.setItemText(3, _translate("talentDialog", "KK"))
        self.comboAttribut1.setItemText(4, _translate("talentDialog", "IN"))
        self.comboAttribut1.setItemText(5, _translate("talentDialog", "KL"))
        self.comboAttribut1.setItemText(6, _translate("talentDialog", "CH"))
        self.comboAttribut1.setItemText(7, _translate("talentDialog", "FF"))
        self.label_6.setText(_translate("talentDialog", " - "))
        self.comboAttribut2.setItemText(0, _translate("talentDialog", "KO"))
        self.comboAttribut2.setItemText(1, _translate("talentDialog", "MU"))
        self.comboAttribut2.setItemText(2, _translate("talentDialog", "GE"))
        self.comboAttribut2.setItemText(3, _translate("talentDialog", "KK"))
        self.comboAttribut2.setItemText(4, _translate("talentDialog", "IN"))
        self.comboAttribut2.setItemText(5, _translate("talentDialog", "KL"))
        self.comboAttribut2.setItemText(6, _translate("talentDialog", "CH"))
        self.comboAttribut2.setItemText(7, _translate("talentDialog", "FF"))
        self.label_7.setText(_translate("talentDialog", " - "))
        self.comboAttribut3.setItemText(0, _translate("talentDialog", "KO"))
        self.comboAttribut3.setItemText(1, _translate("talentDialog", "MU"))
        self.comboAttribut3.setItemText(2, _translate("talentDialog", "GE"))
        self.comboAttribut3.setItemText(3, _translate("talentDialog", "KK"))
        self.comboAttribut3.setItemText(4, _translate("talentDialog", "IN"))
        self.comboAttribut3.setItemText(5, _translate("talentDialog", "KL"))
        self.comboAttribut3.setItemText(6, _translate("talentDialog", "CH"))
        self.comboAttribut3.setItemText(7, _translate("talentDialog", "FF"))
        self.label.setText(_translate("talentDialog", "Fertigkeitsname"))
        self.labelKampffertigkeit.setText(_translate("talentDialog", "Fertigkeitstyp"))
        self.comboKampffertigkeit.setItemText(0, _translate("talentDialog", "Keine Kampffertigkeit"))
        self.comboKampffertigkeit.setItemText(1, _translate("talentDialog", "Nahkampffertigkeit"))
        self.comboKampffertigkeit.setItemText(2, _translate("talentDialog", "Sonstige Kampffertigkeit"))
        self.labelVoraussetzungen.setText(_translate("talentDialog", "Voraussetzungen"))
        self.label_2.setText(_translate("talentDialog", "Steigerungsfaktor"))
        self.label_3.setText(_translate("talentDialog", "Attribute"))
        self.label_5.setText(_translate("talentDialog", "Beschreibung"))
        self.label_12.setText(_translate("talentDialog", "Sortierung"))
        self.warning.setText(_translate("talentDialog", "Dies ist eine Ilaris-Standardfertigkeit. Sobald du hier etwas veränderst, bekommst du eine persönliche Kopie und das Original wird in der aktuellen User-Regelbasis gelöscht. Damit erhältst du für diese Fertigkeit keine automatischen Updates mehr mit neuen Sephrasto-Versionen."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    talentDialog = QtWidgets.QDialog()
    ui = Ui_talentDialog()
    ui.setupUi(talentDialog)
    talentDialog.show()
    sys.exit(app.exec_())
