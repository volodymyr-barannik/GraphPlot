# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets, Qt
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QDoubleValidator, QFont, QRegExpValidator, QKeySequence, QIcon
from PyQt5.QtWidgets import QStatusBar, QShortcut, QMenuBar

from src.Constants import PLOT_BUTTON_BACKGROUND_COLOR, IMPORTANT_BUTTON_BACKGROUND_COLOR, MAIN_WINDOW_BACKGROUND_COLOR, \
    LINE_COLOR, LINE_TEXT_COLOR, LINE_PADDING, STATUSBAR_BACKGROUND_COLOR, STATUSBAR_BORDER_COLOR, STATUSBAR_TEXT_COLOR, \
    BUTTON_TEXT_COLOR, PLOT_BUTTON_TEXT_COLOR, LABEL_TEXT_COLOR, MAIN_WINDOW_TEXT_COLOR, QMENU_BACKGROUND_COLOR, \
    QMENU_SELECTED_ITEM_BACKGROUND_COLOR, QMENU_ENABLED_TEXT_COLOR, QMENUBAR_ITEM_BACKGROUND_COLOR, \
    QMENUBAR_ITEM_PRESSED_BACKGROUND_COLOR, QMENUBAR_BACKGROUND_COLOR, QMENUBAR_ITEM_TEXT_COLOR
from src.components.PlotWindow import windowPlot


