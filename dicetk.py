import tkinter as tk
import random

def roll_dice():
    number = random.randint(1, 6)
    label.config(text=str(number))

root = tk.Tk()
root.title("Dice Roller")
root.geometry("700x300")
root.config(bg='green')
label = tk.Label(root, text="", font=("Helvetica", 100))
label.pack()

btn = tk.Button(root, text="Roll", command=roll_dice, font=("Helvetica", 16))
btn.pack()

root.mainloop()
