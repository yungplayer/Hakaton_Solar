from tkinter import *
import tkinter as tk
from tkinter import ttk
import openpyxl

root = tk.Tk()
root.title("Автоматизированная установка ПО")
root.geometry("720x450")
root.resizable(width=False, height=False)

label_1 = tk.Label(root, text='Установка дополнительного ПО', font=10)
label_1.pack()

label_2 = tk.Label(root, text='Рекомендуемое ПО')
label_2.place(x=10, y=140)

label_3 = tk.Label(root, text='Поиск необходимого вам ПО')
label_3.place(x=448, y=140)

check_1 = tk.Checkbutton(root, text="Positive Technologies Application Inspector")
check_1.place(x=10, y=190)
check_2 = tk.Checkbutton(root, text="Kaspersky Web Traffic Security")
check_2.place(x=10, y=210)
check_3 = tk.Checkbutton(root, text="Kaspersky Linux Mail Security")
check_3.place(x=10, y=230)
check_4 = tk.Checkbutton(root, text="SafeERP Security Suite")
check_4.place(x=10, y=250)
check_5 = tk.Checkbutton(root, text="ПАК «Соболь»")
check_5.place(x=10, y=270)
check_6 = tk.Checkbutton(root, text="vGate")
check_6.place(x=10, y=290)

spisok = ['Solar webProxy', 'DDoS-GUARD', 'Kaspersky Anti Targeted Attack Platform']
combo_1 = ttk.Combobox(root, values=spisok, width=40)
combo_1.current(0)
combo_1.place(x=450, y=175)

next_ = tk.Button(root, text='Далее', width=7)
next_.place(x=650, y=400)

root.mainloop()