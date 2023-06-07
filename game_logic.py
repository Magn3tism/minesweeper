import tkinter as tk
from PIL import ImageTk, Image

from config import buttons

unclicked_cells = 13 * 6

backup = {}

def get_surrounding_elements(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])

    surrounding_values = []

    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if i != row or j != col:
                surrounding_values.append(matrix[i][j])

    return surrounding_values


def hit_mine():
    print("Game Over!")
    for row in buttons:
        for btn in row:
            if (btn["content"] == -1):
                image = ImageTk.PhotoImage(Image.open("./images/mine.png"))

                btn["button"].configure(image=image, compound=tk.CENTER)
                btn["button"].image = image
            btn["button"].configure(state="disabled")


def click_number(i, j):
    global unclicked_cells

    if (unclicked_cells == 12):
        print("Win!")
        return

    surrounding = get_surrounding_elements(buttons, i, j)

    print(surrounding)
    print(unclicked_cells)

    if (buttons[i][j]["content"] == 0):
        buttons[i][j]["content"] = 100
        for btn in surrounding:
            if (btn["content"] < 100):
                btn["button"].invoke()
        return


def left_click(i, j):
    global unclicked_cells

    value = buttons[i][j]["content"]
    if (value == -2):
        return

    if (value == 100 or value == 0):
        if (value == 0):
            unclicked_cells -= 1
        buttons[i][j]["button"].configure(style="secondary.TButton")
        click_number(i, j)
        return

    if (value > 0 and value < 100):
        unclicked_cells -= 1
        buttons[i][j]["content"] = 101
        image = ImageTk.PhotoImage(Image.open(f"./images/{value}.png"))
        click_number(i, j)
    elif (value == -1):
        image = ImageTk.PhotoImage(Image.open("./images/mine.png"))
        hit_mine()

    buttons[i][j]["button"].configure(image=image, compound=tk.CENTER)
    buttons[i][j]["button"].image = image


def right_click(i, j):
    if (buttons[i][j]["content"] == -2):
        buttons[i][j]["button"].configure(image="")
        buttons[i][j]["content"] = backup[f"${i}${j}"]
        return

    image = ImageTk.PhotoImage(Image.open("./images/flag.png"))
    buttons[i][j]["button"].configure(image=image, compound=tk.CENTER)
    buttons[i][j]["button"].image = image
    backup[f"${i}${j}"] = buttons[i][j]["content"]
    buttons[i][j]["content"] = -2
