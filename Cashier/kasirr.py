import sys

from PyQt5 import Qt
from PyQt5.uic import loadUi

# [ms]
TICK_TIME = 2**6

class kasirr(Qt.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = loadUi("kasir.ui", self)
        self.hitung.clicked.connect(self.hitung1)
        self.reset.clicked.connect(self.setreset)

    @Qt.pyqtSlot()
    def hitung1(self):
        harga1 = self.hargabarang.text()
        harga2 = eval(harga1)
        barang1 = self.jumlahbarang.text()
        barang2 = eval(barang1)
        uang1 = self.uangtunai.text()
        uang2 = eval(uang1)
        total1 = harga2*barang2
        self.total.setText(str(total1))
        kembalian1 = uang2-total1
        self.uang.setText(str(kembalian1))

    @Qt.pyqtSlot()
    def setreset(self) :
        self.namabarang.setText("")
        self.hargabarang.setText("")
        self.jumlahbarang.setText("")
        self.uangtunai.setText("")
        self.total.setText("")
        self.uang.setText("")