class UI_MainWindow(object):
    def init_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
       # MainWindow.title()
        MainWindow.resize(528, 638)
        MainWindow.setWindowIcon(QIcon('res/icon.png'))
        MainWindow.setStyleSheet(""" 
                                #centralwidget {{
                                    background-color: {main_window_background_color};
                                }}     
                                                        
                                QMenuBar {{
                                    background-color: {qmenubar_background_color};
                                }}
                                
                                QMenuBar::item {{
                                    spacing: 3px;           
                                    padding: 2px 10px;
                                    background-color: {qmenubar_item_background_color};
                                    color: {qmenubar_item_text_color};  
                                    border-radius: 3px;
                                }}

                                QMenuBar::item:pressed {{
                                    background-color: {qmenubar_item_pressed_background_color};
                                }}  
                                
                                QMenu {{
                                    background-color: {qmenu_background_color};   
                                }}
                                
                                QMenu::item {{
                                    background-color: {qmenu_background_color};
                                }}
                                
                                QMenu::item:enabled {{
                                    background-color: {qmenu_background_color};
                                    color: {qmenu_enabled_text_color};
                                }}
                                
                                QMenu::item:selected {{
                                    background-color: {qmenu_selected_item_background_color};
                                    color: rgb(250,250,250);
                                }}
                                """
                                 .format(main_window_background_color = MAIN_WINDOW_BACKGROUND_COLOR,
                                         qmenubar_background_color = QMENUBAR_BACKGROUND_COLOR,
                                         qmenubar_item_text_color = QMENUBAR_ITEM_TEXT_COLOR,
                                         qmenu_background_color = QMENU_BACKGROUND_COLOR,
                                         qmenu_selected_item_background_color = QMENU_SELECTED_ITEM_BACKGROUND_COLOR,
                                         qmenu_enabled_text_color = QMENU_ENABLED_TEXT_COLOR,
                                         qmenubar_item_background_color = QMENUBAR_ITEM_BACKGROUND_COLOR,
                                         qmenubar_item_pressed_background_color = QMENUBAR_ITEM_PRESSED_BACKGROUND_COLOR
                                         ))

        self.colibri_font_AA_bold = QFont("Calibri Bold", 8)
        self.colibri_font_AA_bold.setStyleStrategy(QFont.PreferAntialias)

        self.colibri_font_AA_regular = QFont("Calibri", 8)
        self.colibri_font_AA_regular.setStyleStrategy(QFont.PreferAntialias)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0,0,0,0)
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
        self.leftToolsVBoxLayout.setSpacing(6)
        self.leftToolsVBoxLayout.setObjectName("leftToolsVBoxLayout")
        self.leftLineFormLayout = QtWidgets.QFormLayout()
        self.leftLineFormLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.leftLineFormLayout.setHorizontalSpacing(4)
        self.leftLineFormLayout.setVerticalSpacing(6)
        self.leftLineFormLayout.setObjectName("leftLineFormLayout")

        self.labelA = QtWidgets.QLabel(self.centralwidget)
        self.labelA.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelA.setObjectName("labelA")
        self.labelA.setStyleSheet("""QLabel {{color: {text_color};}}"""
                                 .format(text_color=LABEL_TEXT_COLOR))
        self.leftLineFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelA)

        self.lineA = QtWidgets.QLineEdit(self.centralwidget)
        self.lineA.setInputMask("")
        self.lineA.setPlaceholderText("")
        self.lineA.setClearButtonEnabled(False)
        self.lineA.setObjectName("lineA")
        self.lineA.setText("1")
        self.lineA.setValidator(QRegExpValidator(QRegExp("^((-?\d{0,16},\d{0,16})|(-?\d{0,16}))$")))
        self.lineA.setStyleSheet("""QLineEdit {{background-color: {background_color};
                                            border-style: none;
                                            border-width: 2px;
                                            border-radius: 3px;
                                            color: {font_color};
                                            padding: {line_padding};}}"""
                                 .format(background_color=LINE_COLOR, font_color=LINE_TEXT_COLOR,
                                         line_padding = LINE_PADDING))
        self.lineA.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lineA.setFont(self.colibri_font_AA_bold)
        self.leftLineFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineA)

        self.labelB = QtWidgets.QLabel(self.centralwidget)
        self.labelB.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelB.setObjectName("labelB")
        self.labelB.setStyleSheet("""QLabel {{color: {text_color};}}"""
                                 .format(text_color=LABEL_TEXT_COLOR))
        self.leftLineFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelB)

        self.lineB = QtWidgets.QLineEdit(self.centralwidget)
        self.lineB.setObjectName("lineB")
        self.lineB.setText("0,1")
        self.lineB.setValidator(QRegExpValidator(QRegExp("^((-?\d{0,16},\d{0,16})|(-?\d{0,16}))$")))
        self.lineB.setStyleSheet("""QLineEdit {{background-color: {background_color};
                                            border-style: none;
                                            border-width: 2px;
                                            border-radius: 3px;
                                            color: {font_color};
                                            padding: {line_padding};}}"""
                                 .format(background_color=LINE_COLOR, font_color=LINE_TEXT_COLOR,
                                         line_padding=LINE_PADDING))
        self.lineB.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lineB.setFont(self.colibri_font_AA_bold)
        self.leftLineFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineB)

        self.leftToolsVBoxLayout.addLayout(self.leftLineFormLayout)

        self.buttonPlot = QtWidgets.QPushButton(self.centralwidget)
        self.buttonPlot.setObjectName("buttonPlot")
        self.buttonPlot.setToolTip('Будує графік логарифмічної спіралі')
        self.buttonPlot.setStyleSheet("""QPushButton {{background-color: {background_color};
                                         border-style: none;
                                         border-width: 2px;
                                         border-radius: 3px;
                                         color: {text_color};
                                         padding: 4px;}}"""
                                      .format(background_color=PLOT_BUTTON_BACKGROUND_COLOR,
                                              text_color=PLOT_BUTTON_TEXT_COLOR))
        self.buttonPlot.setFont(self.colibri_font_AA_bold)
        self.leftToolsVBoxLayout.addWidget(self.buttonPlot)

        self.toolsHBoxLayout.addLayout(self.leftToolsVBoxLayout)
        self.rightToolsVBoxLayout = QtWidgets.QVBoxLayout()
        self.rightToolsVBoxLayout.setSpacing(6)
        self.rightToolsVBoxLayout.setObjectName("rightToolsVBoxLayout")
        self.rightLineFormLayout = QtWidgets.QFormLayout()
        self.rightLineFormLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.rightLineFormLayout.setHorizontalSpacing(4)
        self.rightLineFormLayout.setVerticalSpacing(6)
        self.rightLineFormLayout.setObjectName("rightLineFormLayout")

        self.labelRange = QtWidgets.QLabel(self.centralwidget)
        self.labelRange.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelRange.setObjectName("labelRange")
        self.labelRange.setStyleSheet("""QLabel {{color: {text_color};}}"""
                                      .format(text_color=LABEL_TEXT_COLOR))
        self.rightLineFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelRange)

        self.lineRange = QtWidgets.QLineEdit(self.centralwidget)
        self.lineRange.setObjectName("lineRange")
        self.lineRange.setText("[0; 4pi]")
        self.range_regexp = QRegExp("^(\[|\()\s?"
                               "((-?\d{0,16},\d{0,16})|(-?\d{0,16}))"
                               "((p?)|(pi));"
                               "\s?((-?\d{0,16},\d{0,16})|(-?\d{0,16}))"
                               "((p?)|(pi))\s?"
                               "(\]|\))$")
        self.lineRange.setValidator(QRegExpValidator(self.range_regexp))
        self.lineRange.setStyleSheet("""QLineEdit {{background-color: {background_color};
                                            border-style: none;
                                            border-width: 2px;
                                            border-radius: 3px;
                                            color: {font_color};
                                            padding: {line_padding};}}"""
                                 .format(background_color=LINE_COLOR, font_color=LINE_TEXT_COLOR,
                                         line_padding=LINE_PADDING))
        self.lineRange.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lineRange.setFont(self.colibri_font_AA_bold)
        self.rightLineFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineRange)

        self.labelStep = QtWidgets.QLabel(self.centralwidget)
        self.labelStep.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelStep.setObjectName("labelStep")
        self.labelStep.setStyleSheet("""QLabel {{color: {text_color};}}"""
                                      .format(text_color=LABEL_TEXT_COLOR))
        self.rightLineFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelStep)

        self.lineStep = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.lineStep.setObjectName("lineStep")
        self.lineStep.setDecimals(5)
        self.lineStep.setValue(0.01)
        self.lineStep.setMinimum(0.00001)
        self.lineStep.setSingleStep(0.01)
        self.lineStep.setStyleSheet("""QDoubleSpinBox {{background-color: {background_color};
                                             border-style: none;
                                             border-width: 2px;
                                             border-radius: 3px;
                                             color: {font_color};
                                             padding: {line_padding};}}
                                                    
                                         QDoubleSpinBox::up-button {{
                                             subcontrol-origin: border;
                                             subcontrol-position: top right;
                                        
                                             width: 16px;
                                             border-image: url('res/spinup.png');
                                             border-width: 1px;
                                         }}
                                        
                                         QDoubleSpinBox::down-button {{
                                             subcontrol-origin: border;
                                             subcontrol-position: bottom right;
                                        
                                             width: 16px;
                                             border-image: url('res/spindown.png');
                                             border-width: 1px;
                                             border-top-width: 0;
                                         }}"""
                                     .format(background_color=LINE_COLOR, font_color=LINE_TEXT_COLOR,
                                             line_padding=LINE_PADDING))
        self.lineStep.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lineStep.setFont(self.colibri_font_AA_bold)
        self.rightLineFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineStep)

        self.rightToolsVBoxLayout.addLayout(self.rightLineFormLayout)
        self.rightButtonsHBoxLayout = QtWidgets.QHBoxLayout()
        self.rightButtonsHBoxLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.rightButtonsHBoxLayout.setSpacing(6)
        self.rightButtonsHBoxLayout.setObjectName("rightButtonsHBoxLayout")

        self.buttonSave = QtWidgets.QPushButton(self.centralwidget)
        self.buttonSave.setObjectName("buttonSave")
        self.shortcutSave = QShortcut(QKeySequence('Ctrl+S'), MainWindow)
        self.buttonSave.setStyleSheet("""QPushButton {{background-color: {background_color};
                                      border-style: none;
                                      border-width: 2px;
                                      border-radius: 3px;
                                      color: {text_color};
                                      padding: 4px;}}"""
                                      .format(background_color=IMPORTANT_BUTTON_BACKGROUND_COLOR,
                                              text_color=BUTTON_TEXT_COLOR))
        self.buttonSave.setFont(self.colibri_font_AA_bold)
        self.rightButtonsHBoxLayout.addWidget(self.buttonSave)

        self.buttonQuit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonQuit.setObjectName("buttonQuit")
        self.buttonQuit.setStyleSheet("""QPushButton {{background-color: {background_color};
                                      border-style: none;
                                      border-width: 2px;
                                      border-radius: 3px;
                                      color: {text_color};
                                      padding: 4px;}}"""
                                      .format(background_color=IMPORTANT_BUTTON_BACKGROUND_COLOR,
                                              text_color=BUTTON_TEXT_COLOR))
        self.buttonQuit.setFont(self.colibri_font_AA_bold)
        self.rightButtonsHBoxLayout.addWidget(self.buttonQuit)

        self.rightToolsVBoxLayout.addLayout(self.rightButtonsHBoxLayout)
        self.toolsHBoxLayout.addLayout(self.rightToolsVBoxLayout)
        self.toolsHBoxLayout.setContentsMargins(20,20,20,6)
        self.verticalLayout.addLayout(self.toolsHBoxLayout)
        self.verticalLayout.setStretch(0, 1)


        self.statusBar = QStatusBar()
        self.statusBar.setSizeGripEnabled(False)
        self.statusBar.setFont(self.colibri_font_AA_regular)
        self.statusBar.setStyleSheet("""QStatusBar {{background-color: {background_color};
                                        border-top-style: solid;
                                        border-right-style: none;
                                        border-bottom-style: none;
                                        border-left-style: none;
                                        border-width: 2px;
                                        border-radius: 2px;
                                        border-color: {border_color};
                                        color: {text_color};
                                        padding: 0px;}}"""
                                     .format(background_color=STATUSBAR_BACKGROUND_COLOR,
                                             border_color=STATUSBAR_BORDER_COLOR,
                                             text_color=STATUSBAR_TEXT_COLOR))
        self.verticalLayout.addWidget(self.statusBar)

        self.menuBar = MainWindow.menuBar()
        self.menuBar.setFont(self.colibri_font_AA_regular)
        self.viewMenu = self.menuBar.addMenu('&View')

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Log Spiral Plotting Tool"))
        self.labelA.setText(_translate("MainWindow", "a ="))
        self.labelB.setText(_translate("MainWindow", "b ="))
        self.buttonPlot.setText(_translate("MainWindow", "Побудувати"))
        self.labelRange.setText(_translate("MainWindow", "φ ∈"))
        self.labelStep.setText(_translate("MainWindow", "Δφ ="))
        self.buttonSave.setText(_translate("MainWindow", "Зберегти"))
        self.buttonQuit.setText(_translate("MainWindow", "Вийти"))