import tkinter as tk
import ttkbootstrap as ttk
import random

import config

window = ttk.Window(themename="flatly")
window.title("Minesweeper")

container = ttk.Frame(master=window)
container.pack(padx=5, pady=5)

for i in range(13):
    row_frame = ttk.Frame(master=container)
    row_frame.grid()

    for j in range(6):
        config.buttons[i][j]['button'] = ttk.Button(
            master=row_frame, bootstyle="primary-outline")
        config.buttons[i][j]['button'].grid(ipadx=15, ipady=10, row=i, column=j)


# Start main loop
window.mainloop()
