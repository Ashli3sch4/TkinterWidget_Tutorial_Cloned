import tkinter as tk 
from tkinter import ttk 

root = tk.Tk()


root.title("Tkinter Treeview")

treeview = ttk.Treeview(columns=("Salary", "Bonus"))

treeview.heading("#0", text="Emplyee")
treeview.heading("Salary", text= "Salary")
treeview.heading("Bonus", text="Bonus")


icon_city = tk.PhotoImage(file="./assets/city.png")
icon_male = tk.PhotoImage(file="./assets/male.png")
icon_female = tk.PhotoImage(file="./assets/female.png")


level1 = treeview.insert("", tk.END, text="San Jose")
treeview.insert(level1, tk.END, text="John Doe", values=(f"${100000: ,}",f"${8000: ,}"), image=icon_male)
treeview.insert(level1, tk.END, text="Jane Doe", values=(f"${120000: ,}",f"${9000: ,}"), image=icon_female)

treeview.pack(fill=tk.BOTH, expand=True padx=10, pady=10)

root.mainloop()