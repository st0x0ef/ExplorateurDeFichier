# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt6 UI code generator 6.8.0.dev2410211537
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import os
from PyQt6 import QtCore, QtGui, QtWidgets

from explorateur.InputDialog import Ui_InputDialog
from explorateur.MessageDialog import Ui_MessageDialog

from explorateur.Application import keyboard


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, app, explorateur):
        self.app = app
        self.explorateur = explorateur
        self.widgets = []
        self.selected_widget = None
        self.app.setEvent(keyboard(self, self.explorateur))

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "ressources", "icon.png")))

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 60, 800, 500))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QtWidgets.QWidget()
        self.scrollAreaWidget.setGeometry(QtCore.QRect(0, 60, 800, 500))

        self.widget = QtWidgets.QWidget(parent=self.scrollAreaWidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.widget.setObjectName("widget")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 150, 15))
        self.label_6.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(170, 10, 60, 15))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(270, 10, 150, 15))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setGeometry(QtCore.QRect(450, 10, 140, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(600, 10, 140, 16))
        self.label_10.setObjectName("label_10")
        self.widget_2 = QtWidgets.QWidget(parent=self.scrollAreaWidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 30, 800, 30))
        self.widget_2.setObjectName("widget_2")
        self.label_21 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_21.setGeometry(QtCore.QRect(10, 10, 150, 15))
        self.label_21.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_22.setGeometry(QtCore.QRect(170, 10, 60, 15))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_23.setGeometry(QtCore.QRect(270, 10, 150, 15))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_24.setGeometry(QtCore.QRect(450, 10, 140, 16))
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_25.setGeometry(QtCore.QRect(600, 10, 140, 16))
        self.label_25.setObjectName("label_25")
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 111, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 30, 111, 30))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 30, 111, 30))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 30, 111, 30))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 30, 111, 30))
        self.label_5.setObjectName("label_5")

        self.repertoire = QtWidgets.QLabel(parent=self.centralwidget)
        self.repertoire.setGeometry(QtCore.QRect(10, 0, 800, 30))
        self.repertoire.setObjectName("repertoire")
        self.repertoire.mouseDoubleClickEvent = lambda event: self.changer_repertoire()
        self.repertoire.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")

        self.menuFichier = QtWidgets.QMenu(parent=self.menubar)
        self.menuFichier.setObjectName("menuFichier")

        self.menuExplorateur = QtWidgets.QMenu(parent=self.menubar)
        self.menuExplorateur.setObjectName("menuExplorateur")

        self.menuHistorique = QtWidgets.QMenu(parent=self.menubar)
        self.menuHistorique.setObjectName("menuHistorique")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.actionRenommer = QtGui.QAction(parent=MainWindow)
        self.actionRenommer.setObjectName("actionRenommer")
        self.actionRenommer.triggered.connect(self.renommer_element)
        self.actionOuvrir = QtGui.QAction(parent=MainWindow)
        self.actionOuvrir.setObjectName("actionOuvrir")
        self.actionOuvrir.triggered.connect(self.open_selected_element)
        self.actionOuvrirTerminal = QtGui.QAction(parent=MainWindow)
        self.actionOuvrirTerminal.setObjectName("actionOuvrirTerminal")
        self.actionOuvrirTerminal.triggered.connect(self.explorateur.open_terminal)
        self.actionSupprimer = QtGui.QAction(parent=MainWindow)
        self.actionSupprimer.setObjectName("actionSupprimer")
        self.actionSupprimer.triggered.connect(self.delete_file)
        self.actionCreerDocument = QtGui.QAction(parent=MainWindow)
        self.actionCreerDocument.setObjectName("actionCreerDocument")
        self.actionCreerDocument.triggered.connect(self.creer_document)
        self.actionCreerDossier = QtGui.QAction(parent=MainWindow)
        self.actionCreerDossier.setObjectName("actionCreerDossier")
        self.actionCreerDossier.triggered.connect(self.creer_dossier)
        self.actionCompresserZip = QtGui.QAction(parent=MainWindow)
        self.actionCompresserZip.setObjectName("actionCompresserZip")
        self.actionCompresserZip.triggered.connect(self.action_compresser_zip)
        self.actionCompresserTar = QtGui.QAction(parent=MainWindow)
        self.actionCompresserTar.setObjectName("actionCompresserTar")
        self.actionCompresserTar.triggered.connect(self.action_compresser_tar)

        self.actionChangerRepertoire = QtGui.QAction(parent=MainWindow)
        self.actionChangerRepertoire.setObjectName("actionChangerRepertoire")
        self.actionChangerRepertoire.triggered.connect(self.changer_repertoire)
        self.actionRecharger = QtGui.QAction(parent=MainWindow)
        self.actionRecharger.setObjectName("actionRecharger")
        self.actionRecharger.triggered.connect(self.refresh)
        self.actionQuitter = QtGui.QAction(parent=MainWindow)
        self.actionQuitter.setObjectName("actionQuitter")
        self.actionQuitter.triggered.connect(self.quitter)

        self.actionRetourArriere = QtGui.QAction(parent=MainWindow)
        self.actionRetourArriere.setObjectName("actionRetourArriere")
        self.actionRetourArriere.triggered.connect(self.retourArriere)
        self.actionRetourAvant = QtGui.QAction(parent=MainWindow)
        self.actionRetourAvant.setObjectName("actionRetourAvant")
        self.actionRetourAvant.triggered.connect(self.retourAvant)

        self.menuFichier.addAction(self.actionRenommer)
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionOuvrirTerminal)
        self.menuFichier.addAction(self.actionSupprimer)
        self.menuFichier.addAction(self.actionCreerDocument)
        self.menuFichier.addAction(self.actionCreerDossier)
        self.menuFichier.addAction(self.actionCompresserZip)
        self.menuFichier.addAction(self.actionCompresserTar)

        self.menuExplorateur.addAction(self.actionChangerRepertoire)
        self.menuExplorateur.addAction(self.actionRecharger)
        self.menuExplorateur.addAction(self.actionQuitter)

        self.menuHistorique.addAction(self.actionRetourArriere)
        self.menuHistorique.addAction(self.actionRetourAvant)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuHistorique.menuAction())
        self.menubar.addAction(self.menuExplorateur.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.refresh()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Explorateur de fichier"))
        self.label.setText(_translate("MainWindow", "Nom"))
        self.label_2.setText(_translate("MainWindow", "Création"))
        self.label_3.setText(_translate("MainWindow", "Taille"))
        self.label_4.setText(_translate("MainWindow", "Type"))
        self.label_5.setText(_translate("MainWindow", "Dernière édition"))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier"))
        self.menuExplorateur.setTitle(_translate("MainWindow", "Explorateur"))
        self.menuHistorique.setTitle(_translate("MainWindow", "Historique"))
        self.actionRenommer.setText(_translate("MainWindow", "Renommer"))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir"))
        self.actionOuvrirTerminal.setText(_translate("MainWindow", "Ouvrir dans un terminal"))
        self.actionSupprimer.setText(_translate("MainWindow", "Supprimer"))
        self.actionCreerDocument.setText(_translate("MainWindow", "Créer un document"))
        self.actionCreerDossier.setText(_translate("MainWindow", "Créer un dossier"))
        self.actionCompresserZip.setText(_translate("MainWindow", "Compresser le dossier en archive zip"))
        self.actionCompresserTar.setText(_translate("MainWindow", "Compresser le dossier en archive tar"))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter"))
        self.actionRecharger.setText(_translate("MainWindow", "Recharger"))
        self.actionChangerRepertoire.setText(_translate("MainWindow", "Changer de répertoire"))
        self.actionRetourArriere.setText(_translate("MainWindow", "Retour arrière"))
        self.actionRetourAvant.setText(_translate("MainWindow", "Retour avant"))

    def refresh(self):
        self.scrollArea.hide()
        self.explorateur.reload()
        fichiers = self.explorateur.get_files()

        self.repertoire.setText("Répertoire : " + str(self.explorateur.get_path()))

        if len(self.widgets) == 0:
            self.spacer = QtWidgets.QSpacerItem(800, 30 * len(fichiers), QtWidgets.QSizePolicy.Policy.Expanding,
                                                QtWidgets.QSizePolicy.Policy.Minimum)
            self.scrollAreaWidgetLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidget)
            self.scrollAreaWidgetLayout.addItem(self.spacer)
        else:
            self.spacer.changeSize(800, 30 * len(fichiers), QtWidgets.QSizePolicy.Policy.Expanding,
                                   QtWidgets.QSizePolicy.Policy.Minimum)
            for widget in self.widgets:
                widget.setVisible(False)
                widget.destroy()
            self.widgets.clear()

        for file in fichiers:
            widget = QtWidgets.QWidget(parent=self.scrollAreaWidget)
            widget.setGeometry(QtCore.QRect(0, 30 * file[0], 800, 30))
            widget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
            widget.setObjectName("widget_" + str(file[0]))
            widget.mousePressEvent = lambda event: self.select(event)
            widget.mouseDoubleClickEvent = lambda event: self.open()

            nom = QtWidgets.QLabel(parent=widget)
            nom.setGeometry(QtCore.QRect(10, 10, 200, 15))
            nom.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
            nom.setObjectName("nom_" + str(file[0]))
            nom.setText(str(file[1]))
            taille = QtWidgets.QLabel(parent=widget)
            taille.setGeometry(QtCore.QRect(220, 10, 60, 15))
            taille.setObjectName("taille_" + str(file[0]))
            if file[2] != "":
                taille.setText(str(round(file[2][0])) + " " + str(file[2][1]))
            type = QtWidgets.QLabel(parent=widget)
            type.setGeometry(QtCore.QRect(280, 10, 100, 15))
            type.setObjectName("type_" + str(file[0]))
            type.setText(str(file[3]))
            creation = QtWidgets.QLabel(parent=widget)
            creation.setGeometry(QtCore.QRect(400, 10, 180, 15))
            creation.setObjectName("creation_" + str(file[0]))
            creation.setText(str(file[4]))
            edition = QtWidgets.QLabel(parent=widget)
            edition.setGeometry(QtCore.QRect(600, 10, 180, 15))
            edition.setObjectName("edition_" + str(file[0]))
            edition.setText(str(file[5]))

            widget.setVisible(True)

            self.widgets.append(widget)

        self.scrollArea.show()

    def contextMenuEvent(self, event):
        contextMenu = QtWidgets.QMenu(self)

        if 0 <= self.explorateur.index_fichier_selectionner < len(self.widgets):
            contextMenu.addAction(self.actionRenommer)
            contextMenu.addAction(self.actionOuvrir)
            contextMenu.addAction(self.actionOuvrirTerminal)
            contextMenu.addAction(self.actionSupprimer)
            contextMenu.addAction(self.actionCreerDocument)
            contextMenu.addAction(self.actionCreerDossier)

            if self.explorateur.get_files()[self.explorateur.index_fichier_selectionner][3] == "Dossier":
                contextMenu.addAction(self.actionCompresserZip)
                contextMenu.addAction(self.actionCompresserTar)

            contextMenu.addAction(self.menuHistorique.menuAction())

        contextMenu.exec(event.globalPos())

    def select(self, event: QtGui.QMouseEvent):
        pos = round(event.scenePosition().y() + self.scrollArea.verticalScrollBar().value() - 80)
        for i in range(len(self.widgets)):
            if pos - 30 < self.widgets[i].y() < pos:
                self.selectIndex(i)
            else:
                self.unselectIndex(i)

    def selectIndex(self, index: int):
        if 0 <= index < len(self.widgets):
            self.widgets[index].setStyleSheet('background-color: #8ceaff;')
            self.explorateur.select_file(index)
            self.selected_widget = self.widgets[index]

    def unselectIndex(self, index: int):
        if 0 <= index < len(self.widgets):
            self.widgets[index].setStyleSheet('background-color: none;')

    def open(self):
        if self.explorateur.open_selected_element():
            self.refresh()

    def quitter(self):
        print("bye")
        sys.exit(self.app.exec())

    def delete_file(self):
        if self.selected_widget is not None:
            self.explorateur.delete_file()
            self.refresh()

    def changer_repertoire(self):
        dialog = Ui_InputDialog(self, "changeRepertoire")
        dialog.exec()

    def renommer_element(self):
        dialog = Ui_InputDialog(self, "renommer")
        dialog.exec()

    def retourArriere(self):
        self.explorateur.retourArriere()
        self.refresh()

    def retourAvant(self):
        self.explorateur.retourAvant()
        self.refresh()

    def creer_document(self):
        dialog = Ui_InputDialog(self, "creerDocument")
        dialog.exec()

    def creer_dossier(self):
        dialog = Ui_InputDialog(self, "creerDossier")
        dialog.exec()

    def erreur(self, text):
        dialog = Ui_MessageDialog(text)
        dialog.exec()

    def action_compresser_zip(self):
        if self.explorateur.make_archive("zip"):
            self.refresh()
        else:
            self.erreur("Seuls les dossiers peuvent être compressés")

    def action_compresser_tar(self):
        if self.explorateur.make_archive("gztar"):
            self.refresh()
        else:
            self.erreur("Seuls les dossiers peuvent être compressés")

    def open_selected_element(self):
        if self.explorateur.open_selected_element():
            self.refresh()