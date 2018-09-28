# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_parcelysearchform.ui'
#
# Created: Fri Nov 20 17:50:47 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

try:
    _encoding = QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig)


class Ui_ParcelySearchForm(object):

    def setupUi(self, ParcelySearchForm):
        ParcelySearchForm.setObjectName("ParcelySearchForm")
        ParcelySearchForm.resize(269, 168)
        self.gridLayout = QGridLayout(ParcelySearchForm)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QLabel(ParcelySearchForm)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.parCisloLineEdit = QLineEdit(ParcelySearchForm)
        self.parCisloLineEdit.setInputMask("")
        self.parCisloLineEdit.setObjectName("parCisloLineEdit")
        self.gridLayout.addWidget(self.parCisloLineEdit, 0, 1, 1, 1)
        self.label_5 = QLabel(ParcelySearchForm)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.typParcelyCombo = QComboBox(ParcelySearchForm)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.typParcelyCombo.sizePolicy().hasHeightForWidth())
        self.typParcelyCombo.setSizePolicy(sizePolicy)
        self.typParcelyCombo.setObjectName("typParcelyCombo")
        self.typParcelyCombo.addItem("")
        self.typParcelyCombo.addItem("")
        self.typParcelyCombo.addItem("")
        self.gridLayout.addWidget(self.typParcelyCombo, 1, 1, 1, 1)
        self.label_6 = QLabel(ParcelySearchForm)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.druhPozemkuCombo = QComboBox(ParcelySearchForm)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.druhPozemkuCombo.sizePolicy().hasHeightForWidth())
        self.druhPozemkuCombo.setSizePolicy(sizePolicy)
        self.druhPozemkuCombo.setObjectName("druhPozemkuCombo")
        self.gridLayout.addWidget(self.druhPozemkuCombo, 2, 1, 1, 1)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 1)
        self.lvParcelyLineEdit = QLineEdit(ParcelySearchForm)
        self.lvParcelyLineEdit.setObjectName("lvParcelyLineEdit")
        self.gridLayout.addWidget(self.lvParcelyLineEdit, 3, 1, 1, 1)
        self.label = QLabel(ParcelySearchForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)

        self.retranslateUi(ParcelySearchForm)
        QMetaObject.connectSlotsByName(ParcelySearchForm)

    def retranslateUi(self, ParcelySearchForm):
        ParcelySearchForm.setWindowTitle(_translate("ParcelySearchForm", "Form", None))
        self.label_3.setText(_translate("ParcelySearchForm", "Parcelní číslo :", None))
        self.label_5.setText(_translate("ParcelySearchForm", "Typ parcely:", None))
        self.typParcelyCombo.setItemText(0, _translate("ParcelySearchForm", "libovolný", None))
        self.typParcelyCombo.setItemText(1, _translate("ParcelySearchForm", "pozemková", None))
        self.typParcelyCombo.setItemText(2, _translate("ParcelySearchForm", "stavební", None))
        self.label_6.setText(_translate("ParcelySearchForm", "Druh pozemku:", None))
        self.label.setText(_translate("ParcelySearchForm", "LV:", None))
