from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.py.hero import Ui_MainWindow
from plugins.ab_edit import AbEditWin


class HeroWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """英雄文件选择器"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('英雄文件选择器')
        self.statusbar.showMessage('初始化完成。 英雄文件选择器：1.0.0')

        self.ab_edit_win = None  # 用于存储 AbEditWin 实例

        self.init()

    def init(self):
        """初始化"""

        # 按钮事件绑定
        self.action_2.triggered.connect(self.open_ab_edit_win)
        # 快捷键绑定
        self.action_2.setShortcut('F2')

    def open_ab_edit_win(self):
        """打开技能编辑器窗口"""
        if not self.ab_edit_win:
            self.ab_edit_win = AbEditWin()
        self.ab_edit_win.show()


if __name__ == '__main__':
    app = QApplication([])
    win = HeroWin()
    win.show()
    app.exec()
