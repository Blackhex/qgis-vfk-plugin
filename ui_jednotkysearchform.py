# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_jednotkysearchform.ui'
#
# Created: Fri Nov 20 17:50:26 2015
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


class Ui_JednotkySearchForm(object):

    def setupUi(self, JednotkySearchForm):
        JednotkySearchForm.setObjectName("JednotkySearchForm")
        JednotkySearchForm.resize(248, 181)
        self.gridLayout = QGridLayout(JednotkySearchForm)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QLabel(JednotkySearchForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QLabel(JednotkySearchForm)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QLabel(JednotkySearchForm)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_4 = QLabel(JednotkySearchForm)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_5 = QLabel(JednotkySearchForm)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.mCisloJednotkyLineEdit = QLineEdit(JednotkySearchForm)
        self.mCisloJednotkyLineEdit.setObjectName("mCisloJednotkyLineEdit")
        self.gridLayout.addWidget(self.mCisloJednotkyLineEdit, 0, 1, 1, 1)
        self.mCisloDomovniLineEdit = QLineEdit(JednotkySearchForm)
        self.mCisloDomovniLineEdit.setObjectName("mCisloDomovniLineEdit")
        self.gridLayout.addWidget(self.mCisloDomovniLineEdit, 1, 1, 1, 1)
        self.mNaParceleLineEdit = QLineEdit(JednotkySearchForm)
        self.mNaParceleLineEdit.setObjectName("mNaParceleLineEdit")
        self.gridLayout.addWidget(self.mNaParceleLineEdit, 2, 1, 1, 1)
        self.mLvJednotkyLineEdit = QLineEdit(JednotkySearchForm)
        self.mLvJednotkyLineEdit.setObjectName("mLvJednotkyLineEdit")
        self.gridLayout.addWidget(self.mLvJednotkyLineEdit, 4, 1, 1, 1)
        self.mZpVyuzitiCombo = QComboBox(JednotkySearchForm)
        self.mZpVyuzitiCombo.setObjectName("mZpVyuzitiCombo")
        self.gridLayout.addWidget(self.mZpVyuzitiCombo, 3, 1, 1, 1)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)

        self.retranslateUi(JednotkySearchForm)
        QMetaObject.connectSlotsByName(JednotkySearchForm)

    def retranslateUi(self, JednotkySearchForm):
        JednotkySearchForm.setWindowTitle(
            _translate("JednotkySearchForm", "Form", None))
        self.label.setText(
            _translate("JednotkySearchForm", "Č. jednotky:", None))
        self.label_2.setText(
            _translate("JednotkySearchForm", "Č. domovní:", None))
        self.label_3.setText(
            _translate("JednotkySearchForm", "Na parcele:", None))
        self.label_4.setText(
            _translate("JednotkySearchForm", "Zp. využití:", None))
        self.label_5.setText(_translate("JednotkySearchForm", "LV:", None))
