# Form implementation generated from reading ui file 'repertoire.ui'
#
# Created by: PyQt6 UI code generator 6.8.0.dev2410211537
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import os
import re
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_InputDialog(QtWidgets.QDialog):
    def __init__(self, interface, dialogType):
        super().__init__()

        self.interface = interface

        self.possibleCharacterFile = r'[^\-_.a-zA-Z0-9]'
        self.possibleCharacterFolder = r'[^\-_a-zA-Z0-9]'

        self.dialogType = dialogType

        self.setWindowIcon(QtGui.QIcon('ressources/icon.png'))

        self.setObjectName("Dialog")
        self.resize(400, 100)
        self.pushButton = QtWidgets.QPushButton(parent=self)
        self.pushButton.setGeometry(QtCore.QRect(170, 70, 80, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.mousePressEvent = lambda event: self.entrer()
        self.lineEdit = QtWidgets.QLineEdit(parent=self)
        self.lineEdit.setGeometry(QtCore.QRect(25, 20, 350, 23))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        match self.dialogType:
            case "changeRepertoire":
                self.setWindowTitle(_translate("Dialog", "Changer de répertoire"))
                self.lineEdit.setText(_translate("Dialog", str(self.interface.explorateur.path)))
                self.lineEdit.setPlaceholderText(
                    _translate("Dialog", "Entrez le répertoire auquel vous souhaitez accéder"))
            case "renommer":
                self.setWindowTitle(_translate("Dialog", "Renommer un élément"))
                self.lineEdit.setText(_translate("Dialog", str(self.interface.explorateur.get_selected_file()[1])))
                self.lineEdit.setPlaceholderText(_translate("Dialog", "Entrez le nouveau nom du document"))
            case "creerDocument":
                self.setWindowTitle(_translate("Dialog", "Créer un document"))
                self.lineEdit.setText(_translate("Dialog", ""))
                self.lineEdit.setPlaceholderText(_translate("Dialog", "Entrez le nom du document"))
            case "creerDossier":
                self.setWindowTitle(_translate("Dialog", "Créer un dossier"))
                self.lineEdit.setText(_translate("Dialog", ""))
                self.lineEdit.setPlaceholderText(_translate("Dialog", "Entrez le nom du dossier"))
            case _:
                self.setWindowTitle(_translate("Dialog", "Erreur"))

        self.pushButton.setText(_translate("Dialog", "Entrer"))

    def entrer(self):
        if self.dialogType == "renommer":
            self.interface.explorateur.rename_file(self.lineEdit.text())

        elif self.dialogType == "creerDocument":
            if not re.search(self.possibleCharacterFile, self.lineEdit.text()):
                file_dest = str(self.interface.explorateur.path) + "/" + self.lineEdit.text()
                if not os.path.exists(file_dest):
                    open(file_dest, "x")
                else:
                    self.interface.erreur("Un fichier portant le même nom existe déjà")
                    return
            else:
                self.interface.erreur("Seul les charactères -_.a-zA-Z0-9 peuvent être utilisé\ndans le nom du fichier")
                return

        elif self.dialogType == "creerDossier":
            if not re.search(self.possibleCharacterFolder, self.lineEdit.text()):
                path_dest = str(self.interface.explorateur.path) + "/" + self.lineEdit.text()
                if not os.path.exists(path_dest):
                    os.makedirs(path_dest)
                else:
                    self.interface.erreur("Un dossier portant le même nom existe déjà")
                    return
            else:
                self.interface.erreur("Seul les charactères -_a-zA-Z0-9 peuvent être utilisé\ndans le nom du dossier")
                return

        elif self.dialogType == "changeRepertoire":
            if not os.path.exists(self.lineEdit.text()):
                self.interface.erreur("Le répertoire n'existe pas")
                return
            self.interface.explorateur.set_path(self.lineEdit.text())

            if len(self.interface.explorateur.historique) - 1 == self.interface.explorateur.index_historique:
                self.interface.explorateur.historique.append(str(self.lineEdit.text()))
                self.interface.explorateur.index_historique = len(self.interface.explorateur.historique) - 1
            else:
                self.interface.explorateur.historique = self.interface.explorateur.historique[
                                                        :self.interface.explorateur.index_historique + 1]
                self.interface.explorateur.historique.append(str(self.lineEdit.text()))
                self.interface.explorateur.index_historique = len(self.interface.explorateur.historique) - 1

        self.interface.refresh()
        self.close()
