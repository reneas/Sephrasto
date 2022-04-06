# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CharakterVorteile.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(701, 460)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.treeWidget = QtWidgets.QTreeWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.treeWidget.setTabKeyNavigation(True)
        self.treeWidget.setProperty("showDropIndicator", False)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setAnimated(False)
        self.treeWidget.setAllColumnsShowFocus(True)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(100)
        self.treeWidget.header().setHighlightSections(False)
        self.treeWidget.header().setMinimumSectionSize(80)
        self.treeWidget.header().setStretchLastSection(False)
        self.scrollArea = QtWidgets.QScrollArea(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 0))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 340, 394))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelKosten = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelKosten.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelKosten.setObjectName("labelKosten")
        self.gridLayout_2.addWidget(self.labelKosten, 3, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.plainText = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainText.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.plainText.setLineWidth(1)
        self.plainText.setReadOnly(True)
        self.plainText.setBackgroundVisible(False)
        self.plainText.setObjectName("plainText")
        self.gridLayout_2.addWidget(self.plainText, 5, 0, 1, 2)
        self.labelVorteil = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelVorteil.setFont(font)
        self.labelVorteil.setObjectName("labelVorteil")
        self.gridLayout_2.addWidget(self.labelVorteil, 0, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 4, 0, 1, 1)
        self.labelNachkauf = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelNachkauf.setMinimumSize(QtCore.QSize(0, 18))
        self.labelNachkauf.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelNachkauf.setObjectName("labelNachkauf")
        self.gridLayout_2.addWidget(self.labelNachkauf, 4, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.labelVoraussetzungen = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelVoraussetzungen.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelVoraussetzungen.setWordWrap(True)
        self.labelVoraussetzungen.setObjectName("labelVoraussetzungen")
        self.gridLayout_2.addWidget(self.labelVoraussetzungen, 2, 1, 1, 1)
        self.labelTyp = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.labelTyp.setMinimumSize(QtCore.QSize(0, 18))
        font = QtGui.QFont()
        font.setItalic(True)
        self.labelTyp.setFont(font)
        self.labelTyp.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelTyp.setObjectName("labelTyp")
        self.gridLayout_2.addWidget(self.labelTyp, 1, 0, 1, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.checkShowAll = QtWidgets.QCheckBox(Form)
        self.checkShowAll.setObjectName("checkShowAll")
        self.gridLayout.addWidget(self.checkShowAll, 2, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.treeWidget, self.scrollArea)
        Form.setTabOrder(self.scrollArea, self.plainText)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "Vorteil"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Kosten"))
        self.labelKosten.setText(_translate("Form", "20 EP"))
        self.label_2.setText(_translate("Form", "Kosten:"))
        self.labelVorteil.setText(_translate("Form", "Vorteil"))
        self.label.setText(_translate("Form", "Nachkauf:"))
        self.labelNachkauf.setText(_translate("Form", "Häufig"))
        self.label_3.setText(_translate("Form", "Voraussetzungen:"))
        self.labelVoraussetzungen.setText(_translate("Form", "keine"))
        self.labelTyp.setText(_translate("Form", "Allgemeine Vorteile"))
        self.checkShowAll.setToolTip(_translate("Form", "Falls diese Option aktiviert ist, werden auch solche Vorteile angezeigt, für die du die Voraussetzungen nicht erfüllst."))
        self.checkShowAll.setText(_translate("Form", "Alle Vorteile anzeigen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
