from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QFileDialog
from ui.py.config import Ui_MainWindow

import configparser
import os
import shutil
import time


class ConfigWin(QMainWindow, Ui_MainWindow):
    def __init__(self, url: str = None):
        """
        环境配置器
        :param url: config.ini的路径
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('环境配置器')
        self.statusbar.showMessage('初始化完成。 环境配置器：1.0.0')

        self.url = url  # config.ini 配置文件
        self.cf = configparser.ConfigParser()  # cf
        self.init()

    def init(self):
        """初始化"""

        # 初始化列宽
        header = self.treeWidget.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        self.treeWidget.setColumnWidth(0, 400)  # 设置第1列的宽度为 400
        self.treeWidget.setColumnWidth(1, 150)  # 设置第2列的宽度为 150

        # 默认配置
        self.load(self.url)

        # 按钮事件绑定
        self.action.triggered.connect(self.open_dir)
        self.action_2.triggered.connect(self.load)
        self.action_3.triggered.connect(lambda: self.save(False))
        self.action_5.triggered.connect(self.save)
        self.pushButton.clicked.connect(self.choose)
        self.pushButton_2.clicked.connect(self.install)
        self.pushButton_3.clicked.connect(self.check)

        # 快捷键绑定
        self.action.setShortcut('f1')
        self.action_2.setShortcut('ctrl+l')
        self.action_3.setShortcut('ctrl+s')
        self.action_5.setShortcut('shift+ctrl+s')
        self.pushButton_2.setShortcut('ctrl+i')
        self.pushButton_3.setShortcut('ctrl+c')

        # 将焦点设置到 pushButton_2
        self.pushButton_2.setFocus()

    def open_dir(self):
        root = os.getcwd()
        os.startfile(root)
        self.statusbar.showMessage('操作：打开根目录')

    def choose(self):
        url = QFileDialog.getExistingDirectory(self, "选择文件夹", self.lineEdit.text())
        if url:
            self.lineEdit.setText(url)
            self.statusbar.showMessage(f'操作：载入路径成功，路径：{url}')

    def load(self, url: str = ''):
        if url:
            url_ = url
        else:
            url_, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "配置文件 (*.ini);;所有文件 (*)")  # 打开文件管理器

        if url_:
            try:
                self.cf.read(url_)
                path = self.cf.get('path', 'game_path')

                # 读取游戏路径
                if not path:
                    self.statusbar.showMessage(f'操作：读取游戏路径失败，错误：路径为空')
                else:
                    self.lineEdit.setText(path)  # 写入路径栏中

            except Exception as e:
                self.statusbar.showMessage(f'操作：读取配置失败，错误：{e}')

    def save(self, save_is: bool = True):
        """保存文件"""
        if save_is:
            url, _ = QFileDialog.getSaveFileName(self, "保存文件", 'config.ini', "配置文件 (*.ini);;所有文件 (*)")
        else:
            url = self.url

        game_path = self.lineEdit.text()  # 游戏配置路径，捕获路径栏
        dota_path = game_path + '/dota'
        mod_path = game_path + '/mod'

        if not game_path:
            self.statusbar.showMessage(f'操作：保存配置失败，配置路径为空')

        else:
            try:
                with open(url, 'w') as f:
                    self.cf['path'] = {'game_path': game_path,
                                       'dota_path': dota_path,
                                       'mod_path': mod_path,
                                       }
                    self.cf.write(f)
                    self.statusbar.showMessage(f'操作：保存配置成功，路径：{url}')
            except Exception as e:
                self.statusbar.showMessage(f'操作：保存配置失败，错误：{e}')

    def copy_gi(self):
        path = self.lineEdit.text() + '/dota'  # 游戏配置路径，捕获路径栏
        if not os.path.exists(path):
            os.makedirs(path)
        else:
            try:
                shutil.copy('../gi/gameinfo.gi', path)
                shutil.copy('../gi/gameinfo_branchspecific.gi', path)
                self.statusbar.showMessage(f'操作：复制gi文件成功，路径：{path}')
            except Exception as e:
                self.statusbar.showMessage(f'操作：复制gi错误，错误：{e}，路径：{path}')

    def create_mod_file(self):
        path = self.lineEdit.text() + '/mod'  # 游戏配置路径，捕获路径栏
        if not os.path.exists(path):
            try:
                os.makedirs(path)
                self.statusbar.showMessage(f'操作：创建文件夹成功，路径：{path}')
            except Exception as e:
                self.statusbar.showMessage(f'操作：创建文件夹错误，错误：{e}，路径：{path}')
        else:
            self.statusbar.showMessage(f'操作：文件夹已存在，路径：{path}')

    def install(self):
        self.copy_gi()
        self.create_mod_file()
        self.statusbar.showMessage(f'操作：环境安装成功')

    def check(self):
        self.statusbar.showMessage('操作：检查环境成功')


if __name__ == '__main__':
    app = QApplication([])
    win = ConfigWin('../config/config.ini')
    win.show()
    app.exec()
