from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.py.config import Ui_MainWindow


class ConfigWin(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """英雄文件选择器"""
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('环境配置器')
        self.statusbar.showMessage('初始化完成。 环境配置器：1.0.0')
        self.init()

    def init(self):
        """初始化"""
        # 按钮事件绑定
        # 快捷键绑定
        pass


if __name__ == '__main__':
    app = QApplication([])
    win = ConfigWin()
    win.show()
    app.exec()
