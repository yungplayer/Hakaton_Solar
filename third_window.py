from tkinter import *
import tkinter as tk
from tkinter import ttk
import openpyxl

root = tk.Tk()
root.title("Автоматизированная установка ПО")
root.geometry("720x450")
root.resizable(width=False, height=False)

label_1 = tk.Label(root, text='Выбор хостов для инсталяции ОС и доп. ПО', font=10)
label_1.pack()

label_2 = tk.Label(root, text='Доступные хосты')
label_2.place(x=10, y=140)

label_3 = tk.Label(root, text='Список выбранных хостов')
label_3.place(x=448, y=140)

label_4 = tk.Label(root, text='Файл с необходимыми хостами')
label_4.place(x=10, y=250)


spisok = ["192.168.0.1", "192.168.0.2", "192.168.0.3"]
combo_1 = ttk.Combobox(root, width=40)
combo_1.current()
combo_1.place(x=10, y=275)

combo_2 = ttk.Combobox(root, values=spisok, width=40)
combo_2.current(0)
combo_2.place(x=10, y=175)

journal = tk.Entry()
journal.place(y=175, x=452, width=250, height=150)

next_ = tk.Button(root, text='Далее', width=7)
next_.place(x=650, y=400)

root.mainloop()