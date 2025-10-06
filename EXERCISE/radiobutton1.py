import tkinter as tk
from tkinter import ttk

# Create the main window
window = tk.Tk()
window.title('Tkinter Radiobutton Example')
window.geometry('400x400')

# Variable to hold the selected radiobutton value
selected_option = tk.StringVar()

# Radiobuttons
radio1 = ttk.Radiobutton(window, text='Option 1', variable=selected_option, value='Option 1')
radio2 = ttk.Radiobutton(window, text='Option 2', variable=selected_option, value='Option 2')
radio3 = ttk.Radiobutton(window, text='Option 3', variable=selected_option, value='Option 3')

radio1.pack()
radio2.pack()
radio3.pack()

# Function to confirm which Radiobutton is selected
def confirm_selection():
    print(f'You selected: {selected_option.get()}')

# Button to trigger the confirmation
confirm_button = ttk.Button(window, text='Confirm Selection', command=confirm_selection)
confirm_button.pack()

window.mainloop()
