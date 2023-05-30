import tkinter as tk
import ttkbootstrap as ttk
import random

from config import buttons
import game_logic

window = ttk.Window(themename="flatly")
window.title("Minesweeper")

container = ttk.Frame(master=window)
container.pack(padx=5, pady=5)

def countMines(lst):
    count = 0
    for ele in lst:
        if (ele == -1):
            count = count + 1
    return count

def get_surrounding_values(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])

    surrounding_values = []
    
    for i in range(max(0, row - 1), min(row + 2, rows)):
        for j in range(max(0, col - 1), min(col + 2, cols)):
            if i != row or j != col:
                surrounding_values.append(matrix[i][j]["content"])
    
    return surrounding_values

for i in range(13):
    row_frame = ttk.Frame(master=container)
    row_frame.grid()

    for j in range(6):
        buttons[i][j]["button"] = ttk.Button(
            master=row_frame, bootstyle="primary-outline", width=5,
            command=lambda i=i, j=j: game_logic.left_click(i, j))
        
        buttons[i][j]["button"].bind("<Button-3>", lambda event, i=i, j=j: game_logic.right_click(i, j))

        buttons[i][j]["button"].grid(ipady=10, row=i, column=j)

count = 0;
while (count < 10):
    a = random.randint(0, 12)
    b = random.randint(0, 5)
    
    if (buttons[a][b]["content"] != -1 and (-1 not in get_surrounding_values(buttons, a, b) or random.randint(0, 1))):
        buttons[a][b]["content"] = -1;
        count += 1

for i, arr in enumerate(buttons):
    for j, btn in enumerate(arr):
        if (btn["content"] == -1):
            continue

        subArray = get_surrounding_values(buttons, i, j)

        btn["content"] = countMines(subArray)

