from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QFileDialog, QTreeWidgetItem
from PyQt6.QtGui import QColor, QBrush
from PyQt6.QtCore import Qt
from ui.py.config import Ui_MainWindow
from datetime import datetime

import configparser
import os
import shutil


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
        self.load(self.url)  # 初始化配置（加载路径至路径栏）
        self.init_btn()  # 按钮事件绑定
        self.init_hotkey()  # 快捷键绑定
        self.init_width()  # 初始化列宽
        self.check()  # 初始化检查
        self.pushButton_2.setFocus()  # 将焦点设置到 pushButton_2

    def init_btn(self):
        """按钮事件绑定"""
        self.action.triggered.connect(lambda: self.open_dir(os.getcwd()))
        self.action_2.triggered.connect(self.load)
        self.action_3.triggered.connect(self.save)
        self.action_5.triggered.connect(lambda: self.save(True))
        self.pushButton.clicked.connect(self.choose)
        self.pushButton_2.clicked.connect(self.install)
        self.pushButton_3.clicked.connect(self.check)
        self.pushButton_4.clicked.connect(lambda: self.open_dir(self.lineEdit.text()))

    def init_hotkey(self):
        """快捷键绑定"""
        self.action.setShortcut('f1')
        self.action_2.setShortcut('ctrl+l')
        self.action_3.setShortcut('ctrl+s')
        self.action_5.setShortcut('shift+ctrl+s')
        self.pushButton_2.setShortcut('ctrl+i')
        self.pushButton_3.setShortcut('ctrl+c')

    def init_width(self):
        """初始化列宽"""
        header = self.treeWidget.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        self.treeWidget.setColumnWidth(0, 400)  # 设置第1列的宽度为 400
        self.treeWidget.setColumnWidth(1, 150)  # 设置第2列的宽度为 150

    def open_dir(self, path: str):
        """打开目录"""
        try:
            os.startfile(path)
            self.statusbar.showMessage(f'操作：打开目录，路径：{path}')
        except Exception as e:
            self.statusbar.showMessage(f'操作：打开目录失败，错误：{e}')

    def choose(self):
        """选择路径"""
        url = QFileDialog.getExistingDirectory(self, "选择文件夹", self.lineEdit.text())
        if url:
            self.lineEdit.setText(url)

    def load(self, url: str = ''):
        """加载文件"""
        if url:
            cf_url = url
        else:
            # 打开文件管理器
            cf_url, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "配置文件 (*.ini);;所有文件 (*)")

        if cf_url:
            try:
                self.cf.read(cf_url)
                path = self.cf.get('path', 'game_path')  # 读取游戏路径
                if not path:
                    self.statusbar.showMessage(f'操作：读取游戏路径失败，错误：路径为空')
                else:
                    self.lineEdit.setText(path)  # 写入路径栏中
            except Exception as e:
                self.statusbar.showMessage(f'操作：读取配置失败，错误：{e}')

    def save(self, save_is: bool = False):
        """保存文件"""
        if save_is:  # 另存
            cf_url = self.url if self.url else 'config.ini'
            url, _ = QFileDialog.getSaveFileName(self, "保存文件", cf_url, "配置文件 (*.ini);;所有文件 (*)")
        else:
            url = self.url

        game_path = self.lineEdit.text()  # 游戏配置路径，捕获路径栏
        dota_path = game_path + '/dota'
        gi_path = game_path + '/dota/gameinfo.gi'
        gi2_path = game_path + '/dota/gameinfo_branchspecific.gi'
        mod_path = game_path + '/mod'
        vpk_path = game_path + '/mod/pak01_dir.vpk'
        bot_path = game_path + '/dota/scripts/vscripts/bots'

        if not game_path:
            self.statusbar.showMessage(f'操作：保存配置失败，配置路径为空')

        else:
            try:
                with open(url, 'w') as f:
                    self.cf['path'] = {'game_path': game_path,
                                       'dota_path': dota_path,
                                       'gi_path': gi_path,
                                       'gi2_path': gi2_path,
                                       'mod_path': mod_path,
                                       'vpk_path': vpk_path,
                                       'bot_path': bot_path,
                                       }
                    self.cf.write(f)
                    self.statusbar.showMessage(f'操作：保存配置成功，路径：{url}')
            except Exception as e:
                self.statusbar.showMessage(f'操作：保存配置失败，错误：{e}')

    def install_file(self, pattern: str, file: str, src: str):
        """安装文件的函数"""
        match pattern:
            case 'create_folder':
                path = f'{self.lineEdit.text()}/{file}'  # 文件夹
                try:
                    if not os.path.exists(path):
                        os.makedirs(path)  # 创建文件夹
                        self.statusbar.showMessage(f'操作：创建文件夹{file}成功，路径：{path}')
                    else:
                        self.statusbar.showMessage(f'操作：文件夹{file}，已存在')
                except Exception as e:
                    self.statusbar.showMessage(f'操作：创建文件夹{file}错误，错误：{e}，路径：{path}')

            case 'copy_folder':
                path = f'{self.lineEdit.text()}/{file}'  # 文件夹
                try:
                    if os.path.exists(path):
                        shutil.rmtree(path)  # 如果文件夹存在，先删除
                    src2 = src.replace('../', './')
                    src3 = src2 if os.path.exists(src2) else src  # 区分内部调用和外部调用，路径不一样
                    shutil.copytree(src3, path)
                    self.statusbar.showMessage(f'操作：复制文件夹{file}成功，路径：{path}')
                except Exception as e:
                    self.statusbar.showMessage(f'操作：复制文件夹{file}错误，错误：{e}，路径：{path}')

            case 'copy_file':
                path = f'{self.lineEdit.text()}/{file}'
                try:
                    src2 = src.replace('../', './')
                    src3 = src2 if os.path.exists(src2) else src  # 区分内部调用和外部调用，路径不一样
                    shutil.copy(src3, path)
                    self.statusbar.showMessage(f'操作：复制文件{file}成功，路径：{path}')
                except Exception as e:
                    self.statusbar.showMessage(f'操作：复制文件{file}错误，错误：{e}，路径：{path}')

    def install(self):
        """安装环境"""
        args = [
            # ex: (pattern, file, src),
            ('create_folder', 'dota', None),
            ('copy_file', 'dota/gameinfo.gi', '../gi/gameinfo.gi'),
            ('copy_file', 'dota/gameinfo_branchspecific.gi', '../gi/gameinfo_branchspecific.gi'),
            ('create_folder', 'mod', None),
            ('copy_file', 'mod/pak01_dir.vpk', '../vpk/pak01_dir.vpk'),
            ('copy_folder', 'dota/scripts/vscripts/bots', '../bot/bots'),
            ('create_folder', 'Dota2SkinChanger', None),
            ('copy_file', 'Dota2SkinChanger/pak01_dir.vpk', '../skin_package/pak01_dir.vpk'),
        ]
        for arg in args:
            self.install_file(*arg)
        self.save()
        # self.statusbar.showMessage(f'操作：环境安装成功')

    def check(self):
        """初始化检查"""
        self.treeWidget.clear()  # 清除所有项
        yellow = QBrush(QColor(255, 255, 0))  # 黄色背景
        green = QBrush(QColor(0, 255, 0))  # 绿色背景
        paths = [
            # (path, enable)
            ('dota', True),
            ('dota/gameinfo.gi', True),
            ('dota/gameinfo_branchspecific.gi', True),
            ('mod', True),
            ('mod/pak01_dir.vpk', True),
            ('dota/scripts/vscripts/bots', True),
            ('Dota2SkinChanger', True),
            ('Dota2SkinChanger/pak01_dir.vpk', True),
        ]

        for (path, enable) in paths:
            url = f'{self.lineEdit.text()}/{path}'
            item = QTreeWidgetItem([path])  # 创建项
            if not os.path.exists(url):  # 创建文件是否存在
                item.setBackground(0, yellow)  # 黄背景
                item.setText(1, '文件不存在')  # 写入信息

            else:
                item.setBackground(0, green)  # 绿背景
                st = os.stat(url).st_mtime  # 获取修改时间
                fts = datetime.fromtimestamp(st)
                ts = fts.strftime('%Y-%m-%d %H:%M:%S')
                item.setText(1, ts)
            if enable:
                item.setCheckState(0, Qt.CheckState.Checked)  # 已勾选
            else:
                item.setCheckState(0, Qt.CheckState.Unchecked)  # 未勾选
            self.treeWidget.addTopLevelItem(item)  # 将项添加到树形控件


if __name__ == '__main__':
    app = QApplication([])
    win = ConfigWin('../config/config.ini')
    win.show()
    app.exec()
