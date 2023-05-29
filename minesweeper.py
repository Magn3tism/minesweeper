import tkinter as tk
import ttkbootstrap as ttk
import random

from config import buttons

window = ttk.Window(themename="flatly")
window.title("Minesweeper")

container = ttk.Frame(master=window)
container.pack(padx=5, pady=5)

def clicked_index(i, j):
    print(buttons[i][j]["content"])

for i in range(13):
    row_frame = ttk.Frame(master=container)
    row_frame.grid()

    for j in range(6):
        buttons[i][j]["button"] = ttk.Button(
            master=row_frame, bootstyle="primary-outline", 
            command=lambda i=i, j=j: clicked_index(i, j))
        
        buttons[i][j]["button"].grid(ipadx=15, ipady=10, row=i, column=j)


count = 0;

while (count < 10):
    a = random.randint(0, 12)
    b = random.randint(0, 5)
    
    if (not buttons[a][b]["content"]):
        buttons[a][b]["content"] = -1;
        count += 1

# Start main loop
window.mainloop()
