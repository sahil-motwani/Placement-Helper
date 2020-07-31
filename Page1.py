# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 14:21:29 2019

@author: Manav
"""
import os
import tkinter as tk

def applicant():
    root.destroy()
    os.system('python Page2.py')
def job_provider():
    root.destroy()
    os.system('python Admin.py')    

HEIGHT = 580
WIDTH = 1000

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='Page1.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Get Hired!", font=("Times","-35"),bg = "#593d25",fg = "White",activebackground="#b79374", command= applicant)
button.place(relheight=1, relwidth=1)

lower_frame = tk.Frame(root, bg='white', bd=5)
lower_frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(lower_frame, text="Want to Hire!", font=("Times","-35"),bg = "#593d25",fg = "White",activebackground="#b79374", command = job_provider)
button.place(relheight=1, relwidth=1)

root.mainloop()



