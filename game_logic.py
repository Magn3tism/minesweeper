from config import buttons

def left_click(i, j):
    buttons[i][j]["button"].configure(bootstyle="primary")

def right_click(i, j):
    buttons[i][j]["button"].configure(bootstyle="dark")