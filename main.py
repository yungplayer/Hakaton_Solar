from tkinter import *
import tkinter as tk
from tkinter import ttk
import openpyxl

inos_OS = ("Windows", "macOS")
ours_OS = []

book = openpyxl.open("OS_DB.xlsx", read_only = True)
sheet = book.active
for row in range(2, 16):
    ino_OS = sheet[row][0].value
    our_OS = sheet[row][1].value
    sertf = sheet[row][2].value
    typee = sheet[row][3].value
    ours_OS.append(our_OS)


root = tk.Tk()
root.title("Автоматизированная установка ПО")
root.geometry("720x450")
root.resizable(width=False, height=False)

label_1 = tk.Label(root, text='Выберите заменяемую ОС')
label_1.place(x=10, y=140)

label_2 = tk.Label(root, text='Выберите заменяемую ОС')
label_2.place(x=445, y=140)

combo_1 = ttk.Combobox(root, values=inos_OS, width=40)
combo_1.current(0)
combo_1.place(x=10, y=175)

combo_2 = ttk.Combobox(root, values=ours_OS, width=40)
combo_2.current(0)
combo_2.place(x=445, y=175)

next_ = tk.Button(root, text='Далее', width=7)
next_.place(x=650, y=400)


root.mainloop()
