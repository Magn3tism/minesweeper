from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget
from config import buttons


class GameBoard(QMainWindow):
    def __init__(self):
        super().__init__()
        global buttons

        self.setWindowTitle("Minesweeper")

        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.add_buttons()

        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)

    def left_click(self, i, j):
        pass

    def add_buttons(self):
        for i in range(13):
            for j in range(6):
                buttons[i][j]["content"] = QPushButton("")
                buttons[i][j]["content"].clicked.connect(
                    lambda event, i=i, j=j: self.left_click(i, j))
                self.layout.addWidget(buttons[i][j]["content"], i, j)


app = QApplication([])

window = GameBoard()
window.show()
