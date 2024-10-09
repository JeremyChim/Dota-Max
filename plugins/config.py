from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QFileDialog
from ui.py.config import Ui_MainWindow

import os
import configparser


class ConfigWin(QMainWindow, Ui_MainWindow):
    def __init__(self, url: str = ''):
        """英雄文件选择器"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('环境配置器')
        self.statusbar.showMessage('初始化完成。 环境配置器：1.0.0')

        self.url = url
        self.cf = configparser.ConfigParser()  # config file
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
        if not os.path.exists(self.url):
            self.statusbar.showMessage(f'操作：读取配置失败，错误：配置文件config.ini不存在')

        else:
            try:
                self.cf.read(self.url)
                path = self.cf.get('path', 'game_path')

                # 读取游戏路径
                if not path:
                    self.statusbar.showMessage(f'操作：读取游戏路径失败，错误：路径为空')
                else:
                    self.lineEdit.setText(path)  # 写入路径栏中

            except Exception as e:
                self.statusbar.showMessage(f'操作：读取配置失败，错误：{e}')

        # 按钮事件绑定
        self.action_5.triggered.connect(self.save_as)
        self.pushButton.clicked.connect(self.choose)
        self.pushButton_2.clicked.connect(self.install)
        self.pushButton_3.clicked.connect(self.check)
        # 快捷键绑定
        self.action_5.setShortcut('shift+ctrl+s')
        self.pushButton.setShortcut('ctrl+l')
        self.pushButton_2.setShortcut('ctrl+i')
        self.pushButton_3.setShortcut('ctrl+c')

        # 将焦点设置到 pushButton_2
        self.pushButton_2.setFocus()

    def install(self):
        self.statusbar.showMessage('操作：安装环境成功')

    def check(self):
        self.statusbar.showMessage('操作：检查环境成功')

    def choose(self):
        url = QFileDialog.getExistingDirectory(self, "选择文件夹", self.lineEdit.text())
        if url:
            self.lineEdit.setText(url)
            self.statusbar.showMessage(f'操作：载入路径成功，路径：{url}')

    def load(self):
        pass

    def save_as(self):
        """另存文件"""
        url, _ = QFileDialog.getSaveFileName(self, "保存文件", 'config.ini', "配置文件 (*.ini);;所有文件 (*)")
        path = self.lineEdit.text()  # 游戏配置路径，捕获路径栏
        if not path:
            self.statusbar.showMessage(f'操作：保存配置失败，配置路径为空')

        else:
            try:
                with open(url, 'w') as f:
                    self.cf['path'] = {'game_path': path}
                    self.cf.write(f)
                    self.statusbar.showMessage(f'操作：保存配置成功，路径：{url}')
            except Exception as e:
                self.statusbar.showMessage(f'操作：保存配置失败，错误：{e}')


if __name__ == '__main__':
    app = QApplication([])
    win = ConfigWin('../config/config.ini')
    win.show()
    app.exec()
