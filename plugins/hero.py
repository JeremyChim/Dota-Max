from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView, QTreeWidgetItem
from PyQt6.QtCore import Qt
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
        self.action.triggered.connect(self.open_dir)
        self.action_2.triggered.connect(self.open_ab_edit_win)

    def init_hotkey(self):
        """快捷键绑定"""
        self.action.setShortcut('f1')
        self.action_2.setShortcut('f2')

    def init_width(self):
        """初始化列宽"""
        header = self.treeWidget.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        self.treeWidget.setColumnWidth(0, 280)  # 设置第1列的宽度为 260
        self.treeWidget.setColumnWidth(1, 60)  # 设置第2列的宽度为 60

    def init_tree(self):
        """初始化树形控件"""
        cf_url = '../config/hero_tag.ini'
        self.cf.read(cf_url, encoding='utf-8')

        path = '../npc/heroes'
        path = path if os.path.exists(path) else './npc/heroes'  # 区分内部调用和外部调用，路径不一样
        item_list = os.listdir(path)  # 获取目录下的所有文件和目录名
        # print(item_list)
        # item_list = [f for f in file if os.path.isfile(os.path.join(path, f))]  # 过滤出文件名，忽略目录
        # print(item_list)

        for item_name in item_list:
            tag = self.cf.get('tag', item_name, fallback=None)  # 获取标签名, 如果没有返回None
            item = QTreeWidgetItem([item_name, tag])  # 创建项
            item.setCheckState(0, Qt.CheckState.Unchecked)  # 未勾选
            self.treeWidget.addTopLevelItem(item)  # 将项添加到树形控件

    def open_dir(self):
        root = os.getcwd()
        os.startfile(root)
        self.statusbar.showMessage('操作：打开根目录')

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
