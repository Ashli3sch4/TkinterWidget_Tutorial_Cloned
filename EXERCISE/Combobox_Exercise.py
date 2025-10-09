import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Tkinter Combobox Widget')
window.geometry('400x400')

string_var = tk.StringVar()
myCombobox = ttk.Combobox(master = window, textvariable = string_var,values=['This Option', 'That Option', 'Another Option'])

myCombobox.pack()

window.mainloop()