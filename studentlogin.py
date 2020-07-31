# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 00:09:17 2019

@author: sahil
"""

import tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='Page1.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#-------Title----------

frameT = tk.Frame(root, bg='white', bd=5)
frameT.place(relx=0.5, rely=0.65, relwidth=0.75, relheight=0.1, anchor='n')

label = tk.Label(frameT, text="Log in", font=80, bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)
#-------Email----------
frameE = tk.Frame(root, bg='white', bd=5)
frameE.place(relx=0.15, rely=0.25, relwidth=0.2, relheight=0.075, anchor='n')

label = tk.Label(frameE, text="Email : ", font=80, bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)


frameET = tk.Frame(root, bg='white', bd=5)
frameET.place(relx=0.3, rely=0.25, relwidth=0.6, relheight=0.075)

email = tk.Entry(frameET, font=80)
email.insert(0,'yourname@domain.com')
email.place(relwidth=1, relheight=1)

#-------Password----------
frameP = tk.Frame(root, bg='white', bd=5)
frameP.place(relx=0.15, rely=0.45, relwidth=0.2, relheight=0.075, anchor='n')

label = tk.Label(frameP, text="Password : ", font=80, bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)


framePT = tk.Frame(root, bg='white', bd=5)
framePT.place(relx=0.3, rely=0.45, relwidth=0.6, relheight=0.075)

password = tk.Entry(framePT, font=80,show="*")
password.place(relwidth=1, relheight=1)
root.mainloop()