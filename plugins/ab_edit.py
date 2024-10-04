from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import Qt, QStringListModel
from ui.py.ab_edit import Ui_MainWindow
from script.try_script import try_decorator
from script.ab_script2 import ab_replace
from script.tab_script import tab_up, tab_down

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

        self.open_url = url  # 初始化路径
        self.file_name = None  # 文件名
        self.undo_board = None  # 撤回文本
        self.clip_board = []  # 剪切板
        self.save_url = None  # 保存文件路径

        self.init()

    def init(self):
        """初始化"""
        if self.open_url:
            self.load(self.open_url)  # 初始化载入文件

        # 按钮事件绑定
        self.action_2.triggered.connect(lambda: self.load())
        self.action_5.triggered.connect(lambda: self.win_top())
        self.pushButton.clicked.connect(lambda: self.calc(is_cd=False))
        self.pushButton_6.clicked.connect(lambda: self.down())
        self.pushButton_7.clicked.connect(lambda: self.up())
        self.pushButton_8.clicked.connect(lambda: self.cut())
        self.pushButton_9.clicked.connect(lambda: self.paste())
        self.pushButton_11.clicked.connect(lambda: self.undo())
        self.pushButton_12.clicked.connect(lambda: self.save_as())
        self.pushButton_13.clicked.connect(lambda: self.open_file())
        self.pushButton_14.clicked.connect(lambda: self.calc(is_cd=True))

        # 快捷键绑定
        self.action_2.setShortcut('ctrl+l')
        self.pushButton.setShortcut('ctrl+`')
        self.pushButton_6.setShortcut('backspace')
        self.pushButton_7.setShortcut('tab')
        self.pushButton_8.setShortcut('ctrl+x')
        self.pushButton_9.setShortcut('ctrl+v')
        self.pushButton_11.setShortcut('ctrl+z')
        self.pushButton_12.setShortcut('ctrl+s')
        self.pushButton_13.setShortcut('ctrl+o')

        # 数值初始化
        self.spinBox_2.setValue(30)  # sa+
        self.spinBox_3.setValue(30)  # sa-
        self.spinBox_4.setValue(60)  # sp+
        self.spinBox_5.setValue(60)  # sp-

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
            self.file_name = url.split('/')[-1]  # 记忆文件名
            self.clip_board = []  # 清空剪切板
            self.statusbar.showMessage(f'操作：载入数据成功，路径：{url}')

    @try_decorator
    def load(self, url=None):
        """
        载入文件
        :param url: 默认打开文件路径
        """
        if not url:  # 如果默认载入路径为空
            url, _ = QFileDialog.getOpenFileName(self, "选择文件", "", "文本文件 (*.txt);;所有文件 (*)")  # 打开文件管理器
        if url:
            with open(url, 'r', encoding='utf-8', errors='ignore') as f:
                ls = f.readlines()
            m = QStringListModel()  # 建立模型
            m.setStringList(ls)  # 写入内容至模型
            self.listView.setModel(m)  # lv绑定模型
            self.file_name = url.split('/')[-1]  # 记忆文件名
            self.clip_board = []  # 清空剪切板
            self.statusbar.showMessage(f'操作：载入数据成功，路径：{url}')

    # @try_decorator
    def calc(self, is_cd: bool):
        """技能计算"""
        m = self.listView.model()  # 读模型，QStringListModel
        ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
        i = ls[0]  # <PyQt6.QtCore.QModelIndex>
        t = m.data(i)  # 读

        args = {'style': 0,
                'cd_enable': is_cd,
                'sa_enable': self.checkBox.isChecked(),
                'sp_enable': self.checkBox_2.isChecked(),
                'sa_value': f'+{self.spinBox_2.value()}%',
                'sp_value': f'+{self.spinBox_4.value()}%',
                'sa_cd': f'-{self.spinBox_3.value()}%',
                'sp_cd': f'-{self.spinBox_5.value()}%',
                'ab_old': t}

        m.setData(i, ab_replace(**args))  # 写
        self.undo_board = f'{t}'  # 备份原字段

    @try_decorator
    def up(self):
        """进格"""
        m = self.listView.model()  # 读模型，QStringListModel
        ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
        i = ls[0]  # <PyQt6.QtCore.QModelIndex>
        t = m.data(i)  # 读
        m.setData(i, tab_up(t))  # 写

    @try_decorator
    def down(self):
        """进格"""
        m = self.listView.model()  # 读模型，QStringListModel
        ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
        i = ls[0]  # <PyQt6.QtCore.QModelIndex>
        t = m.data(i)  # 读
        m.setData(i, tab_down(t))  # 写

    @try_decorator
    def cut(self):
        """剪切"""
        m = self.listView.model()  # 读模型，QStringListModel
        ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
        i = ls[0]  # <PyQt6.QtCore.QModelIndex>
        t = m.data(i)  # 读
        t2 = '\n' + tab_up(t)
        self.clip_board.append(t2)  # 剪切
        m.setData(i, '')  # 删
        self.statusbar.showMessage(f'操作：剪切成功，剪切板次数：{len(self.clip_board)}')

    @try_decorator
    def paste(self):
        """粘贴"""
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
    def save_as(self):
        """另存文件"""
        url, _ = QFileDialog.getSaveFileName(self, "保存文件", self.file_name, "文本文件 (*.txt);;所有文件 (*)")
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
            self.save_url = url
            self.statusbar.showMessage(f'操作：保存数据成功，路径：{url}')

    def open_file(self):
        """打开文件"""
        if self.save_url:
            if os.path.exists(self.save_url) is True:
                try:
                    os.startfile(self.save_url)
                except Exception as e:
                    self.statusbar.showMessage(f'操作：打开文件失败，错误：{e}')
            else:
                self.statusbar.showMessage('操作：文件不存在，无法打开')
        else:
            self.statusbar.showMessage('操作：文件未保存，无法打开')


if __name__ == '__main__':
    app = QApplication([])
    win = AbEditWin(r'D:\PJ\Dota Max\npc_dota_hero_spectre.txt')
    win.show()
    app.exec()
