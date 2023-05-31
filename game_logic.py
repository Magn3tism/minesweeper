import tkinter as tk
from PIL import ImageTk, Image

from config import buttons


def hit_mine():
    print("Game Over!")
    for row in buttons:
        for btn in row:
            if (btn["content"] == -1):
                image = ImageTk.PhotoImage(Image.open("./images/mine.png"))

                btn["button"].configure(image=image, compound=tk.CENTER)
                btn["button"].image = image
            btn["button"].configure(state="disabled")


def click_number():
    pass


def left_click(i, j):
    value = buttons[i][j]["content"]
    if (value == -2):
        return

    if (value >= 0):
        image = ImageTk.PhotoImage(Image.open(f"./images/{value}.png"))
        click_number()
    else:
        image = ImageTk.PhotoImage(Image.open("./images/mine.png"))
        hit_mine()

    buttons[i][j]["button"].configure(image=image, compound=tk.CENTER)
    buttons[i][j]["button"].image = image


def right_click(i, j):
    if (buttons[i][j]["content"] == -2):
        buttons[i][j]["button"].configure(image="")
        buttons[i][j]["content"] = -1
        return

    image = ImageTk.PhotoImage(Image.open("./images/flag.png"))
    buttons[i][j]["button"].configure(image=image, compound=tk.CENTER)
    buttons[i][j]["button"].image = image
    buttons[i][j]["content"] = -2
