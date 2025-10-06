import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title('Tkinter Checkbutton Widget')
window.geometry('400x400')

# Variable for Checkbutton
bool_var = tk.BooleanVar()

# Checkbutton widget
Boolean_checkbutton = ttk.Checkbutton(window, variable=bool_var, text='Are you happy?', onvalue=True, offvalue=False)
Boolean_checkbutton.pack(pady=20)

# Label to update based on Checkbutton state
status_label = ttk.Label(window, text="", font='Calibri 16')
status_label.pack(pady=10)

# Function to update label based on Checkbutton state
def update_label():
    if bool_var.get():
        status_label.config(text="I am very HAPPY for you!")
    else:
        status_label.config(text="")

# Link the function to the variable change
bool_var.trace_add('write', lambda *args: update_label())

window.mainloop()
