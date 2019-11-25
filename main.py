import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawCircle(qp)
        qp.end()

    def drawCircle(self, qp):
        qp.setBrush(QColor('yellow'))
        radius = randint(10, 200)
        qp.drawEllipse(210 - radius // 2, 160 - radius // 2, radius, radius)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())