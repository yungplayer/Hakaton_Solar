from tkinter import *
import tkinter as tk
from tkinter import ttk
import openpyxl

root = tk.Tk()
root.title("Автоматизированная установка ПО")
root.geometry("720x450")
root.resizable(width=False, height=False)

label_1 = tk.Label(root, text='Выбор функции', font=10)
label_1.pack()

level_var = tk.IntVar()

check_1 = tk.Radiobutton(root, text="Настройка логина/пароля для администратора", variable=level_var, value=1)
check_1.place(x=10, y=100)
check_2 = tk.Radiobutton(root, text="Установка ОС", variable=level_var, value=2)
check_2.place(x=10, y=150)
check_3 = tk.Radiobutton(root, text="Установка доп. ПО",  variable=level_var, value=3)
check_3.place(x=10, y=200)
check_4 = tk.Radiobutton(root, text="Обновление ПО", variable=level_var, value=4)
check_4.place(x=10, y=250)

next_ = tk.Button(root, text='Далее', width=7)
next_.place(x=650, y=400)

root.mainloop()
