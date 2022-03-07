# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankMain.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(795, 535)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelParameter = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelParameter.setFont(font)
        self.labelParameter.setObjectName("labelParameter")
        self.verticalLayout.addWidget(self.labelParameter)
        self.nameFilterEdit = QtWidgets.QLineEdit(Form)
        self.nameFilterEdit.setObjectName("nameFilterEdit")
        self.verticalLayout.addWidget(self.nameFilterEdit)
        self.checkFilterTyp = QtWidgets.QCheckBox(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkFilterTyp.setFont(font)
        self.checkFilterTyp.setChecked(True)
        self.checkFilterTyp.setTristate(True)
        self.checkFilterTyp.setObjectName("checkFilterTyp")
        self.verticalLayout.addWidget(self.checkFilterTyp)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.showVorteile = QtWidgets.QCheckBox(Form)
        self.showVorteile.setChecked(True)
        self.showVorteile.setTristate(False)
        self.showVorteile.setObjectName("showVorteile")
        self.verticalLayout_3.addWidget(self.showVorteile)
        self.showFertigkeiten = QtWidgets.QCheckBox(Form)
        self.showFertigkeiten.setChecked(True)
        self.showFertigkeiten.setObjectName("showFertigkeiten")
        self.verticalLayout_3.addWidget(self.showFertigkeiten)
        self.showFreieFertigkeiten = QtWidgets.QCheckBox(Form)
        self.showFreieFertigkeiten.setChecked(True)
        self.showFreieFertigkeiten.setObjectName("showFreieFertigkeiten")
        self.verticalLayout_3.addWidget(self.showFreieFertigkeiten)
        self.showUebernatuerlicheFertigkeiten = QtWidgets.QCheckBox(Form)
        self.showUebernatuerlicheFertigkeiten.setMinimumSize(QtCore.QSize(200, 0))
        self.showUebernatuerlicheFertigkeiten.setChecked(True)
        self.showUebernatuerlicheFertigkeiten.setObjectName("showUebernatuerlicheFertigkeiten")
        self.verticalLayout_3.addWidget(self.showUebernatuerlicheFertigkeiten)
        self.showTalente = QtWidgets.QCheckBox(Form)
        self.showTalente.setChecked(True)
        self.showTalente.setObjectName("showTalente")
        self.verticalLayout_3.addWidget(self.showTalente)
        self.showRuestungen = QtWidgets.QCheckBox(Form)
        self.showRuestungen.setChecked(True)
        self.showRuestungen.setObjectName("showRuestungen")
        self.verticalLayout_3.addWidget(self.showRuestungen)
        self.showWaffen = QtWidgets.QCheckBox(Form)
        self.showWaffen.setChecked(True)
        self.showWaffen.setObjectName("showWaffen")
        self.verticalLayout_3.addWidget(self.showWaffen)
        self.showWaffeneigenschaften = QtWidgets.QCheckBox(Form)
        self.showWaffeneigenschaften.setChecked(True)
        self.showWaffeneigenschaften.setObjectName("showWaffeneigenschaften")
        self.verticalLayout_3.addWidget(self.showWaffeneigenschaften)
        self.showManoever = QtWidgets.QCheckBox(Form)
        self.showManoever.setChecked(True)
        self.showManoever.setObjectName("showManoever")
        self.verticalLayout_3.addWidget(self.showManoever)
        self.showEinstellung = QtWidgets.QCheckBox(Form)
        self.showEinstellung.setChecked(True)
        self.showEinstellung.setObjectName("showEinstellung")
        self.verticalLayout_3.addWidget(self.showEinstellung)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.labelParameter1 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelParameter1.setFont(font)
        self.labelParameter1.setObjectName("labelParameter1")
        self.verticalLayout.addWidget(self.labelParameter1)
        self.showDeleted = QtWidgets.QCheckBox(Form)
        self.showDeleted.setChecked(True)
        self.showDeleted.setObjectName("showDeleted")
        self.verticalLayout.addWidget(self.showDeleted)
        self.showUserAdded = QtWidgets.QCheckBox(Form)
        self.showUserAdded.setChecked(False)
        self.showUserAdded.setObjectName("showUserAdded")
        self.verticalLayout.addWidget(self.showUserAdded)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonCloseDB = QtWidgets.QPushButton(Form)
        self.buttonCloseDB.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonCloseDB.setObjectName("buttonCloseDB")
        self.verticalLayout.addWidget(self.buttonCloseDB)
        self.buttonLoadDB = QtWidgets.QPushButton(Form)
        self.buttonLoadDB.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonLoadDB.setObjectName("buttonLoadDB")
        self.verticalLayout.addWidget(self.buttonLoadDB)
        self.buttonSaveDB = QtWidgets.QPushButton(Form)
        self.buttonSaveDB.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonSaveDB.setObjectName("buttonSaveDB")
        self.verticalLayout.addWidget(self.buttonSaveDB)
        self.buttonQuicksave = QtWidgets.QPushButton(Form)
        self.buttonQuicksave.setMinimumSize(QtCore.QSize(0, 25))
        self.buttonQuicksave.setObjectName("buttonQuicksave")
        self.verticalLayout.addWidget(self.buttonQuicksave)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.listDatenbank = QtWidgets.QListView(Form)
        self.listDatenbank.setObjectName("listDatenbank")
        self.verticalLayout_2.addWidget(self.listDatenbank)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.buttonHinzufuegen = QtWidgets.QPushButton(Form)
        self.buttonHinzufuegen.setMinimumSize(QtCore.QSize(28, 28))
        self.buttonHinzufuegen.setMaximumSize(QtCore.QSize(28, 28))
        self.buttonHinzufuegen.setObjectName("buttonHinzufuegen")
        self.horizontalLayout.addWidget(self.buttonHinzufuegen)
        self.buttonEditieren = QtWidgets.QPushButton(Form)
        self.buttonEditieren.setMinimumSize(QtCore.QSize(28, 28))
        self.buttonEditieren.setMaximumSize(QtCore.QSize(28, 28))
        self.buttonEditieren.setObjectName("buttonEditieren")
        self.horizontalLayout.addWidget(self.buttonEditieren)
        self.buttonDuplizieren = QtWidgets.QPushButton(Form)
        self.buttonDuplizieren.setMinimumSize(QtCore.QSize(28, 28))
        self.buttonDuplizieren.setMaximumSize(QtCore.QSize(28, 28))
        self.buttonDuplizieren.setObjectName("buttonDuplizieren")
        self.horizontalLayout.addWidget(self.buttonDuplizieren)
        self.buttonLoeschen = QtWidgets.QPushButton(Form)
        self.buttonLoeschen.setMinimumSize(QtCore.QSize(28, 28))
        self.buttonLoeschen.setMaximumSize(QtCore.QSize(28, 28))
        self.buttonLoeschen.setObjectName("buttonLoeschen")
        self.horizontalLayout.addWidget(self.buttonLoeschen)
        self.buttonWiederherstellen = QtWidgets.QPushButton(Form)
        self.buttonWiederherstellen.setMinimumSize(QtCore.QSize(28, 28))
        self.buttonWiederherstellen.setMaximumSize(QtCore.QSize(28, 28))
        self.buttonWiederherstellen.setVisible(False)
        self.buttonWiederherstellen.setObjectName("buttonWiederherstellen")
        self.horizontalLayout.addWidget(self.buttonWiederherstellen)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.nameFilterEdit, self.checkFilterTyp)
        Form.setTabOrder(self.checkFilterTyp, self.showVorteile)
        Form.setTabOrder(self.showVorteile, self.showFertigkeiten)
        Form.setTabOrder(self.showFertigkeiten, self.showFreieFertigkeiten)
        Form.setTabOrder(self.showFreieFertigkeiten, self.showUebernatuerlicheFertigkeiten)
        Form.setTabOrder(self.showUebernatuerlicheFertigkeiten, self.showTalente)
        Form.setTabOrder(self.showTalente, self.showRuestungen)
        Form.setTabOrder(self.showRuestungen, self.showWaffen)
        Form.setTabOrder(self.showWaffen, self.showWaffeneigenschaften)
        Form.setTabOrder(self.showWaffeneigenschaften, self.showManoever)
        Form.setTabOrder(self.showManoever, self.showDeleted)
        Form.setTabOrder(self.showDeleted, self.showUserAdded)
        Form.setTabOrder(self.showUserAdded, self.buttonCloseDB)
        Form.setTabOrder(self.buttonCloseDB, self.buttonLoadDB)
        Form.setTabOrder(self.buttonLoadDB, self.buttonSaveDB)
        Form.setTabOrder(self.buttonSaveDB, self.buttonQuicksave)
        Form.setTabOrder(self.buttonQuicksave, self.listDatenbank)
        Form.setTabOrder(self.listDatenbank, self.buttonHinzufuegen)
        Form.setTabOrder(self.buttonHinzufuegen, self.buttonEditieren)
        Form.setTabOrder(self.buttonEditieren, self.buttonDuplizieren)
        Form.setTabOrder(self.buttonDuplizieren, self.buttonLoeschen)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Sephrasto - Datenbank-Editor"))
        Form.setToolTip(_translate("Form", "Wiederherstellen"))
        self.labelParameter.setText(_translate("Form", "Filter nach Name:"))
        self.checkFilterTyp.setText(_translate("Form", "Filter nach Typ:"))
        self.showVorteile.setText(_translate("Form", "Vorteile"))
        self.showFertigkeiten.setText(_translate("Form", "Profane Fertigkeiten"))
        self.showFreieFertigkeiten.setText(_translate("Form", "Freie Fertigkeiten"))
        self.showUebernatuerlicheFertigkeiten.setText(_translate("Form", "Übernatürliche Fertigkeiten"))
        self.showTalente.setText(_translate("Form", "Talente"))
        self.showRuestungen.setText(_translate("Form", "Rüstungen"))
        self.showWaffen.setText(_translate("Form", "Waffen"))
        self.showWaffeneigenschaften.setText(_translate("Form", "Waffeneigenschaften"))
        self.showManoever.setText(_translate("Form", "Manöver / Modifikation / Regel"))
        self.showEinstellung.setText(_translate("Form", "Einstellung"))
        self.labelParameter1.setText(_translate("Form", "Filter nach Status:"))
        self.showDeleted.setText(_translate("Form", "Gelöschte Standardelemente"))
        self.showUserAdded.setText(_translate("Form", "Nur eigene Änderungen"))
        self.buttonCloseDB.setText(_translate("Form", "Hausregeln schließen"))
        self.buttonLoadDB.setText(_translate("Form", "Hausregeln laden"))
        self.buttonSaveDB.setText(_translate("Form", "Speichern als..."))
        self.buttonQuicksave.setText(_translate("Form", "Speichern"))
        self.buttonHinzufuegen.setToolTip(_translate("Form", "Hinzufügen"))
        self.buttonHinzufuegen.setText(_translate("Form", "Hinzufügen"))
        self.buttonEditieren.setToolTip(_translate("Form", "Editieren"))
        self.buttonEditieren.setText(_translate("Form", "Editieren"))
        self.buttonDuplizieren.setToolTip(_translate("Form", "Duplizieren"))
        self.buttonDuplizieren.setText(_translate("Form", "Duplizieren"))
        self.buttonLoeschen.setToolTip(_translate("Form", "Löschen"))
        self.buttonLoeschen.setText(_translate("Form", "Löschen"))
        self.buttonWiederherstellen.setToolTip(_translate("Form", "W"))
        self.buttonWiederherstellen.setText(_translate("Form", "Wiederherstellen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
