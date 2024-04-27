from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QPropertyAnimation, pyqtProperty, QEasingCurve, QRect
from PyQt5.QtGui import QPalette, QColor

class AnimatedButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        self.colorAnimation = QPropertyAnimation(self, b"color")
        self.colorAnimation.setDuration(500)
        self.colorAnimation.setEasingCurve(QEasingCurve.InOutQuad)

        self.geometryAnimation = QPropertyAnimation(self, b"geometry")
        self.geometryAnimation.setDuration(500)
        self.geometryAnimation.setEasingCurve(QEasingCurve.InOutQuad)

    def enterEvent(self, event):
        self.colorAnimation.setStartValue(QColor(169, 169, 169))
        self.colorAnimation.setEndValue(QColor(211, 211, 211))
        self.colorAnimation.start()

        self.geometryAnimation.setStartValue(self.geometry())
        self.geometryAnimation.setEndValue(QRect(self.x(), self.y(), self.width() + 10, self.height()))
        self.geometryAnimation.start()

    def leaveEvent(self, event):
        self.colorAnimation.setStartValue(QColor(211, 211, 211))
        self.colorAnimation.setEndValue(QColor(169, 169, 169))
        self.colorAnimation.start()

        self.geometryAnimation.setStartValue(self.geometry())
        self.geometryAnimation.setEndValue(QRect(self.x(), self.y(), self.width() - 10, self.height()))
        self.geometryAnimation.start()

    def setColor(self, color):
        palette = self.palette()
        palette.setColor(QPalette.Button, color)
        self.setPalette(palette)

    color = pyqtProperty(QColor, fset=setColor)