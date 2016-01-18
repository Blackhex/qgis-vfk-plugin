# -*- coding: utf-8 -*-

"""
/***************************************************************************
 vfkPluginDialog
                                 A QGIS plugin
 Plugin umoznujici praci s daty katastru nemovitosti
                             -------------------
        begin                : 2015-06-11
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Stepan Bambula
        email                : stepan.bambula@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtGui import *
from PyQt4.QtCore import QAbstractItemModel, QModelIndex, QRegExp, SIGNAL, SLOT

from ui_parcelysearchform import *


class ParcelySearchForm(QWidget):
    def __init__(self, parent=None):
        super(ParcelySearchForm, self).__init__(parent)
        # Set up the user interface from Designer.
        self.ui = Ui_ParcelySearchForm()
        self.ui.setupUi(self)

        self.__defaultModel = QAbstractItemModel
        self.__stavebniModel = QAbstractItemModel
        self.__pozemkovaModel = QAbstractItemModel

        self.connect(self.ui.typParcelyCombo, SIGNAL("currentIndexChanged(int)"), self.__setDruhModel)
        self.rx = QRegExp("[0-9]*/?[0-9]*")
        self.validator = QRegExpValidator(self.rx)
        self.ui.parCisloLineEdit.setValidator(self.validator)

    def parcelniCislo(self):
        return unicode(self.ui.parCisloLineEdit.text()).strip()

    def lv(self):
        return unicode(self.ui.lvParcelyLineEdit.text()).strip()

    def setDruhPozemkuModel(self, model):
        """

        :param model: QAbstractItemModel
        """
        self.__defaultModel = model
        self.__pozemkovaModel = model
        self.__stavebniModel = model
        self.ui.druhPozemkuCombo.setModel(model)
        self.ui.druhPozemkuCombo.setModelColumn(1)

    def __setDruhModel(self):
        if self.ui.typParcelyCombo.currentIndex() == 1:
            self.ui.druhPozemkuCombo.setModel(self.__pozemkovaModel)
        elif self.ui.typParcelyCombo.currentIndex() == 2:
            self.ui.druhPozemkuCombo.setModel(self.__stavebniModel)
        else:
            self.ui.druhPozemkuCombo.setModel(self.__defaultModel)

    def setDruhPozemkuStavebniModel(self, model):
        """

        :param model: QAbstractItemModel
        """
        self.__stavebniModel = model

    def setDruhPozemkuPozemkovaModel(self, model):
        """

        :param model: QAbstractItemModel
        """
        self.__pozemkovaModel = model

    def typParcely(self):
        return self.ui.typParcelyCombo.currentIndex()

    def druhPozemkuKod(self):
        row = self.ui.druhPozemkuCombo.currentIndex()
        index = self.ui.druhPozemkuCombo.model().index(row, 0)
        return self.ui.druhPozemkuCombo.model().data(index)
