# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_form.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(719, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.centralWidget.setFont(font)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tableView_shifts = QtWidgets.QTableView(self.centralWidget)
        self.tableView_shifts.setMinimumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tableView_shifts.setFont(font)
        self.tableView_shifts.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableView_shifts.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView_shifts.setObjectName("tableView_shifts")
        self.horizontalLayout_2.addWidget(self.tableView_shifts)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 719, 29))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menuBar.setFont(font)
        self.menuBar.setObjectName("menuBar")
        self.menu_Tariffs = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menu_Tariffs.setFont(font)
        self.menu_Tariffs.setObjectName("menu_Tariffs")
        self.menu_settingTariffs = QtWidgets.QMenu(self.menu_Tariffs)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menu_settingTariffs.setFont(font)
        self.menu_settingTariffs.setObjectName("menu_settingTariffs")
        self.menuShifts = QtWidgets.QMenu(self.menuBar)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.menuShifts.setFont(font)
        self.menuShifts.setObjectName("menuShifts")
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setSizeGripEnabled(True)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.dockWidget_setting = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.
                                           MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_setting.sizePolicy().hasHeightForWidth())
        self.dockWidget_setting.setSizePolicy(sizePolicy)
        self.dockWidget_setting.setMinimumSize(QtCore.QSize(250, 284))
        self.dockWidget_setting.setMaximumSize(QtCore.QSize(250, 300))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dockWidget_setting.setFont(font)
        self.dockWidget_setting.setFeatures(
            QtWidgets.QDockWidget.DockWidgetClosable | QtWidgets.QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget_setting.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea)
        self.dockWidget_setting.setObjectName("dockWidget_setting")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateEdit_shifts = QtWidgets.QDateEdit(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.dateEdit_shifts.sizePolicy().hasHeightForWidth())
        self.dateEdit_shifts.setSizePolicy(sizePolicy)
        self.dateEdit_shifts.setMinimumSize(QtCore.QSize(200, 30))
        self.dateEdit_shifts.setMaximumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.dateEdit_shifts.setFont(font)
        self.dateEdit_shifts.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.dateEdit_shifts.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.dateEdit_shifts.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit_shifts.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit_shifts.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_shifts.setCalendarPopup(True)
        self.dateEdit_shifts.setObjectName("dateEdit_shifts")
        self.verticalLayout.addWidget(self.dateEdit_shifts)
        self.comboBox_setting = QtWidgets.QComboBox(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_setting.sizePolicy().hasHeightForWidth())
        self.comboBox_setting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.comboBox_setting.setFont(font)
        self.comboBox_setting.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.comboBox_setting.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_setting.setEditable(False)
        self.comboBox_setting.setMaxCount(10)
        self.comboBox_setting.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_setting.setMinimumContentsLength(5)
        self.comboBox_setting.setModelColumn(0)
        self.comboBox_setting.setObjectName("comboBox_setting")
        self.verticalLayout.addWidget(self.comboBox_setting)
        self.tableView_setting = QtWidgets.QTableView(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView_setting.sizePolicy().hasHeightForWidth())
        self.tableView_setting.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tableView_setting.setFont(font)
        self.tableView_setting.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.tableView_setting.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.tableView_setting.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableView_setting.setObjectName("tableView_setting")
        self.tableView_setting.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout.addWidget(self.tableView_setting, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.dockWidget_setting.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_setting)
        self.dockWidget_salaryShow = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.
                                           MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_salaryShow.sizePolicy().hasHeightForWidth())
        self.dockWidget_salaryShow.setSizePolicy(sizePolicy)
        self.dockWidget_salaryShow.setFeatures(
            QtWidgets.QDockWidget.DockWidgetClosable | QtWidgets.QDockWidget.DockWidgetVerticalTitleBar)
        self.dockWidget_salaryShow.setAllowedAreas(QtCore.Qt.RightDockWidgetArea)
        self.dockWidget_salaryShow.setObjectName("dockWidget_salaryShow")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.dockWidgetContents_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(10, 20, 10, 10)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_salaryOfMonth = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label_salaryOfMonth.setText("")
        self.label_salaryOfMonth.setObjectName("label_salaryOfMonth")
        self.verticalLayout_2.addWidget(self.label_salaryOfMonth)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.dockWidget_salaryShow.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget_salaryShow)
        self.action_addTariff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_addTariff.setFont(font)
        self.action_addTariff.setObjectName("action_addTariff")
        self.action_removeTariff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_removeTariff.setFont(font)
        self.action_removeTariff.setObjectName("action_removeTariff")
        self.action_addRow = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_addRow.setFont(font)
        self.action_addRow.setObjectName("action_addRow")
        self.action_removeRow = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_removeRow.setFont(font)
        self.action_removeRow.setObjectName("action_removeRow")
        self.action_saveTariff = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_saveTariff.setFont(font)
        self.action_saveTariff.setObjectName("action_saveTariff")
        self.action_saveSettings = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("C059 [UKWN]")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.action_saveSettings.setFont(font)
        self.action_saveSettings.setObjectName("action_saveSettings")
        self.action_addShift = QtWidgets.QAction(MainWindow)
        self.action_addShift.setObjectName("action_addShift")
        self.action_removeShift = QtWidgets.QAction(MainWindow)
        self.action_removeShift.setObjectName("action_removeShift")
        self.action_calculationShift = QtWidgets.QAction(MainWindow)
        self.action_calculationShift.setObjectName("action_calculationShift")
        self.action_saveData = QtWidgets.QAction(MainWindow)
        self.action_saveData.setObjectName("action_saveData")
        self.menu_settingTariffs.addAction(self.action_addRow)
        self.menu_settingTariffs.addAction(self.action_removeRow)
        self.menu_settingTariffs.addSeparator()
        self.menu_settingTariffs.addAction(self.action_saveTariff)
        self.menu_settingTariffs.addAction(self.action_saveSettings)
        self.menu_Tariffs.addAction(self.action_addTariff)
        self.menu_Tariffs.addAction(self.action_removeTariff)
        self.menu_Tariffs.addSeparator()
        self.menu_Tariffs.addAction(self.menu_settingTariffs.menuAction())
        self.menuShifts.addAction(self.action_addShift)
        self.menuShifts.addAction(self.action_removeShift)
        self.menuShifts.addSeparator()
        self.menuShifts.addAction(self.action_calculationShift)
        self.menuShifts.addAction(self.action_saveData)
        self.menuBar.addAction(self.menu_Tariffs.menuAction())
        self.menuBar.addAction(self.menuShifts.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Моя зарплата в такси"))
        self.menu_Tariffs.setTitle(_translate("MainWindow", "Тарифы"))
        self.menu_settingTariffs.setTitle(_translate("MainWindow", "Настроить тарифы"))
        self.menuShifts.setTitle(_translate("MainWindow", "Смены"))
        self.dockWidget_setting.setWindowTitle(_translate("MainWindow", "Настройки тарифов"))
        self.dateEdit_shifts.setDisplayFormat(_translate("MainWindow", "dd.MM.yy"))
        self.dockWidget_salaryShow.setWindowTitle(_translate("MainWindow", "Доход"))
        self.label_2.setText(_translate("MainWindow", "Доход за месяц"))
        self.action_addTariff.setText(_translate("MainWindow", "Добавить тариф"))
        self.action_removeTariff.setText(_translate("MainWindow", "Удалить тариф"))
        self.action_addRow.setText(_translate("MainWindow", "Добвить строку"))
        self.action_removeRow.setText(_translate("MainWindow", "Удалить строку"))
        self.action_saveTariff.setText(_translate("MainWindow", "Сохранить тариф"))
        self.action_saveSettings.setText(_translate("MainWindow", "Сохранить настройки"))
        self.action_addShift.setText(_translate("MainWindow", "Добавить смену"))
        self.action_removeShift.setText(_translate("MainWindow", "Удалить смену"))
        self.action_calculationShift.setText(_translate("MainWindow", "Расчитать смену"))
        self.action_saveData.setText(_translate("MainWindow", "Сохранить данные"))
