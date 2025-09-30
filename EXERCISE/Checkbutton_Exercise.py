import tkinter as tk
from tkinter import ttk

# This section creaetes the Tkinter Window and adds the required elements to it
window = tk.Tk()
window.title('Tkinter Checkbutton Widget')
window.geometry('400x400')

# this ius our Checknbutton
bool_var = tk.BooleanVar()
Boolean_checkbutton = ttk.Checkbutton(window, variable = bool_var, text = 'Are you happy?', onvalue = True)

#Pack elements in frames ready to push onto form/window
Boolean_checkbutton.pack()

# run the program to generate window with all packed elements for user interaction 
window.mainloop()