# Form implementation generated from reading ui file 'ab_edit.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1029, 862)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listView = QtWidgets.QListView(parent=self.centralwidget)
        self.listView.setStyleSheet("font: 700 italic 10pt \"JetBrains Mono\";")
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_14 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setProperty("value", 25)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_3.addWidget(self.spinBox_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_3.setMaximum(1000)
        self.spinBox_3.setProperty("value", 25)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_3.addWidget(self.spinBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_4.addWidget(self.checkBox_2)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.spinBox_4 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_4.setMaximum(1000)
        self.spinBox_4.setProperty("value", 100)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_4.addWidget(self.spinBox_4)
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_4.addWidget(self.pushButton_5)
        self.spinBox_5 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_5.setMaximum(1000)
        self.spinBox_5.setProperty("value", 50)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_4.addWidget(self.spinBox_5)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_9.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_5.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_5.addWidget(self.pushButton_7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_6.addWidget(self.pushButton_8)
        self.pushButton_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_6.addWidget(self.pushButton_9)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton_10 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_7.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_7.addWidget(self.pushButton_11)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_12 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_8.addWidget(self.pushButton_12)
        self.pushButton_13 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_8.addWidget(self.pushButton_13)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9.addLayout(self.verticalLayout_2)
        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1029, 24))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setCheckable(False)
        self.action.setEnabled(True)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setCheckable(False)
        self.action_4.setChecked(False)
        self.action_4.setEnabled(True)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        self.action_5.setCheckable(True)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtGui.QAction(parent=MainWindow)
        self.action_6.setObjectName("action_6")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "自动识别"))
        self.radioButton_2.setText(_translate("MainWindow", "{ }格式"))
        self.radioButton_3.setText(_translate("MainWindow", "“ ”格式"))
        self.pushButton.setText(_translate("MainWindow", "增强"))
        self.pushButton_14.setText(_translate("MainWindow", "减CD"))
        self.checkBox.setText(_translate("MainWindow", "魔晶"))
        self.pushButton_2.setText(_translate("MainWindow", "+"))
        self.pushButton_3.setText(_translate("MainWindow", "-"))
        self.checkBox_2.setText(_translate("MainWindow", "A 杖"))
        self.pushButton_4.setText(_translate("MainWindow", "+"))
        self.pushButton_5.setText(_translate("MainWindow", "-"))
        self.pushButton_6.setText(_translate("MainWindow", "←"))
        self.pushButton_7.setText(_translate("MainWindow", "→"))
        self.pushButton_8.setText(_translate("MainWindow", "剪切"))
        self.pushButton_9.setText(_translate("MainWindow", "粘贴"))
        self.pushButton_10.setText(_translate("MainWindow", "清空剪切板"))
        self.pushButton_11.setText(_translate("MainWindow", "撤回"))
        self.pushButton_12.setText(_translate("MainWindow", "另存"))
        self.pushButton_13.setText(_translate("MainWindow", "打开已保存"))
        self.menu.setTitle(_translate("MainWindow", "控制台"))
        self.action.setText(_translate("MainWindow", "打开根目录"))
        self.action_2.setText(_translate("MainWindow", "载入数据"))
        self.action_3.setText(_translate("MainWindow", "保存数据"))
        self.action_4.setText(_translate("MainWindow", "另存数据"))
        self.action_5.setText(_translate("MainWindow", "置顶窗口"))
        self.action_6.setText(_translate("MainWindow", "保存数据"))
