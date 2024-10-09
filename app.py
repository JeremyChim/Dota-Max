from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction
from ui.py.main import Ui_MainWindow
from plugins.hero import HeroWin
from plugins.config import ConfigWin

import os
import pyperclip
import configparser


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, url: str = ''):
        """
        :param url: code.ini 的路径
        """
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Dota Max 游戏修改器')
        self.statusbar.showMessage('初始化完成。 游戏修改器版本：1.0.0')

        self.url = url  # 用于存储 code.ini 的路径
        self.config_win = None  # 用于存储 ConfigWin 实例
        self.hero_win = None  # 用于存储 HeroWin 实例
        self.cf = configparser.ConfigParser()  # config file
        self.code_dict = {
            # action_widget: (section, option)
            self.action_2: ('Open Hyper AI', 'Open Fretbots Mode'),
            self.action_3: ('Steam Command', 'Steam Boot'),
            self.action_4: ('Steam Command', 'Steam Small Win'),
        }

        self.init()

    def init(self):
        """初始化"""

        # 动作事件绑定
        for widget, (sec, opt) in self.code_dict.items():
            # 确保在 lambda 表达式中使用的变量名称与在循环中定义的变量名称相匹配
            widget.triggered.connect(lambda wid_=widget, sec_=sec, opt_=opt: self.copy_code(sec_, opt_))

        # 按钮事件绑定
        self.pushButton.clicked.connect(self.open_config_win)
        self.pushButton_4.clicked.connect(self.open_hero_win)
        self.pushButton_5.clicked.connect(self.create_vpk)

        # 快捷键绑定
        self.pushButton.setShortcut('ctrl+1')
        self.pushButton_2.setShortcut('ctrl+2')
        self.pushButton_3.setShortcut('ctrl+3')
        self.pushButton_4.setShortcut('ctrl+4')
        self.pushButton_5.setShortcut('ctrl+5')
        self.pushButton_6.setShortcut('ctrl+6')

    def copy_code(self, sec: str, opt: str):
        """复制指令"""
        if not os.path.exists(self.url):
            self.statusbar.showMessage(f'操作：复制指令失败，错误：配置文件code.ini不存在')

        else:
            try:
                self.cf.read(self.url)
                code = self.cf.get(sec, opt)

                # 读取游戏路径
                if not code:
                    self.statusbar.showMessage(f'操作：复制指令失败，错误：路径为空')
                else:
                    self.statusbar.showMessage(f'操作：复制指令成功，指令：{code}')
                    pyperclip.copy(code)

            except Exception as e:
                self.statusbar.showMessage(f'操作：复制指令失败，错误：{e}')

    def open_config_win(self):
        """打开英雄文件选择器窗口"""
        if not self.config_win:
            self.config_win = ConfigWin(r'config/config.ini')
        self.config_win.show()

    def open_hero_win(self):
        """打开英雄文件选择器窗口"""
        if not self.hero_win:
            self.hero_win = HeroWin()
        self.hero_win.show()

    def create_vpk(self):
        if not os.path.exists('vpk/pak01_dir'):
            self.statusbar.showMessage(f'操作：生成vpk失败，错误：pak01_dir文件夹不存在')

        else:
            try:
                order = '"vpk/vpk.exe" "vpk/pak01_dir" && exit'
                os.system(f'start cmd /k "{order}"')
                self.statusbar.showMessage('操作：生成vpk成功')
            except Exception as e:
                self.statusbar.showMessage(f'操作：生成vpk失败，错误：{e}')


if __name__ == '__main__':
    app = QApplication([])
    win = MainWin(r'config/code.ini')
    win.show()
    app.exec()
