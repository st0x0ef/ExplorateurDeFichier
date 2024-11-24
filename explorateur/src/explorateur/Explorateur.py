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
        self.index_fichier_selectionner = -1
        self.path = Path.home()
        self.trash_path = str(self.path) + "/.local/share/Trash/files"
        self.historique = [str(self.path)]
        self.index_historique = 0

    def reload(self):
        self.fichiers.clear()
        self.index_fichier_selectionner = -1

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

    def select_file(self, index: int):
        self.index_fichier_selectionner = index

    def open_selected_folder(self):
        self.set_path(self.fichiers[self.index_fichier_selectionner][6])

        if len(self.historique) - 1 == self.index_historique:
            self.historique.append(str(self.path))
            self.index_historique = len(self.historique) - 1
        else:
            self.historique = self.historique[:self.index_historique + 1]
            self.historique.append(str(self.path))
            self.index_historique = len(self.historique) - 1

    def get_selected_file(self) -> []:
        return self.fichiers[self.index_fichier_selectionner]

    def open_selected_file(self):
        if os.access(str(self.fichiers[self.index_fichier_selectionner][6]), os.X_OK):
            subprocess.call(str(self.fichiers[self.index_fichier_selectionner][6]))
        else:
            subprocess.call(['xdg-open', str(self.fichiers[self.index_fichier_selectionner][6])])

    def open_selected_element(self):
        if self.index_fichier_selectionner >= 0:
            if self.fichiers[self.index_fichier_selectionner][3] == "Dossier":
                self.open_selected_folder()
                return True
            else:
                self.open_selected_file()
                return False

    def delete_file(self):
        if self.index_fichier_selectionner >= 0:
            send2trash.send2trash(str(self.fichiers[self.index_fichier_selectionner][6]))

            for i in range(len(self.fichiers) - self.index_fichier_selectionner):
                self.fichiers[i][0] -= 1

            self.fichiers.pop(self.index_fichier_selectionner)

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
        if self.index_fichier_selectionner >= 0:
            os.rename(self.fichiers[self.index_fichier_selectionner][6], str(self.path) + "/" + new_name)
            self.fichiers[self.index_fichier_selectionner][1] = new_name
            self.fichiers[self.index_fichier_selectionner][6] = str(self.path) + "/" + new_name

    def make_archive(self, type: str):
        if self.index_fichier_selectionner >= 0:
            if self.fichiers[self.index_fichier_selectionner][3] == "Dossier":
                shutil.make_archive(str(self.path) + "/" + self.fichiers[self.index_fichier_selectionner][1],
                                    type,
                                    root_dir=self.fichiers[self.index_fichier_selectionner][6])
                return True

            else:
                return False

    def open_terminal(self):
        if self.index_fichier_selectionner >= 0:
            if self.fichiers[self.index_fichier_selectionner][3] == "Dossier":
                os.system("gnome-terminal --working-directory=" + str(
                    self.fichiers[self.index_fichier_selectionner][6]).replace(" ", r"\ "))

            else:
                os.system("gnome-terminal --working-directory=" + str(self.path).replace(" ", r"\ "))
        else:
            os.system("gnome-terminal --working-directory=" + str(self.path).replace(" ", r"\ "))
