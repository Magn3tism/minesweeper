import tkinter as tk
from PIL import ImageTk, Image

from config import buttons

def left_click(i, j):
    value = buttons[i][j]["content"]
    if (value >= 0):
        image = ImageTk.PhotoImage(Image.open(f"./images/{value}.png"))
        buttons[i][j]["button"].configure(image=image, compound=tk.CENTER)
        buttons[i][j]["button"].image = image

def right_click(i, j):
    buttons[i][j]["button"].configure(bootstyle="dark")

# import tkinter as tk
# from PIL import ImageTk, Image

# from config import buttons

# images = []

# def create_images():
#     global images
#     images = []
#     for i in range(10):
#         image = ImageTk.PhotoImage(Image.open("./images/1.png"))
#         images.append(image)

# create_images()

# def left_click(i, j):
#     value = buttons[i][j]["content"]
#     if (value > 0):
#       n_image = images[value - 1]
#       buttons[i][j]["button"].configure(image=n_image, compound=tk.CENTER)
#       buttons[i][j]["button"].image = n_image

# def right_click(i, j):
#     buttons[i][j]["button"].configure(bootstyle="dark")

