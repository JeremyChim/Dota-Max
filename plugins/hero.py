from PyQt6.QtWidgets import QApplication, QMainWindow, QHeaderView
from ui.py.hero import Ui_MainWindow
from plugins.ab_edit import AbEditWin

import os


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

        self.init()

    def init(self):
        """初始化"""

        # 初始化列宽
        header = self.treeWidget.header()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Fixed)  # 设置第一列为固定宽度
        self.treeWidget.setColumnWidth(0, 280)  # 设置第1列的宽度为 260
        self.treeWidget.setColumnWidth(1, 60)  # 设置第2列的宽度为 60

        # 按钮事件绑定
        self.action.triggered.connect(self.open_dir)
        self.action_2.triggered.connect(self.open_ab_edit_win)

        # 快捷键绑定
        self.action.setShortcut('f1')
        self.action_2.setShortcut('f2')

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
