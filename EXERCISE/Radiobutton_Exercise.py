import tkinter as tk
from tkinter import ttk

# This section creates the Tkinter Window and adds the requires elements to it 
window = tk.Tk()
window.title('Tkinter Radiobutton Widget')
window.geometry('400x400')

# Frame 
radiobutton_frame = tk.Frame(window)

# This is our Radiobuttons
int_var = tk.IntVar()
Int_radiobutton_1 = ttk.Radiobutton(radiobutton_frame, value = 1, variable = int_var, text = 'This is One')
Int_radiobutton_2 = ttk.Radiobutton(radiobutton_frame, value = 2, variable = int_var, text = 'This is Two')

output_label = ttk.Label(
    master=window,
    text='This is my Label',
    font=('Helvetica', 20, 'bold'),   # Font and size
    foreground='blue',                 # Text color
    justify='center'                   # Center align
)
output_label.pack(pady=20)

# Pack elements in frames ready to push onto form/window 
radiobutton_frame.pack()
Int_radiobutton_1.pack()
Int_radiobutton_2.pack()
output_label.pack(pady=20)

# run the program to generate window with all packed elements for user interaction 
window.mainloop()





