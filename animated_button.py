from PyQt5.QtWidgets import QPushButton, QApplication
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty, QEasingCurve
from PyQt5.QtGui import QPalette, QColor
import sys

class AnimatedButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        self.colorAnimation = QPropertyAnimation(self, b"color")
        self.colorAnimation.setDuration(500)
        self.colorAnimation.setEasingCurve(QEasingCurve.InOutQuad)

    def enterEvent(self, event):
        self.colorAnimation.setStartValue(QColor(255, 140, 0))  # #ff8c00
        self.colorAnimation.setEndValue(QColor(255, 165, 0))  # #ffa500
        self.colorAnimation.start()

    def leaveEvent(self, event):
        self.colorAnimation.setStartValue(QColor(255, 165, 0))  # #ffa500
        self.colorAnimation.setEndValue(QColor(255, 191, 0))  # #ffbf00
        self.colorAnimation.start()

    def setColor(self, color):
        palette = self.palette()
        palette.setColor(QPalette.Button, color)
        self.setPalette(palette)

    color = pyqtProperty(QColor, fset=setColor)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimatedButton()
    window.setStyleSheet("""
        AnimatedButton {
            border-radius: 15px;
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #ff8c00, stop:0.5 #ffa500, stop:1 #ffbf00);
            border: none;
            font: bold;
            color: #fff;
        }

        AnimatedButton:focus {outline: none;
                         }

        AnimatedButton:hover {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #ffbf00, stop:0.5 #ffa500, stop:1 #ff8c00);
        }
    """)
    window.show()
    sys.exit(app.exec_())