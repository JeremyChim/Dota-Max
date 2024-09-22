from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.py.main import Ui_MainWindow
from plugins.hero import HeroWin


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Dota Max 游戏修改器')
        self.statusbar.showMessage('初始化完成。 游戏修改器版本：1.0.0')

        self.hero_win = None  # 用于存储 HeroWin 实例

        self.init()

    def init(self):
        """初始化"""

        # 按钮事件绑定
        self.pushButton_4.clicked.connect(self.open_hero_win)

        # 快捷键绑定
        # ...

    def open_hero_win(self):
        """打开英雄文件选择器窗口"""
        if not self.hero_win:
            self.hero_win = HeroWin()
        self.hero_win.show()


if __name__ == '__main__':
    app = QApplication([])
    win = MainWin()
    win.show()
    app.exec()
