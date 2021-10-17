import sys
import wmi
from PySide6 import QtCore, QtWidgets, QtGui


TURN_UP_LIGHT = "Lit Up"
TURN_LIGHT_OUT = "Lit Out"


class MyWidget(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.lit_up = QtWidgets.QPushButton(TURN_UP_LIGHT)
        self.lit_out = QtWidgets.QPushButton(TURN_LIGHT_OUT)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.lit_up)
        self.layout.addWidget(self.lit_out)

        self.lit_up.clicked.connect(self.light_control)
        self.lit_out.clicked.connect(self.light_out)

    @QtCore.Slot()
    def light_control(self):
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(100, 0)

    @QtCore.Slot()
    def light_out(self):
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(0, 0)

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    widget = MyWidget()
    widget.resize(250, 30)
    widget.show()

    sys.exit(app.exec())
