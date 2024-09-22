from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtCore import Qt, QStringListModel
from ui.py.ab_edit import Ui_MainWindow
from script.try_script import try_decorator


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
        self.ab = None  # 用于存储撤回文本

        self.init()

    def init(self):
        """初始化"""
        if self.init_url:
            self.load(self.init_url)  # 初始化载入文件

        # 按钮事件绑定
        self.action_2.triggered.connect(lambda: self.load())
        self.action_5.triggered.connect(lambda: self.win_top())
        self.pushButton.clicked.connect(lambda: self.calc())
        self.pushButton_11.clicked.connect(lambda: self.undo())

        # 快捷键绑定
        self.action_2.setShortcut('F2')
        self.pushButton_11.setShortcut('Ctrl+Z')

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
        for i in ls:
            ab = m.data(i)  # 读
            m.setData(i, '1')  # 写
            self.ab = f'{ab}'  # 备份原字段

    @try_decorator
    def undo(self):
        """撤回"""
        m = self.listView.model()  # 读模型，QStringListModel
        ls = self.listView.selectionModel().selectedIndexes()  # [<PyQt6.QtCore.QModelIndex>]
        for i in ls:
            if self.ab:
                m.setData(i, self.ab)  # 写


if __name__ == '__main__':
    app = QApplication([])
    win = AbEditWin(r'D:\python\project\Dota-Tool\vpk\pak01_dir\scripts\npc\heroes\ban\npc_dota_hero_mirana.txt')
    win.show()
    app.exec()
