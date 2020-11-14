from PyQt5 import QtWidgets


class MainPage(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.resize(400, 200)
        self.setWindowTitle("png-to-jpeg")
