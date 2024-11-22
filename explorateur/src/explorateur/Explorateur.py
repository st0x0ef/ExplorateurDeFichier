import os
import time
import subprocess
from pathlib import Path
import shutil
import magic


def find_size_in_good_unit(octets: int) -> tuple:
    i = 0
    while octets / 1024 >= 1:
        octets /= 1024
        i += 1
        if i > 5:
            print("Le fichier est trop gros")
            return octets * 1024, 5
    return octets, convert_number_to_size_units(i)


def convert_number_to_size_units(nb: int) -> str:
    match nb:
        case 0:
            return "o"
        case 1:
            return "ko"
        case 2:
            return "mo"
        case 3:
            return "go"
        case 4:
            return "to"
        case 5:
            return "po"
        case _:
            return ""


def convert_number_to_octet(nb: float, unit: int) -> float:
    while unit > 0:
        nb *= 1024
        unit -= 1
    return nb


def find_file_type(path_entry: str) -> str:
    type_file = magic.from_file(path_entry, mime=True)

    if type_file == "text/plain":
        type_file = "Document texte"
    elif type_file == "application/pdf":
        type_file = "Document PDF"
    elif type_file == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        type_file = "Document Word"

    type_file = type_file.replace("application/", "")
    type_file = type_file.replace("image/", "")
    type_file = type_file.replace("text/", "")

    type_file = type_file.capitalize()

    return type_file


class explorateur:
    def __init__(self):
        self.fichiers = []
        self.index_fichier_selectionner = -1
        self.path = Path.home()
        self.historique = [str(self.path)]
        self.index_historique = 0

    def reload(self):
        self.fichiers.clear()
        self.index_fichier_selectionner = -1

        i = 0
        with os.scandir(self.path) as it:
            for entry in it:
                if not entry.name.startswith('.'):
                    if entry.is_dir():
                        self.fichiers.append([i, entry.name, "", "Dossier", time.ctime(os.path.getmtime(entry.path)),
                                              time.ctime(os.path.getctime(entry.path)), entry.path])
                    else:
                        self.fichiers.append(
                            [i, entry.name, find_size_in_good_unit(os.path.getsize(entry.path)),
                             find_file_type(str(entry.path)),
                             time.ctime(os.path.getmtime(entry.path)), time.ctime(os.path.getctime(entry.path)),
                             entry.path])
                    i += 1

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
            os.remove(self.fichiers[self.index_fichier_selectionner][6])

            for i in range(len(self.fichiers) - self.index_fichier_selectionner):
                self.fichiers[i][0] -= 1

            self.fichiers.pop(self.index_fichier_selectionner)

    def set_path(self, path: str):
        self.path = path

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
