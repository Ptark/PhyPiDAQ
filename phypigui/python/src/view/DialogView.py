from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class DialogView:
    @staticmethod
    def __new_dialog() -> QMessageBox:
        dialog = QMessageBox()
        dialog.setIcon(QMessageBox.Critical)
        dialog.setWindowIcon(QIcon('../resources/images/PhiPi_icon.png'))
        return dialog

    @staticmethod
    def show_info(title: str, description: str):
        dialog = DialogView.__new_dialog()

        dialog.setIcon(QMessageBox.Information)
        dialog.addButton(QMessageBox.Ok)

        dialog.setWindowTitle(dialog.tr("Information"))
        dialog.setText(title)
        dialog.setInformativeText(description)

        dialog.exec()

    @staticmethod
    def show_warning(title: str, description: str):
        dialog = DialogView.__new_dialog()

        dialog.setIcon(QMessageBox.Warning)
        dialog.addButton(QMessageBox.Close)

        dialog.setWindowTitle(dialog.tr("Warnung"))
        dialog.setText(title)
        dialog.setInformativeText(description)

        dialog.exec()

    @staticmethod
    def show_error(title: str, description: str):
        dialog = DialogView.__new_dialog()

        dialog.setIcon(QMessageBox.Critical)
        dialog.addButton(QMessageBox.Close)

        dialog.setWindowTitle(dialog.tr("Fehler"))
        dialog.setText(title)
        dialog.setInformativeText(description)
        dialog.setAttribute(Qt.WA_QuitOnClose)
        dialog.exec()
