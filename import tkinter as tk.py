import tkinter as tk
from tkinter import filedialog

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        text.delete(1.0, tk.END)
        with open(file_path, "r") as file:
            text.insert(tk.INSERT, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))

root = tk.Tk()
root.title("Simple Text Editor")

text = tk.Text(root, wrap=tk.WORD)
text.pack(expand=True, fill=tk.BOTH)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()