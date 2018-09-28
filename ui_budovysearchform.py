# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_budovysearchform.ui'
#
# Created: Fri Nov 20 17:50:07 2015
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


class Ui_BudovySearchForm(object):

    def setupUi(self, BudovySearchForm):
        BudovySearchForm.setObjectName("BudovySearchForm")
        BudovySearchForm.resize(248, 190)
        self.gridLayout_2 = QGridLayout(BudovySearchForm)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QLabel(BudovySearchForm)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.label_2 = QLabel(BudovySearchForm)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QLabel(BudovySearchForm)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.cisloDomovniLineEdit = QLineEdit(BudovySearchForm)
        self.cisloDomovniLineEdit.setObjectName("cisloDomovniLineEdit")
        self.gridLayout_2.addWidget(self.cisloDomovniLineEdit, 0, 1, 1, 1)
        self.naParceleLineEdit = QLineEdit(BudovySearchForm)
        self.naParceleLineEdit.setObjectName("naParceleLineEdit")
        self.gridLayout_2.addWidget(self.naParceleLineEdit, 1, 1, 1, 1)
        self.label_4 = QLabel(BudovySearchForm)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.lvBudovyLineEdit = QLineEdit(BudovySearchForm)
        self.lvBudovyLineEdit.setObjectName("lvBudovyLineEdit")
        self.gridLayout_2.addWidget(self.lvBudovyLineEdit, 3, 1, 1, 1)
        self.mZpVyuzitiCombo = QComboBox(BudovySearchForm)
        self.mZpVyuzitiCombo.setObjectName("mZpVyuzitiCombo")
        self.gridLayout_2.addWidget(self.mZpVyuzitiCombo, 2, 1, 1, 1)

        self.retranslateUi(BudovySearchForm)
        QMetaObject.connectSlotsByName(BudovySearchForm)

    def retranslateUi(self, BudovySearchForm):
        BudovySearchForm.setWindowTitle(
            _translate("BudovySearchForm", "Form", None))
        self.label.setText(_translate("BudovySearchForm", "LV:", None))
        self.label_2.setText(
            _translate("BudovySearchForm", "Na parcele:", None))
        self.label_3.setText(
            _translate("BudovySearchForm", "Č. domovní:", None))
        self.label_4.setText(
            _translate("BudovySearchForm", "Zp. využití:", None))
