# Form implementation generated from reading ui file 'config.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 363)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.treeWidget = QtWidgets.QTreeWidget(parent=self.centralwidget)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item_1.setBackground(0, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_1.setForeground(0, brush)
        item_1.setCheckState(0, QtCore.Qt.CheckState.Checked)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_1.setBackground(1, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.NoBrush)
        item_1.setForeground(1, brush)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item_1.setBackground(0, brush)
        item_1.setCheckState(0, QtCore.Qt.CheckState.Checked)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item_0.setBackground(0, brush)
        item_0.setCheckState(0, QtCore.Qt.CheckState.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item_1.setBackground(0, brush)
        item_1.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item_0.setBackground(0, brush)
        item_0.setCheckState(0, QtCore.Qt.CheckState.Checked)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        item_1.setBackground(0, brush)
        item_1.setCheckState(0, QtCore.Qt.CheckState.Unchecked)
        self.treeWidget.header().setDefaultSectionSize(300)
        self.verticalLayout.addWidget(self.treeWidget)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 650, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtGui.QAction(parent=MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtGui.QAction(parent=MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtGui.QAction(parent=MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtGui.QAction(parent=MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtGui.QAction(parent=MainWindow)
        self.action_5.setObjectName("action_5")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addAction(self.action_3)
        self.menu.addAction(self.action_5)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "游戏路径"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", ".../Steam/steamapps/common/dota 2 beta/game"))
        self.pushButton.setText(_translate("MainWindow", "..."))
        self.pushButton_4.setText(_translate("MainWindow", "→"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "文件名"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "修改时间"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "dota"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "gameinfo.gi"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("MainWindow", "2024‎/9/‎12‎/ ‎17:50"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "gameinfo_branchspecific.gi"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "mod"))
        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "pak01_dir.vpk"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "DotaThoughts"))
        self.treeWidget.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "pak01_dir.vpk"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_2.setText(_translate("MainWindow", "安装环境"))
        self.pushButton_3.setText(_translate("MainWindow", "检查环境"))
        self.menu.setTitle(_translate("MainWindow", "控制台"))
        self.action.setText(_translate("MainWindow", "打开根目录"))
        self.action_2.setText(_translate("MainWindow", "载入配置"))
        self.action_3.setText(_translate("MainWindow", "保存配置"))
        self.action_4.setText(_translate("MainWindow", "另存配置"))
        self.action_5.setText(_translate("MainWindow", "另存配置"))
