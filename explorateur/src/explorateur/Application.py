from PyQt6 import QtCore, QtWidgets


class keyboard:
    def __init__(self, interface, explorateur):
        self.interface = interface
        self.explorateur = explorateur

    def keyPress(self, key):
        if key == QtCore.Qt.Key.Key_Up:
            self.interface.selectIndex(self.explorateur.index_fichier_selectionner - 1)
            for i in range(len(self.interface.widgets)):
                if i != self.explorateur.index_fichier_selectionner:
                    self.interface.unselectIndex(i)
        elif key == QtCore.Qt.Key.Key_Down:
            self.interface.selectIndex(self.explorateur.index_fichier_selectionner + 1)
            for i in range(len(self.interface.widgets)):
                if i != self.explorateur.index_fichier_selectionner:
                    self.interface.unselectIndex(i)


class App(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.eventSet = False
        self.keyboardInstance = None
        self.keyPressed = []

    def setEvent(self, keyboardInstance):
        self.keyboardInstance = keyboardInstance
        self.eventSet = True

    def eventFilter(self, source, event):
        if self.eventSet:
            if event.type() == QtCore.QEvent.Type.KeyPress and self.keyPressed.count(event.key()) == 0:
                self.keyboardInstance.keyPress(event.key())
                self.keyPressed.append(event.key())
            if event.type() == QtCore.QEvent.Type.KeyRelease and self.keyPressed.count(event.key()) > 0:
                self.keyPressed.remove(event.key())
        return QtCore.QObject.eventFilter(self, source, event)
