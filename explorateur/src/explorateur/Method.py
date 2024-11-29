import sys
import os
import magic
from pathlib import Path
from explorateur.InputDialog import Ui_InputDialog
from explorateur.MessageDialog import Ui_MessageDialog

interface = None
explorateur = None


def init(i, e):
    global interface, explorateur
    interface = i
    explorateur = e


def open():
    if explorateur.open_selected_element():
        interface.refresh()


def quitter():
    print("bye")
    sys.exit(interface.app.exec())


def delete_file():
    if interface.selected_widget is not None:
        explorateur.delete_file()
        interface.refresh()


def changer_repertoire():
    dialog = Ui_InputDialog(interface, "changeRepertoire")
    dialog.exec()


def renommer_element():
    dialog = Ui_InputDialog(interface, "renommer")
    dialog.exec()


def retourArriere():
    explorateur.retourArriere()
    interface.refresh()


def retourAvant():
    explorateur.retourAvant()
    interface.refresh()


def creer_document():
    dialog = Ui_InputDialog(interface, "creerDocument")
    dialog.exec()


def creer_dossier():
    dialog = Ui_InputDialog(interface, "creerDossier")
    dialog.exec()


def popup(type, text):
    dialog = Ui_MessageDialog(type, text)
    dialog.exec()


def action_compresser_zip():
    if explorateur.make_archive("zip"):
        interface.refresh()
    else:
        popup("Erreur", "Seuls les dossiers peuvent être compressés")


def action_compresser_tar():
    if explorateur.make_archive("gztar"):
        interface.refresh()
    else:
        popup("Erreur", "Seuls les dossiers peuvent être compressés")


def open_selected_element():
    if explorateur.open_selected_element():
        interface.refresh()


def clear_trash():
    os.system("rm -rf ~/.local/share/Trash/*")
    explorateur.set_path(Path.home())
    interface.refresh()


def goto_trash():
    if explorateur.set_path(explorateur.trash_path):
        interface.refresh()
    else:
        popup("Info", "Le dossier corbeil est vide")


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
    elif type_file == "inode/x-empty":
        type_file = "Fichier vide"

    type_file = type_file.replace("application/", "")
    type_file = type_file.replace("image/", "")
    type_file = type_file.replace("text/", "")

    type_file = type_file.capitalize()

    return type_file

def paste_file():
    explorateur.paste_file()
    interface.refresh()
