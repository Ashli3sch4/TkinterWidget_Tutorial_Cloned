import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title('Tkinter Spinbox Widget')
window.geometry('400x400')

# Variable for Spinbox
int_var = tk.DoubleVar()

# Spinbox widget
number_spinbox = ttk.Spinbox(window, from_=0, to=100, increment=0.01, textvariable=int_var, font='Calibri 24 bold')
number_spinbox.pack(pady=20)

# Label that will display the current value of the Spinbox
value_label = ttk.Label(window, text=f"Current Value: {int_var.get()}", font='Calibri 18')
value_label.pack(pady=10)

# Function to update label when Spinbox value changes
def update_label(*args):
    value_label.config(text=f"Current Value: {int_var.get()}")

# Trace variable changes to call update_label function
int_var.trace_add('write', update_label)

window.mainloop()
