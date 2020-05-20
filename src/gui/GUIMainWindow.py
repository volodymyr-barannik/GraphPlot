# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QDoubleValidator

from src.components.PlotWindow import windowPlot


class UI_MainWindow(object):
    def init_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 638)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.windowPlotObject = windowPlot(self.centralwidget)
        self.windowPlotObject.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.windowPlotObject.sizePolicy().hasHeightForWidth())
        self.windowPlotObject.setSizePolicy(sizePolicy)
        self.windowPlotObject.setMinimumSize(QtCore.QSize(300, 300))
        self.windowPlotObject.setObjectName("windowPlotObject")
        self.verticalLayout.addWidget(self.windowPlotObject)

        self.toolsHBoxLayout = QtWidgets.QHBoxLayout()
        self.toolsHBoxLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.toolsHBoxLayout.setSpacing(20)
        self.toolsHBoxLayout.setObjectName("toolsHBoxLayout")
        self.leftToolsVBoxLayout = QtWidgets.QVBoxLayout()
        self.leftToolsVBoxLayout.setSpacing(5)
        self.leftToolsVBoxLayout.setObjectName("leftToolsVBoxLayout")
        self.leftLineFormLayout = QtWidgets.QFormLayout()
        self.leftLineFormLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leftLineFormLayout.setHorizontalSpacing(4)
        self.leftLineFormLayout.setVerticalSpacing(6)
        self.leftLineFormLayout.setObjectName("leftLineFormLayout")

        self.labelA = QtWidgets.QLabel(self.centralwidget)
        self.labelA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelA.setObjectName("labelA")
        self.leftLineFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelA)

        self.lineA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineA.setInputMask("")
        self.lineA.setText("")
        self.lineA.setPlaceholderText("")
        self.lineA.setClearButtonEnabled(False)
        self.lineA.setObjectName("lineA")
        self.lineA.setText("1")
        self.lineA.setValidator(QDoubleValidator())

        self.leftLineFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineA)
        self.labelB = QtWidgets.QLabel(self.centralwidget)
        self.labelB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelB.setObjectName("labelB")
        self.leftLineFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelB)

        self.lineB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineB.setObjectName("lineB")
        self.lineB.setText("0,1")
        self.lineB.setValidator(QDoubleValidator())
        self.leftLineFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineB)

        self.leftToolsVBoxLayout.addLayout(self.leftLineFormLayout)

        self.buttonPlot = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPlot.setObjectName("buttonPlot")
        self.buttonPlot.setToolTip('Будує графік')
        self.leftToolsVBoxLayout.addWidget(self.buttonPlot)

        self.toolsHBoxLayout.addLayout(self.leftToolsVBoxLayout)
        self.rightToolsVBoxLayout = QtWidgets.QVBoxLayout()
        self.rightToolsVBoxLayout.setSpacing(5)
        self.rightToolsVBoxLayout.setObjectName("rightToolsVBoxLayout")
        self.rightLineFormLayout = QtWidgets.QFormLayout()
        self.rightLineFormLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rightLineFormLayout.setHorizontalSpacing(4)
        self.rightLineFormLayout.setVerticalSpacing(6)
        self.rightLineFormLayout.setObjectName("rightLineFormLayout")
        self.labelRange = QtWidgets.QLabel(self.centralwidget)

        self.labelRange.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelRange.setObjectName("labelRange")
        self.rightLineFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelRange)

        self.lineRange = QtWidgets.QLineEdit(self.centralwidget)
        self.lineRange.setObjectName("lineRange")
        self.rightLineFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineRange)

        self.labelStep = QtWidgets.QLabel(self.centralwidget)
        self.labelStep.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelStep.setObjectName("labelStep")
        self.rightLineFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelStep)

        self.lineStep = QtWidgets.QLineEdit(self.centralwidget)
        self.lineStep.setObjectName("lineStep")
        self.lineStep.setText("0,01")
        self.lineStep.setValidator(QDoubleValidator())
        self.rightLineFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineStep)

        self.rightToolsVBoxLayout.addLayout(self.rightLineFormLayout)
        self.rightButtonsHBoxLayout = QtWidgets.QHBoxLayout()
        self.rightButtonsHBoxLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.rightButtonsHBoxLayout.setSpacing(4)
        self.rightButtonsHBoxLayout.setObjectName("rightButtonsHBoxLayout")

        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setObjectName("buttonSave")
        self.rightButtonsHBoxLayout.addWidget(self.buttonSave)

        self.buttonQuit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonQuit.setObjectName("buttonQuit")
        self.rightButtonsHBoxLayout.addWidget(self.buttonQuit)

        self.rightToolsVBoxLayout.addLayout(self.rightButtonsHBoxLayout)
        self.toolsHBoxLayout.addLayout(self.rightToolsVBoxLayout)
        self.verticalLayout.addLayout(self.toolsHBoxLayout)
        self.verticalLayout.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelA.setText(_translate("MainWindow", "a ="))
        self.labelB.setText(_translate("MainWindow", "b ="))
        self.buttonPlot.setText(_translate("MainWindow", "Побудувати"))
        self.labelRange.setText(_translate("MainWindow", "φ ∈"))
        self.labelStep.setText(_translate("MainWindow", "Δφ ="))
        self.buttonSave.setText(_translate("MainWindow", "Зберегти"))
        self.buttonQuit.setText(_translate("MainWindow", "Вийти"))