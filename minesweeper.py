import tkinter as tk
import ttkbootstrap as ttk

window = ttk.Window(themename="flatly")
window.title("Minesweeper")

buttons = [[[] for i in range(6)] for i in range(13)]

container = ttk.Frame(master=window)
container.pack(padx=5, pady=5)

for i in range(13):
    row_frame = ttk.Frame(master=container)
    row_frame.grid()

    for j in range(6):
        buttons[i][j] = ttk.Button(
            master=row_frame, bootstyle="primary-outline")
        buttons[i][j].grid(ipadx=15, ipady=10, row=i, column=j)


window.mainloop()
