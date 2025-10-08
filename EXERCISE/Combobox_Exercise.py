import tkinter as tk
from tkinter import ttk
 
#window
window = tk.Tk()
window.title('Tkinter Combobox Widget')
window.geometry('400x400')
 
#combobox widget
string_var = tk.StringVar()
myCombobox = ttk.Combobox(master = window, textvariable = string_var, values=['This Options', 'That Options', 'Another Option'])
 
#pack
myCombobox.pack()
 
#run
window.mainloop()
 