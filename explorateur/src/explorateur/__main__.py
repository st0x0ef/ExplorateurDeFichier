import sys
from explorateur.Explorateur import explorateur
from PyQt6.QtWidgets import QApplication, QMainWindow
from explorateur.Interface import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, explorateur, parent=None):
        super().__init__(parent)
        self.setupUi(self, app, explorateur)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    explorateur = explorateur()
    win = Window(explorateur)
    win.show()
    sys.exit(app.exec())
