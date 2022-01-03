# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankEditVorteil.ui'
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
        talentDialog.resize(475, 801)
        self.gridLayout_2 = QtWidgets.QGridLayout(talentDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(talentDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtWidgets.QPlainTextEdit(talentDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 9, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(talentDialog)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 13, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkVariable = QtWidgets.QCheckBox(talentDialog)
        self.checkVariable.setObjectName("checkVariable")
        self.horizontalLayout_2.addWidget(self.checkVariable)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.kostenEdit = QtWidgets.QSpinBox(talentDialog)
        self.kostenEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.kostenEdit.setMinimum(-10000)
        self.kostenEdit.setMaximum(10000)
        self.kostenEdit.setSingleStep(20)
        self.kostenEdit.setProperty("value", 40)
        self.kostenEdit.setObjectName("kostenEdit")
        self.horizontalLayout_2.addWidget(self.kostenEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(talentDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.scriptEdit = QtWidgets.QLineEdit(talentDialog)
        self.scriptEdit.setObjectName("scriptEdit")
        self.horizontalLayout_4.addWidget(self.scriptEdit)
        self.scriptPrioEdit = QtWidgets.QSpinBox(talentDialog)
        self.scriptPrioEdit.setMinimum(-10)
        self.scriptPrioEdit.setMaximum(10)
        self.scriptPrioEdit.setSingleStep(1)
        self.scriptPrioEdit.setProperty("value", 0)
        self.scriptPrioEdit.setObjectName("scriptPrioEdit")
        self.horizontalLayout_4.addWidget(self.scriptPrioEdit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 10, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(talentDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setMaximumSize(QtCore.QSize(130, 16777215))
        self.label_8.setWordWrap(True)
        self.label_8.setIndent(0)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 14, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(talentDialog)
        self.label_4.setMinimumSize(QtCore.QSize(110, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(talentDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.comboNachkauf = QtWidgets.QComboBox(talentDialog)
        self.comboNachkauf.setObjectName("comboNachkauf")
        self.comboNachkauf.addItem("")
        self.comboNachkauf.addItem("")
        self.comboNachkauf.addItem("")
        self.comboNachkauf.addItem("")
        self.comboNachkauf.addItem("")
        self.horizontalLayout.addWidget(self.comboNachkauf)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 1, 1, 1)
        self.line_2 = QtWidgets.QFrame(talentDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 12, 0, 1, 2)
        self.voraussetzungenEdit = QtWidgets.QPlainTextEdit(talentDialog)
        self.voraussetzungenEdit.setObjectName("voraussetzungenEdit")
        self.gridLayout.addWidget(self.voraussetzungenEdit, 7, 1, 1, 1)
        self.label_41 = QtWidgets.QLabel(talentDialog)
        self.label_41.setMinimumSize(QtCore.QSize(110, 0))
        self.label_41.setObjectName("label_41")
        self.gridLayout.addWidget(self.label_41, 10, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboTyp = QtWidgets.QComboBox(talentDialog)
        self.comboTyp.setObjectName("comboTyp")
        self.horizontalLayout_3.addWidget(self.comboTyp)
        self.gridLayout.addLayout(self.horizontalLayout_3, 8, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(talentDialog)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.checkKommentar = QtWidgets.QCheckBox(talentDialog)
        self.checkKommentar.setObjectName("checkKommentar")
        self.gridLayout.addWidget(self.checkKommentar, 4, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(talentDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(talentDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 8, 0, 1, 1)
        self.label = QtWidgets.QLabel(talentDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.warning = QtWidgets.QLabel(talentDialog)
        self.warning.setVisible(False)
        self.warning.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.warning.setWordWrap(True)
        self.warning.setObjectName("warning")
        self.gridLayout.addWidget(self.warning, 0, 0, 1, 2)
        self.checkCheatsheet = QtWidgets.QCheckBox(talentDialog)
        self.checkCheatsheet.setChecked(True)
        self.checkCheatsheet.setObjectName("checkCheatsheet")
        self.gridLayout.addWidget(self.checkCheatsheet, 13, 1, 1, 1)
        self.horizontalLayout1 = QtWidgets.QHBoxLayout()
        self.horizontalLayout1.setObjectName("horizontalLayout1")
        self.gridLayout.addLayout(self.horizontalLayout1, 17, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(talentDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 9, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.comboLinkKategorie = QtWidgets.QComboBox(talentDialog)
        self.comboLinkKategorie.setMaximumSize(QtCore.QSize(130, 16777215))
        self.comboLinkKategorie.setObjectName("comboLinkKategorie")
        self.comboLinkKategorie.addItem("")
        self.comboLinkKategorie.addItem("")
        self.comboLinkKategorie.addItem("")
        self.comboLinkKategorie.addItem("")
        self.horizontalLayout_5.addWidget(self.comboLinkKategorie)
        self.comboLinkElement = QtWidgets.QComboBox(talentDialog)
        self.comboLinkElement.setObjectName("comboLinkElement")
        self.horizontalLayout_5.addWidget(self.comboLinkElement)
        self.gridLayout.addLayout(self.horizontalLayout_5, 11, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(talentDialog)
        self.label_9.setIndent(0)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 11, 0, 1, 1)
        self.teCheatsheet = QtWidgets.QPlainTextEdit(talentDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teCheatsheet.sizePolicy().hasHeightForWidth())
        self.teCheatsheet.setSizePolicy(sizePolicy)
        self.teCheatsheet.setObjectName("teCheatsheet")
        self.gridLayout.addWidget(self.teCheatsheet, 14, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(talentDialog)
        self.buttonBox.accepted.connect(talentDialog.accept) # type: ignore
        self.buttonBox.rejected.connect(talentDialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(talentDialog)
        talentDialog.setTabOrder(self.nameEdit, self.checkVariable)
        talentDialog.setTabOrder(self.checkVariable, self.kostenEdit)
        talentDialog.setTabOrder(self.kostenEdit, self.checkKommentar)
        talentDialog.setTabOrder(self.checkKommentar, self.comboNachkauf)
        talentDialog.setTabOrder(self.comboNachkauf, self.voraussetzungenEdit)
        talentDialog.setTabOrder(self.voraussetzungenEdit, self.comboTyp)
        talentDialog.setTabOrder(self.comboTyp, self.textEdit)
        talentDialog.setTabOrder(self.textEdit, self.scriptEdit)
        talentDialog.setTabOrder(self.scriptEdit, self.scriptPrioEdit)
        talentDialog.setTabOrder(self.scriptPrioEdit, self.comboLinkKategorie)
        talentDialog.setTabOrder(self.comboLinkKategorie, self.comboLinkElement)
        talentDialog.setTabOrder(self.comboLinkElement, self.checkCheatsheet)
        talentDialog.setTabOrder(self.checkCheatsheet, self.teCheatsheet)

    def retranslateUi(self, talentDialog):
        _translate = QtCore.QCoreApplication.translate
        talentDialog.setWindowTitle(_translate("talentDialog", "Sephrasto - Vorteil bearbeiten..."))
        self.label_10.setText(_translate("talentDialog", "Cheatsheet"))
        self.checkVariable.setText(_translate("talentDialog", "Kosten sind Variabel"))
        self.kostenEdit.setSuffix(_translate("talentDialog", " EP"))
        self.label_8.setText(_translate("talentDialog", "Alternative Beschreibung (optional)"))
        self.label_4.setText(_translate("talentDialog", "Voraussetzungen"))
        self.label_2.setText(_translate("talentDialog", "Lernkosten"))
        self.comboNachkauf.setItemText(0, _translate("talentDialog", "häufig"))
        self.comboNachkauf.setItemText(1, _translate("talentDialog", "üblich"))
        self.comboNachkauf.setItemText(2, _translate("talentDialog", "selten"))
        self.comboNachkauf.setItemText(3, _translate("talentDialog", "extrem selten"))
        self.comboNachkauf.setItemText(4, _translate("talentDialog", "nicht möglich"))
        self.label_41.setText(_translate("talentDialog", "Script / Priorität"))
        self.label_3.setText(_translate("talentDialog", "Nachkauf"))
        self.checkKommentar.setText(_translate("talentDialog", "Nutzern erlauben einen Kommentar einzutragen"))
        self.label_7.setText(_translate("talentDialog", "Kommentar"))
        self.label_6.setText(_translate("talentDialog", "Typ"))
        self.label.setText(_translate("talentDialog", "Vorteilsname"))
        self.warning.setText(_translate("talentDialog", "Dies ist ein Ilaris-Standardvorteil. Sobald du hier etwas veränderst, bekommst du eine persönliche Kopie und das Original wird in der aktuellen User-Regelbasis gelöscht. Damit erhältst du für diesen Vorteil keine automatischen Updates mehr mit neuen Sephrasto-Versionen."))
        self.checkCheatsheet.setText(_translate("talentDialog", "Auflisten"))
        self.label_5.setText(_translate("talentDialog", "Beschreibung"))
        self.comboLinkKategorie.setItemText(0, _translate("talentDialog", "Nicht verknüpfen"))
        self.comboLinkKategorie.setItemText(1, _translate("talentDialog", "Manöver / Mod."))
        self.comboLinkKategorie.setItemText(2, _translate("talentDialog", "Übernat. Talent"))
        self.comboLinkKategorie.setItemText(3, _translate("talentDialog", "Vorteil"))
        self.label_9.setText(_translate("talentDialog", "Verknüpfung"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    talentDialog = QtWidgets.QDialog()
    ui = Ui_talentDialog()
    ui.setupUi(talentDialog)
    talentDialog.show()
    sys.exit(app.exec_())
