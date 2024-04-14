from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("Автоматизированная установка ПО")
root.geometry("720x450")
root.resizable(width=False, height=False)

label_1 = tk.Label(root, text='Укажите расположениe журнала инсталяции', font=10)
label_1.pack()

Dyrect = ['C/', 'D/']

combo_1 = ttk.Combobox(root, values=Dyrect, width=100)
combo_1.current(0)
combo_1.place(x=50, y=100)

next_ = tk.Button(root, text='Далее', width=7)
next_.place(x=650, y=400)

root.mainloop()