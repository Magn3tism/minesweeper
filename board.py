import tkinter as tk
import ttkbootstrap as ttk
import random

from config import buttons

window = ttk.Window(themename="flatly")
window.title("Minesweeper")

container = ttk.Frame(master=window)
container.pack(padx=5, pady=5)

def clicked_index(i, j):
    print(buttons[i][j]["content"].get())

def countMines(lst):
    count = 0
    for ele in lst:
        if (ele == -1):
            count = count + 1
    return count

for i in range(13):
    row_frame = ttk.Frame(master=container)
    row_frame.grid()

    for j in range(6):
        buttons[i][j]["content"] = tk.IntVar()

        buttons[i][j]["button"] = ttk.Button(
            master=row_frame, bootstyle="primary-outline", 
            textvariable=buttons[i][j]["content"],
            command=lambda i=i, j=j: clicked_index(i, j))
        
        buttons[i][j]["button"].grid(ipadx=15, ipady=10, row=i, column=j)


count = 0;
while (count < 10):
    a = random.randint(0, 12)
    b = random.randint(0, 5)
    
    if (buttons[a][b]["content"] != -1):
        buttons[a][b]["content"].set(-1);
        count += 1

for i, arr in enumerate(buttons):
    for j, btn in enumerate(arr):
        if (btn["content"].get() == -1 or i == 0 or i == 12 or j == 0 or j == 5):
            continue
        
        subArray = []
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                subArray.append(buttons[k][l]["content"].get())

        btn["content"].set(countMines(subArray))

