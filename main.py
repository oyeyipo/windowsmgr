import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui


TURN_UP_LIGHT = "Lit Up"

class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton(TURN_UP_LIGHT)

        self.text = QtWidgets.QLabel("Hello World Mr Ola", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec())
