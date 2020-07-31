# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:02:55 2019

@author: Manav
"""
import sqlite3
import tkinter as tk
from tkinter import messagebox

def set_data(name,dob,qualification,cgpa,email,password):
    try:
        conn = sqlite3.connect('jobs.db')
        conn.execute("INSERT INTO COMPANY(name,dob,qualification,cgpa,email,password,flag)\
                     VALUES (?,?,?,?,?,?,?)",(name,dob,qualification,cgpa,email,password,0));
        conn.commit()
    except sqlite3.IntegrityError:
        messagebox.showinfo("Error","Failed")
    else:
        messagebox.showinfo("Success","Entered Successfully!")
        root.destroy()

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
frameT.place(relx=0.5, rely=0.075, relwidth=0.75, relheight=0.1, anchor='n')

label = tk.Label(frameT, text="Sign Up Fast!!!", font=("Times","-25"), bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)

#-------Name----------

frameN = tk.Frame(root, bg='white', bd=5)
frameN.place(relx=0.15, rely=0.25, relwidth=0.2, relheight=0.075, anchor='n')

label = tk.Label(frameN, text="Name : ", font=("Times","-25"), bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)

frameNT = tk.Frame(root, bg='white', bd=5)
frameNT.place(relx=0.3, rely=0.25, relwidth=0.6, relheight=0.075)

name = tk.Entry(frameNT, font=80)
#Name.insert(0,'Bill Gates')
name.place(relwidth=1, relheight=1)

#-------DOB----------

frameD = tk.Frame(root, bg='white', bd=5)
frameD.place(relx=0.15, rely=0.35, relwidth=0.2, relheight=0.075, anchor='n')

label = tk.Label(frameD, text="D.O.B : ", font=("Times","-25"), bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)


frameDT = tk.Frame(root, bg='white', bd=5)
frameDT.place(relx=0.3, rely=0.35, relwidth=0.6, relheight=0.075)

dob = tk.Entry(frameDT, font=80)
#dob.insert(0,'DD/MM/YYYY')
dob.place(relwidth=1, relheight=1)

#-------Qualification----------

frameQ = tk.Frame(root, bg='white', bd=5)
frameQ.place(relx=0.15, rely=0.45, relwidth=0.2, relheight=0.075, anchor='n')

label = tk.Label(frameQ, text="Qualification : ", font=("Times","-18"), bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)


frameQT = tk.Frame(root, bg='white', bd=5)
frameQT.place(relx=0.3, rely=0.45, relwidth=0.6, relheight=0.075)

qualification = tk.Entry(frameQT, font=80)
#qualification.insert(0,'E.x, B.E.')
qualification.place(relwidth=1, relheight=1)

#-------CGPA----------
frameC = tk.Frame(root, bg='white', bd=5)
frameC.place(relx=0.15, rely=0.55, relwidth=0.2, relheight=0.075, anchor='n')

label = tk.Label(frameC, text="C.G.P.A : ", font=("Times","-25"), bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)


frameCT = tk.Frame(root, bg='white', bd=5)
frameCT.place(relx=0.3, rely=0.55, relwidth=0.6, relheight=0.075)

cgpa = tk.Entry(frameCT, font=80)
#cgpa.insert(0,'E.x, 9.14')
cgpa.place(relwidth=1, relheight=1)


#-------Email----------
frameE = tk.Frame(root, bg='white', bd=5)
frameE.place(relx=0.15, rely=0.65, relwidth=0.2, relheight=0.075, anchor='n')

label = tk.Label(frameE, text="Email : ", font=("Times","-25"), bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)


frameET = tk.Frame(root, bg='white', bd=5)
frameET.place(relx=0.3, rely=0.65, relwidth=0.6, relheight=0.075)

email = tk.Entry(frameET, font=80)
#email.insert(0,'yourname@domain.com')
email.place(relwidth=1, relheight=1)

#-------Password----------
frameP = tk.Frame(root, bg='white', bd=5)
frameP.place(relx=0.15, rely=0.75, relwidth=0.2, relheight=0.075, anchor='n')

label = tk.Label(frameP, text="Password : ", font=("Times","-20"), bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)


framePT = tk.Frame(root, bg='white', bd=5)
framePT.place(relx=0.3, rely=0.75, relwidth=0.6, relheight=0.075)

password = tk.Entry(framePT, font=80,show="*")
password.place(relwidth=1, relheight=1)

#-------Submit----------
frameB = tk.Frame(root, bg='white', bd=5)
frameB.place(relx=0.75, rely=0.85, relwidth=0.3, relheight=0.1, anchor='n')

button = tk.Button(frameB, text="Submit", font=("Times","-25"),bg = "#593d25",fg = "White",activebackground="#b79374",command=lambda: set_data(name.get(),dob.get(),qualification.get(),cgpa.get(),email.get(),password.get()))
button.place(relheight=1, relwidth=1)

root.mainloop()
