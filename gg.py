from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QColor, QPainter, QBrush, QPixmap
from PyQt5.QtCore import Qt, QTimer, QRect,QUrl
from PyQt5.QtMultimedia import QSoundEffect
import sys

class TransparentWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口属性
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # 加载音频文件
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("./res/gg.wav"))
        self.sound.setLoopCount(QSoundEffect.Infinite)

        # 加载图像文件
        self.image_label = QLabel(self)
        pixmap = QPixmap("./res/gg.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setGeometry(QRect(0, 0, pixmap.width(), pixmap.height()))

        # 设置窗口大小和位置
        self.resize(pixmap.width(), pixmap.height())
        self.center()

        # 开始播放音频
        self.sound.play()

        self.show()

    def center(self):
        # 获取屏幕的尺寸
        screen_geometry = QApplication.desktop().screenGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        # 计算窗口的左上角坐标
        x = (screen_width - self.width()) // 2
        y = (screen_height - self.height()) // 2

        # 移动窗口到指定位置
        self.move(x, y)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制透明背景
        brush = QBrush(QColor(0, 0, 0, 0))
        painter.setBrush(brush)
        painter.drawRect(self.rect())

# 创建应用程序
app = QApplication(sys.argv)
window = TransparentWindow()

# 设置定时器，每2秒播放音频
timer = QTimer()
timer.timeout.connect(window.sound.play)
timer.start(2000)

# 运行应用程序
sys.exit(app.exec_())