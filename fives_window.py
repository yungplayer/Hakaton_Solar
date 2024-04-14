from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.title("Автоматизированная установка ПО")
root.geometry("720x450")
root.resizable(width=False, height=False)

label_1 = tk.Label(root, text='Процесс установки доп. ПО', font=10)
label_1.pack()

value_var = IntVar()

progressbar = ttk.Progressbar(orient="horizontal", variable=value_var)
progressbar.place(y=80, x=58, width=600)

label = ttk.Label(textvariable=value_var)
label.place(x=57,y=102)

journal = tk.Entry()
journal.place(y=140, x=58, width=600, height=160)


def start(): progressbar.start(100)  # запускаем progressbar

def stop(): progressbar.stop()  # останавливаем progressbar

start_btn = ttk.Button(text="Start", command=start)
start_btn.pack(anchor=SW, side=LEFT, padx=6, pady=6)
stop_btn = ttk.Button(text="Stop", command=stop)
stop_btn.pack(anchor=SE, side=RIGHT, padx=6, pady=6)

root.mainloop()