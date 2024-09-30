from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import Qt, QStringListModel
from ui.py.ab_edit import Ui_MainWindow
from script.try_script import try_decorator
from script.ab_script2 import ab_replace
from script.tab_script import tab_up

import os


class AbEditWin(QMainWindow, Ui_MainWindow):
    def __init__(self, url=None):
        """
        技能编辑器
        :param url: 默认打开文件路径
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('技能编辑器')
        self.statusbar.showMessage('初始化完成。 技能编辑器版本：1.0.0')

        self.init_url = url  # 初始化路径
        self.fn = None  # 用于存储文件名
        self.undo_board = None  # 用于存储撤回文本
        self.clip_board = []  # 剪切板

        self.init()

    def init(self):
        """初始化"""
        if self.init_url:
            self.load(self.init_url)  # 初始化载入文件

        # 按钮事件绑定
        self.action_2.triggered.connect(lambda: self.load())
        self.action_5.triggered.connect(lambda: self.win_top())
        self.pushButton.clicked.connect(lambda: self.calc())
        self.pushButton_8.clicked.connect(lambda: self.cut())
        self.pushButton_9.clicked.connect(lambda: self.paste())
        self.pushButton_11.clicked.connect(lambda: self.undo())
        self.pushButton_12.clicked.connect(lambda: self.save_as())
        self.pushButton_13.clicked.connect(lambda: self.save_as())

        # 快捷键绑定
        self.action_2.setShortcut('F2')
        self.pushButton.setShortcut('Ctrl+`')
        self.pushButton_8.setShortcut('Ctrl+X')
        self.pushButton_9.setShortcut('Ctrl+V')
        self.pushButton_11.setShortcut('Ctrl+Z')
        self.pushButton_12.setShortcut('Ctrl+S')
        self.pushButton_13.setShortcut('Shift+Ctrl+S')

    @try_decorator
    def win_top(self):
        """窗口置顶"""
        if self.action_5.isChecked() is True:
            self.setWindowFlags(self.windowFlags() | Qt.WindowType.WindowStaysOnTopHint)  # window top
            self.statusbar.showMessage('操作：窗口置顶')
        else:
            self.setWindowFlags(self.windowFlags() & ~Qt.WindowType.WindowStaysOnTopHint)  # cancel
            self.statusbar.showMessage('操作：窗口取消置顶')
        self.show()

    @try_decorator
    def load(self, url=None):
        """
        :param url: 默认打开文件路径
        """
        if not url:
            url, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "文本文件 (*.txt);;所有文件 (*)")
        if url:
            with open(url, 'r', encoding='utf-8', errors='ignore') as f:
                ls = f.readlines()
            m = QStringListModel()  # 建立模型
            m.setStringList(ls)  # 写入内容至模型
            self.listView.setModel(m)  # lv绑定模型
            self.fn = url.split('/')[-1]  # 记忆文件名
            # self.pushButton_15.click()  # 清空剪切板
            self.statusbar.showMessage(f'操作：载入数据成功，路径：{url}')

    @try_decorator
    def dragEnterEvent(self, event):
        """允许拖拽文件"""
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    @try_decorator
    def dropEvent(self, event):
        """处理拖放事件"""
        url = [u.toLocalFile() for u in event.mimeData().urls()][0]
        if url:
            with open(url, 'r', encoding='utf-8', errors='ignore') as f:
                ls = f.readlines()
            m = QStringListModel()  # 建立模型
            m.setStringList(ls)  # 写入内容至模型
            self.listView.setModel(m)  # lv绑定模型
            self.fn = url.split('/')[-1]  # 记忆文件名
            # self.pushButton_15.click()  # 清空剪切板
            self.statusbar.showMessage(f'操作：载入数据成功，路径：{url}')

    @try_decorator
    def calc(self):
        """技能计算"""
        m = self.listView.model()  # 读模型，QStringListModel
        ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
        i = ls[0]  # <PyQt6.QtCore.QModelIndex>
        ab_old = m.data(i)  # 读
        m.setData(i, ab_replace(ab_old))  # 写
        self.undo_board = f'{ab_old}'  # 备份原字段

    @try_decorator
    def cut(self):
        m = self.listView.model()  # 读模型，QStringListModel
        ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
        i = ls[0]  # <PyQt6.QtCore.QModelIndex>
        t = m.data(i)  # 读
        t2 = '\n' + tab_up(t) + '\n'
        self.clip_board.append(t2)  # 剪切
        m.setData(i, '')  # 删
        self.statusbar.showMessage(f'操作：剪切成功，剪切板次数：{len(self.clip_board)}')

    @try_decorator
    def paste(self):
        m = self.listView.model()  # 读模型，QStringListModel
        ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
        i = ls[0]  # <PyQt6.QtCore.QModelIndex>
        t = m.data(i)  # 读
        t2 = '\n'.join(self.clip_board)  # 读剪切板
        # t3 = tab_func(t2, '+')  # 剪切板内容全部进格
        t4 = t + t2
        m.setData(i, t4 + '\n')  # 写
        self.clip_board = []  # 清空剪切板
        self.statusbar.showMessage(f'操作：粘贴成功')

    @try_decorator
    def undo(self):
        """撤回"""
        m = self.listView.model()  # 读模型，QStringListModel
        ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
        i = ls[0]  # <PyQt6.QtCore.QModelIndex>
        if self.undo_board:
            m.setData(i, self.undo_board)  # 写
            self.statusbar.showMessage(f'操作：撤回成功')

    @try_decorator
    def save_as(self, is_open: bool = False):
        url, _ = QFileDialog.getSaveFileName(self, "保存文件", self.fn, "文本文件 (*.txt);;所有文件 (*)")
        if url:
            with open(url, 'w') as f:
                m = self.listView.model()  # 读模型，QStringListModel
                row = m.rowCount()  # 共多少行
                ls = []
                for r in range(row):
                    i = m.index(r, 0)  # r行0列
                    tx = m.data(i)  # 内容
                    ls.append(tx)  # 写入列表
                f.writelines(ls)  # 写
            self.statusbar.showMessage(f'操作：保存数据成功，路径：{url}')

            # 打开
            try:
                if is_open is True:
                    os.startfile(url)
            except Exception as e:
                print(e)


if __name__ == '__main__':
    app = QApplication([])
    win = AbEditWin(r'D:\PJ\Dota Max\npc_dota_hero_spectre.txt')
    win.show()
    app.exec()
