import sys
import wmi
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import QFile, QIODevice, QObject, Slot


class MainWindow(QObject):

    def __init__(self, ui_file_name, parent=None):
        super(MainWindow, self).__init__(parent)

        ui_file = QFile(ui_file_name)

        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        if not self.window:
            print(loader.errorString())
            sys.exit(-1)

        btn_lit_out = self.window.findChild(QPushButton, 'pushButton')
        btn_lit_out.clicked.connect(self.light_out)

        btn_lit_up = self.window.findChild(QPushButton, 'pushButton_2')
        btn_lit_up.clicked.connect(self.light_up)
        self.window.show()

    @Slot()
    def light_up(self):
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(100, 0)

    @Slot()
    def light_out(self):
        wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(0, 0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow('main.ui')
    sys.exit(app.exec())
