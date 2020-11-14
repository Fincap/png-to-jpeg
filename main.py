import sys

from PyQt5 import QtWidgets

from view import MainPage

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainPage()
    main_window.show()

    sys.exit(app.exec_())
