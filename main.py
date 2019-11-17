import sys
from PyQt5.QtWidgets import QApplication,  QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor
from random import randint
from des import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.paint = False
        self.pushButton.clicked.connect(self.run)

    def run(self):
        try:
            self.paint = True
            self.update()
        except Exception as e:
            print(e)

    def paintEvent(self, event):
        try:
            if self.paint:
                qp = QPainter()
                qp.begin(self)
                self.drawFlag(qp)
                qp.end()
        except Exception as e:
            print(e)

    def drawFlag(self, qp):
        for i in range(7):
            size = randint(20, 90)
            qp.setBrush(QColor(randint(0, 255), randint(0,255), randint(0, 255)))
            qp.drawEllipse(randint(0, 400), randint(0, 400), size, size)
        self.paint = False


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())