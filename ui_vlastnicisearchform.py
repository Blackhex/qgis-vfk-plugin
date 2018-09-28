# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_vlastnicisearchform.ui'
#
# Created: Fri Nov 20 17:51:01 2015
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


class Ui_VlastniciSearchForm(object):

    def setupUi(self, VlastniciSearchForm):
        VlastniciSearchForm.setObjectName("VlastniciSearchForm")
        VlastniciSearchForm.resize(238, 208)
        self.gridLayout = QGridLayout(VlastniciSearchForm)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QLabel(VlastniciSearchForm)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.jmenoLineEdit = QLineEdit(VlastniciSearchForm)
        self.jmenoLineEdit.setObjectName("jmenoLineEdit")
        self.gridLayout.addWidget(self.jmenoLineEdit, 0, 1, 1, 1)
        self.label_4 = QLabel(VlastniciSearchForm)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.ofoCheckBox = QCheckBox(VlastniciSearchForm)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ofoCheckBox.sizePolicy().hasHeightForWidth())
        self.ofoCheckBox.setSizePolicy(sizePolicy)
        self.ofoCheckBox.setChecked(True)
        self.ofoCheckBox.setObjectName("ofoCheckBox")
        self.gridLayout.addWidget(self.ofoCheckBox, 1, 1, 1, 1)
        self.opoCheckBox = QCheckBox(VlastniciSearchForm)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.opoCheckBox.sizePolicy().hasHeightForWidth())
        self.opoCheckBox.setSizePolicy(sizePolicy)
        self.opoCheckBox.setChecked(True)
        self.opoCheckBox.setObjectName("opoCheckBox")
        self.gridLayout.addWidget(self.opoCheckBox, 2, 1, 1, 1)
        self.sjmCheckBox = QCheckBox(VlastniciSearchForm)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sjmCheckBox.sizePolicy().hasHeightForWidth())
        self.sjmCheckBox.setSizePolicy(sizePolicy)
        self.sjmCheckBox.setChecked(True)
        self.sjmCheckBox.setObjectName("sjmCheckBox")
        self.gridLayout.addWidget(self.sjmCheckBox, 3, 1, 1, 1)
        self.label_2 = QLabel(VlastniciSearchForm)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)
        self.rcIcoLineEdit = QLineEdit(VlastniciSearchForm)
        self.rcIcoLineEdit.setObjectName("rcIcoLineEdit")
        self.gridLayout.addWidget(self.rcIcoLineEdit, 4, 1, 1, 1)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.label_3 = QLabel(VlastniciSearchForm)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.lvVlastniciLineEdit = QLineEdit(VlastniciSearchForm)
        self.lvVlastniciLineEdit.setObjectName("lvVlastniciLineEdit")
        self.gridLayout.addWidget(self.lvVlastniciLineEdit, 5, 1, 1, 1)

        self.retranslateUi(VlastniciSearchForm)
        QMetaObject.connectSlotsByName(VlastniciSearchForm)

    def retranslateUi(self, VlastniciSearchForm):
        VlastniciSearchForm.setWindowTitle(
            _translate("VlastniciSearchForm", "Form", None))
        self.label.setText(_translate("VlastniciSearchForm", "Jméno:", None))
        self.label_4.setText(
            _translate("VlastniciSearchForm", "Typ osoby:", None))
        self.ofoCheckBox.setText(
            _translate("VlastniciSearchForm", "OFO", None))
        self.opoCheckBox.setText(
            _translate("VlastniciSearchForm", "OPO", None))
        self.sjmCheckBox.setText(
            _translate("VlastniciSearchForm", "SJM", None))
        self.label_2.setText(
            _translate("VlastniciSearchForm", "RČ/IČO:", None))
        self.label_3.setText(_translate("VlastniciSearchForm", "LV:", None))
