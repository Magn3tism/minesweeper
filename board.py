from PyQt6 import QtCore
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Minesweeper")
        self.setMinimumSize(QSize(500, 300))


app = QApplication([])

window = MainWindow()
window.show()
