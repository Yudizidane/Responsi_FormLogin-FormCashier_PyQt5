import sys

from PyQt5 import Qt
from PyQt5.uic import loadUi
from kasirr import *


class loginnn(Qt.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = loadUi("login.ui", self)
        self.masuk.clicked.connect(self.masukk)

    @Qt.pyqtSlot()
    def masukk(self):
        masuk1 = self.nama.text()
        password1 = self.katasandi.text()

        if masuk1 =="yudi" and password1 =="776682":

            self.kasir=kasirr()
            self.kasir.show()
            self.close()

        else:
            self.nama.setText("")
            self.katasandi.setText("")


app = Qt.QApplication(sys.argv)

watch = loginnn()
watch.show()

app.exec_()
