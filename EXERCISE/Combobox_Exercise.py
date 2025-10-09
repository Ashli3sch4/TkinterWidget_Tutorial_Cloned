import tkinter as tk
from tkinter import ttk
 
# window
window = tk.Tk()
window.title('Tkinter Combobox Widget')
window.geometry('400x400')
 
# function to update label when combobox selection changes
def update_label(event):
    selected = string_var.get()
    label.config(text=f'You selected: {selected}')
 
# combobox widget
string_var = tk.StringVar()
myCombobox = ttk.Combobox(
    master=window,
    textvariable=string_var,
    values=['This Option', 'That Option', 'Another Option']
)
myCombobox.bind('<<ComboboxSelected>>', update_label)  # bind selection event
 
# label to display selection
label = tk.Label(window, text="Please select an option.")
label.pack(pady=10)
 
# pack combobox
myCombobox.pack(pady=10)
 
# run
window.mainloop()
 