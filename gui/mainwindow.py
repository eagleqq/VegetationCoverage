import os

from PyQt5.QtCore import QSize, Qt, pyqtSlot
from PyQt5.QtGui import QImage, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QGraphicsPixmapItem, QGraphicsScene, QFileDialog, QListView, QListWidgetItem, \
    QProgressDialog
from cv2 import cv2

from core.coloridentification import ColorIdentification
from gui import ui_mainwindow


class VCMainWindow(QMainWindow, ui_mainwindow.Ui_MainWindow):
    def __init__(self):
        super(VCMainWindow, self).__init__()
        self.setupUi(self)
        self.zoomscale = 1
        self.pushButton_select.clicked.connect(self.slotSelectPath)
        self.colorIdentification = ColorIdentification()
        self.initWidget()

    def initWidget(self):
        self.listWidget_img.resize(365, 400)
        self.listWidget_img.setViewMode(QListView.IconMode)
        self.listWidget_img.setIconSize(QSize(100, 100))
        self.listWidget_img.setSpacing(10)
        self.listWidget_img.setResizeMode(QListView.Adjust)
        self.listWidget_img.setMovement(QListView.Static)
        self.listWidget_img.itemClicked.connect(self.slotColorIdentification)

    def showImgToLabel(self, frame):
        result_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        qtImg = QImage(result_frame.data,
                       result_frame.shape[1],
                       result_frame.shape[0],
                       QImage.Format_RGB888)
        pix = QPixmap.fromImage(qtImg)
        self.item = QGraphicsPixmapItem(pix)
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView2.setScene(self.scene)

    def slotSelectPath(self):
        directory = QFileDialog.getExistingDirectory(None, "选取文件夹", "./")  # 起始路径
        self.lineEdit_path.setText(directory)
        self.listWidget_img.clear()
        jpg_list = self.getJPGList(directory)
        progress = QProgressDialog(self)
        progress.setWindowTitle("请稍等")
        progress.setLabelText("正在读取...")
        progress.setCancelButton(None)
        progress.setMinimumDuration(5)  # 此属性保留对话框出现之前必须通过的时间。
        progress.setWindowModality(Qt.ApplicationModal)
        progress.setWindowFlag(Qt.FramelessWindowHint)
        progress.setRange(0, len(jpg_list))
        i = 0
        for jpg in jpg_list:
            progress.setLabelText("正在读取第{}/{}张图片".format(i + 1, len(jpg_list)))
            item = QListWidgetItem()
            item.setIcon(QIcon(os.path.join(directory, jpg)))
            item.setText(jpg)
            item.setToolTip(jpg)
            item.setSizeHint(QSize(100, 120))
            self.listWidget_img.addItem(item)
            i += 1
            progress.setValue(i)

    def getJPGList(self, path):
        jpg_list = []
        dirs = os.listdir(path)  # 获取指定路径下的文件
        for i in dirs:  # 循环读取路径下的文件并筛选输出
            if os.path.splitext(i)[1] == ".jpg":
                jpg_list.append(i)
        return jpg_list

    def slotColorIdentification(self):
        root_path = self.lineEdit_path.text()
        jpg_name = self.listWidget_img.currentItem().text()
        path = os.path.join(root_path, jpg_name)
        frame2, percent = self.colorIdentification.getRet(path)
        self.showImgToLabel(frame2)
        self.lcdNumber.display(percent)

    @pyqtSlot()
    def on_pushButton_zoomin_clicked(self):
        """
        点击缩小图像
        """
        self.zoomscale=self.zoomscale-0.05
        if self.zoomscale<=0:
           self.zoomscale=0.2
        self.item.setScale(self.zoomscale)                                #缩小图像


    @pyqtSlot()
    def on_pushButton_zoomout_clicked(self):
        """
        点击放大图像
        """
        self.zoomscale=self.zoomscale+0.05
        if self.zoomscale>=1.2:
            self.zoomscale=1.2
        self.item.setScale(self.zoomscale)                             #放大图像