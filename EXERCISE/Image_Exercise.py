import tkinter as tk
from winsound import *
from tkinter import PhotoImage

window = tk.Tk()
window.title("Image & Sound in Tkinter")

title_label = tk.Label(master = window, text = 'Image & Sound', font = 'Calibri 24 bold')
title_label.pack()

image2 = PhotoImage(file="grading_System.png")

image_label = tk.Label(window, image=image2)
image_label.pack()

image = PhotoImage(file="play-button.png")

play = lambda: PlaySound('lion_growl.wav', SND_FILENAME)

button = tk.Button(window, image=image, command = play)
button.pack(pady=20)

window.mainloop