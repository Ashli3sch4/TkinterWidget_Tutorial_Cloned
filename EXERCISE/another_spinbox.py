import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title('Tkinter Spinbox Widget')
window.geometry('400x400')

# Spinbox for numbers
int_var = tk.IntVar()
number_spinbox = ttk.Spinbox(window, from_=0, to=100, increment=1, textvariable=int_var, font='Calibri 24 bold')
number_spinbox.pack(pady=20)

# Spinbox for subjects from a predefined list
subjects = ['Maths', 'English', 'Science', 'Computing', 'Latin', 'Arabic', 'Social Studies', 'Sports Science']
subject_var = tk.StringVar()
subject_spinbox = ttk.Spinbox(window, values=subjects, textvariable=subject_var, font='Calibri 18')
subject_spinbox.pack(pady=20)

window.mainloop()
