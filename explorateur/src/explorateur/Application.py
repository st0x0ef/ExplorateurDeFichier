from PyQt6 import QtCore, QtWidgets
from explorateur import Method


class keyboard:
    def __init__(self, interface, explorateur):
        self.interface = interface
        self.explorateur = explorateur

    def keyPress(self, key, modifiers):
        if key == QtCore.Qt.Key.Key_Up:
            if self.explorateur.index_fichier_selectionner[0] > 0:
                last_element = self.explorateur.index_fichier_selectionner[-1]
                if modifiers != QtCore.Qt.KeyboardModifier.ShiftModifier and len(self.explorateur.index_fichier_selectionner) > 0:
                    self.explorateur.index_fichier_selectionner.clear()
                self.interface.selectIndex(last_element - 1, False)
                for i in range(len(self.interface.widgets)):
                    if self.explorateur.index_fichier_selectionner.count(i) == 0:
                        self.interface.unselectIndex(i)

        elif key == QtCore.Qt.Key.Key_Down:
            if self.explorateur.index_fichier_selectionner[-1] < len(self.explorateur.fichiers):
                last_element = self.explorateur.index_fichier_selectionner[-1]
                if modifiers != QtCore.Qt.KeyboardModifier.ShiftModifier and len(self.explorateur.index_fichier_selectionner) > 0:
                    self.explorateur.index_fichier_selectionner.clear()
                self.interface.selectIndex(last_element + 1, False)
                for i in range(len(self.interface.widgets)):
                    if self.explorateur.index_fichier_selectionner.count(i) == 0:
                        self.interface.unselectIndex(i)

        elif key == QtCore.Qt.Key.Key_C and modifiers == QtCore.Qt.KeyboardModifier.ControlModifier:
            self.explorateur.copy_selected_elements()

        elif key == QtCore.Qt.Key.Key_V and modifiers == QtCore.Qt.KeyboardModifier.ControlModifier:
            Method.paste_file()

        elif key == QtCore.Qt.Key.Key_Return:
            self.interface.explorateur.open_selected_element()

        elif key == QtCore.Qt.Key.Key_Delete:
            Method.delete_file()

        elif key == QtCore.Qt.Key.Key_F2:
            self.interface.renommer_element()


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
                self.keyboardInstance.keyPress(event.key(), event.modifiers())
                self.keyPressed.append(event.key())
            if event.type() == QtCore.QEvent.Type.KeyRelease and self.keyPressed.count(event.key()) > 0:
                self.keyPressed.remove(event.key())
        return QtCore.QObject.eventFilter(self, source, event)
