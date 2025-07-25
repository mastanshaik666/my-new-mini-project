import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)

            entry.insert(0, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.config(bg='light blue')

entry = tk.Entry(root, font="Arial 20", bd=10, relief=tk.GROOVE, justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
]

for i, b in enumerate(buttons):
    btn = tk.Button(root, text=b, font="Arial 18", padx=20, pady=20,bg="orange")
    btn.grid(row=1 + i // 4, column=i % 4)
    btn.bind("<Button-1>", click)

root.mainloop()
