import sys

from PyQt5.QtWidgets import QApplication

from gui.mainwindow import VCMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = VCMainWindow()
    win.setWindowTitle("草原草畜平衡监测图像的分析 ")
    win.show()
    sys.exit(app.exec_())
