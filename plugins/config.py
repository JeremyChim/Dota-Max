from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView
from ui.py.config import Ui_MainWindow

import os
import configparser


class ConfigWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """英雄文件选择器"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('环境配置器')
        self.statusbar.showMessage('初始化完成。 环境配置器：1.0.0')

        self.cf = None  # config file
        self.gp = None  # game path

        self.init()

    def init(self):
        """初始化"""

        # 初始化列宽
        header = self.treeWidget.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        self.treeWidget.setColumnWidth(0, 400)  # 设置第1列的宽度为 400
        self.treeWidget.setColumnWidth(1, 150)  # 设置第2列的宽度为 150

        # 读取配置文件
        if not os.path.exists('config.ini'):
            self.statusbar.showMessage(f'操作：读取配置失败，错误：配置文件config.ini不存在')

        else:
            try:
                self.cf = configparser.ConfigParser()
                self.cf.read('config.ini')
                self.gp = self.cf.get('path', 'game_path')

                # 读取游戏路径
                if not self.gp:
                    self.statusbar.showMessage(f'操作：读取游戏路径失败，错误：路径为空')
                else:
                    self.lineEdit.setText(self.gp)  # 写入路径栏中

            except Exception as e:
                self.statusbar.showMessage(f'操作：读取配置失败，错误：{e}')

        # 按钮事件绑定
        self.pushButton_2.clicked.connect(self.install)
        self.pushButton_3.clicked.connect(self.install)
        # 快捷键绑定
        self.pushButton_2.setShortcut('ctrl+i')
        self.pushButton_3.setShortcut('ctrl+c')

        # 将焦点设置到 pushButton_2
        self.pushButton_2.setFocus()

    def install(self):
        self.statusbar.showMessage('操作：安装环境成功')


if __name__ == '__main__':
    app = QApplication([])
    win = ConfigWin()
    win.show()
    app.exec()
