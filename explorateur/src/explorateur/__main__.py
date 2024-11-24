import sys
from explorateur.Explorateur import explorateur
from PyQt6.QtWidgets import QApplication, QMainWindow
from explorateur.Interface import Ui_MainWindow
from explorateur.Application import App


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self, app, explorateur)
        self.show()


if __name__ == "__main__":
    app = App(sys.argv)
    app.installEventFilter(app)

    explorateur = explorateur()

    win = Window()

    sys.exit(app.exec())
