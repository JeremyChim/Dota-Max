from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTreeWidgetItem
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QBrush
from ui.py.hero import Ui_MainWindow
from plugins.ab_edit import AbEditWin

import os
import configparser


class HeroWin(QMainWindow, Ui_MainWindow):
    def __init__(self, url: str = None):
        """
        英雄文件选择器
        :param url: npc_dota_hero_windrunner.txt(临时变量)
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('英雄文件选择器')
        self.statusbar.showMessage('初始化完成。 英雄文件选择器：1.0.0')
        self.ab_url = url  # 英雄编辑器默认载入路径
        self.ab_edit_win = None  # 用于存储 AbEditWin 实例
        self.cf = configparser.ConfigParser()  # cf
        self.init()

    def init(self):
        """初始化"""
        self.init_btn()  # 按钮事件绑定
        self.init_hotkey()  # 快捷键绑定
        self.init_width()  # 初始化列宽
        self.init_tree()  # 初始化树形控件

    def init_btn(self):
        """按钮事件绑定"""
        self.action.triggered.connect(lambda: self.open_dir(os.getcwd()))
        self.action_2.triggered.connect(self.open_ab_edit_win)

    def init_hotkey(self):
        """快捷键绑定"""
        self.action.setShortcut('f1')
        self.action_2.setShortcut('f2')

    def init_width(self):
        """初始化列宽"""
        header = self.treeWidget.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # 设置第1列为固定宽度
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)  # 设置第2列为固定宽度
        self.treeWidget.setColumnWidth(0, 300)  # 设置第1列的宽度为 300
        self.treeWidget.setColumnWidth(1, 100)  # 设置第2列的宽度为 100

    def init_tree(self):
        """初始化树形控件"""
        grey = QBrush(QColor(220, 220, 220))  # 灰色背景

        cf_url = '../config/hero_tag.ini'
        cf_url = cf_url if os.path.exists(cf_url) else './config/hero_tag.ini'  # 区分内部调用和外部调用，路径不一样
        self.cf.read(cf_url, encoding='utf-8')

        path = '../npc/heroes'
        path = path if os.path.exists(path) else './npc/heroes'  # 区分内部调用和外部调用，路径不一样
        item_list = os.listdir(path)  # 获取目录下的所有文件和目录名

        for item_name in item_list:
            tag = self.cf.get('tag', item_name, fallback=None)  # 获取标签名, 如果没有返回None
            item = QTreeWidgetItem([item_name, tag])  # 创建项
            item.setCheckState(0, Qt.CheckState.Unchecked)  # 第1列添加未勾选框
            item.setBackground(1, grey)  # 第2列灰色背景
            self.treeWidget.addTopLevelItem(item)  # 将项添加到树形控件
            self.treeWidget.itemDoubleClicked.connect(self.double_clicked)

    def double_clicked(self, item):
        """treeWidget项双击事件"""
        _path = os.getcwd().replace("\\", "/")  # 获取运行目录
        _list = _path.split('/')

        # 区分内部调用和外部调用，路径不一样
        if _list[-1] == 'Dota-Max':
            root = _path
        else:
            root = '/'.join(_list[:-1])
        path = f'{root}/npc/heroes/{item.text(0)}'  # 默认第1列
        self.open_dir(path)

    def open_dir(self, path):
        """打开目录"""
        try:
            os.startfile(path)
            self.statusbar.showMessage(f'操作：打开目录，路径：{path}')
        except Exception as e:
            self.statusbar.showMessage(f'操作：打开目录失败，错误：{e}')

    def open_ab_edit_win(self):
        """打开技能编辑器窗口"""
        if not self.ab_edit_win:
            self.ab_edit_win = AbEditWin(self.ab_url)
        self.ab_edit_win.show()


if __name__ == '__main__':
    app = QApplication([])
    win = HeroWin('npc_dota_hero_windrunner.txt')
    win.show()
    app.exec()
