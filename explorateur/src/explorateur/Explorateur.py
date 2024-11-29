import os
import time
import subprocess
from pathlib import Path
import shutil
import send2trash
from explorateur import Method


class explorateur:
    def __init__(self):
        self.fichiers = []
        self.index_fichier_selectionner = []
        self.path = Path.home()
        self.trash_path = str(Path.home()) + "/.local/share/Trash/files"
        self.historique = [str(Path.home())]
        self.index_historique = 0
        self.fichiers_copier = []

    def reload(self):
        self.fichiers.clear()
        self.index_fichier_selectionner = []

        dossier = []
        fichier = []

        with os.scandir(self.path) as it:
            for entry in it:
                if not entry.name.startswith('.'):
                    if entry.is_dir():
                        dossier.append([0, entry.name, "", "Dossier", time.ctime(os.path.getmtime(entry.path)),
                                        time.ctime(os.path.getctime(entry.path)), entry.path])
                    else:
                        fichier.append(
                            [0, entry.name, Method.find_size_in_good_unit(os.path.getsize(entry.path)),
                             Method.find_file_type(str(entry.path)),
                             time.ctime(os.path.getmtime(entry.path)), time.ctime(os.path.getctime(entry.path)),
                             entry.path])

        self.fichiers = sorted(dossier, key=lambda x: x[3])
        self.fichiers.extend(sorted(fichier, key=lambda x: x[3]))

        for i in range(len(self.fichiers)):
            self.fichiers[i][0] = i

    def get_files(self) -> []:
        return self.fichiers

    def select_file(self, index: int, clear: bool):
        if clear:
            self.index_fichier_selectionner.clear()
        self.index_fichier_selectionner.append(index)

    def open_selected_folder(self):
        if len(self.index_fichier_selectionner) > 0:
            self.set_path(self.fichiers[self.index_fichier_selectionner[0]][6])

            if len(self.historique) - 1 == self.index_historique:
                self.historique.append(str(self.path))
                self.index_historique = len(self.historique) - 1
            else:
                self.historique = self.historique[:self.index_historique + 1]
                self.historique.append(str(self.path))
                self.index_historique = len(self.historique) - 1

    def get_selected_file(self) -> []:
        fichier_selectionner = []
        for i in self.index_fichier_selectionner:
            fichier_selectionner.append(self.fichiers[i])
        return fichier_selectionner

    def open_selected_element(self):
        for fichier in self.get_selected_file():
            if fichier[3] == "Dossier":
                self.open_selected_folder()
                return True
            else:
                if os.access(str(fichier[6]), os.X_OK):
                    subprocess.call(str(fichier[6]))
                else:
                    subprocess.call(['xdg-open', str(fichier[6])])
        return False

    def delete_file(self):
        for fichier in self.get_selected_file():
            send2trash.send2trash(str(fichier[6]))
        self.reload()

    def set_path(self, path: str):
        if os.path.exists(path):
            self.path = path
            return True
        return False

    def get_path(self):
        return self.path

    def retourArriere(self):
        if self.index_historique > 0:
            self.index_historique -= 1
            self.set_path(self.historique[self.index_historique])

    def retourAvant(self):
        if len(self.historique) > (self.index_historique + 1):
            self.index_historique += 1
            self.set_path(self.historique[self.index_historique])

    def rename_file(self, new_name: str):
        if len(self.index_fichier_selectionner) == 1:
            os.rename(self.fichiers[self.index_fichier_selectionner[0]][6], str(self.path) + "/" + new_name)
            self.fichiers[self.index_fichier_selectionner[0]][1] = new_name
            self.fichiers[self.index_fichier_selectionner[0]][6] = str(self.path) + "/" + new_name
        else:
            Method.popup("Erreur", "Vous ne pouvez renommer qu'un seul élément à la fois")

    def make_archive(self, type: str):
        for fichier in self.get_selected_file():
            if fichier[3] == "Dossier":
                shutil.make_archive(str(fichier[6]), type, root_dir=fichier[6])
                return True
            else:
                return False

    def copy_selected_elements(self):
        self.fichiers_copier.clear()
        for fichier in self.get_selected_file():
            self.fichiers_copier.append(str(fichier[6]))

    def paste_file(self):
        for fichier in self.fichiers_copier:
            if os.path.exists(str(self.path) + "/" + fichier.split("/")[-1]):
                Method.popup("Erreur", "Un fichier portant le même nom existe déjà")
            else:
                shutil.copy(fichier, str(self.path))
                self.reload()

    def open_terminal(self):
        if len(self.index_fichier_selectionner) > 0:
            for fichier in self.get_selected_file():
                if fichier[3] == "Dossier":
                    os.system("gnome-terminal --working-directory=" + str(fichier[6]).replace(" ", r"\ "))
                    return True
                else:
                    os.system("gnome-terminal --working-directory=" + str(self.path).replace(" ", r"\ "))
                    return False
        else:
            os.system("gnome-terminal --working-directory=" + str(self.path).replace(" ", r"\ "))
