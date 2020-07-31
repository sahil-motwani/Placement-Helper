
#---------------------start-------------------
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 00:13:47 2019

@author: Manav
"""
from tkinter import *
from tkinter import ttk
import tkinter as tk
import sqlite3
import smtplib
from email.mime.text import MIMEText
from tkinter import messagebox
from scroll import ScrollableFrame
def sendmail(cgpa):
    conn = sqlite3.connect('jobs.db')
    
    cursor = conn.execute("SELECT name,email,cgpa from COMPANY ORDER BY cgpa");
    cursor=list(cursor)
    
    for row in cursor:
        if row[2]>=cgpa:
            body="You have to come at VESIT on date 10 April 2019 in Room No. 303"

            msg=MIMEText(body)
            
            fromaddr="lasytu@gmail.com"
            
            toaddr=row[1]
            
            
            msg['From']=fromaddr
            msg['To']=toaddr
            msg['subject']=f"Congo {row[0]} you are selected for interview!!!"
            
            
            server=smtplib.SMTP('smtp.gmail.com',587)
            
            server.starttls()
            
            server.login(fromaddr,"papamareto")
            
            server.send_message(msg)
            print('Mail sent....')
    
            server.quit()
            
        else:
           continue
    conn.close()
    
    messagebox.showinfo("Success","Conformation sent Successfully!")
    root.destroy()
def fetch(cgpa):
    conn = sqlite3.connect('jobs.db')
    
    cursor = conn.execute("SELECT name,cgpa from COMPANY ORDER BY cgpa desc");
    cursor=list(cursor)
    '''frameT = tk.Frame(root, bg='white', bd=5)
    frameT.place(relx=0.125, rely=0.32, relwidth=0.5, relheight=0.1)
            
    label = tk.Label(frameT, text='Name', font=("Times","-30"), bg = "#593d25", fg = "White")
    label.place(relwidth=1, relheight=1)
    
    frameT = tk.Frame(root, bg='white', bd=5)
    frameT.place(relx=0.64, rely=0.32, relwidth=0.25, relheight=0.1)
            
    label = tk.Label(frameT, text='C.G.P.A', font=("Times","-30"), bg = "#593d25", fg = "White", bd=5)
    label.place(relwidth=1, relheight=1)'''
    r=Frame(root)
    r.place(relx=0.1, rely=0.32)
    frame = ScrollableFrame(r)
    label = tk.Label(r, text='Name       -        cgpa', font=("Times","-30"), bg = "black", fg = "White")
    label.pack(fill=X)
    for row in cursor:
        if row[1]>=cgpa:
            #-----------name--------
            frameT = tk.Frame(frame.scrollable_frame, bd=5)
            frameT.pack(fill=X)
            
            label1 = tk.Label(frameT, text=row[0], font=("Times","-30"), bg = "#593d25", fg = "White")
            label1.pack(side=LEFT,padx=20)
            #----------cgpa-----------

            label2 = tk.Label(frameT, text=row[1], font=("Times","-30"), bg = "#593d25", fg = "White")
            label2.pack(side=RIGHT,padx=40)
            
        else:
            continue
    frame.pack()
    frameB = tk.Frame(root, bg='white', bd=5)
    frameB.place(relx=0.75, rely=0.9, relwidth=0.25, relheight=0.07, anchor='n')
    
    button = tk.Button(frameB, text="Send Conformation", font=("Times","-25"),bg = "#593d25",fg = "White",activebackground="#b79374",command=lambda: sendmail(float(cgpa)))
    button.place(relheight=1, relwidth=1)
    
    
    conn.close()
    
HEIGHT = 580
WIDTH = 1000

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='Page1.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

#-------Title----------

frameT = tk.Frame(root, bg='white', bd=5)
frameT.place(relx=0.5, rely=0.075, relwidth=0.85, relheight=0.1, anchor='n')

label = tk.Label(frameT, text="Admin Page", font=("Times","-30"), bg = "#593d25", fg = "White")
label.place(relwidth=1, relheight=1)

#--------Text------
frameCT = tk.Frame(root, bg='white', bd=5)
frameCT.place(relx=0.13, rely=0.2, relwidth=0.4, relheight=0.075)

cgpa = tk.Entry(frameCT, font=("Times","-25"))
cgpa.place(relwidth=1, relheight=1)

#--------Search-------
frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.57, rely=0.2, relwidth=0.3, relheight=0.075)

button = tk.Button(frame, text="Search", font=("Times","-25"),bg = "#593d25",fg = "White",activebackground="#b79374",command =lambda: fetch(float(cgpa.get())))
button.place(relheight=1, relwidth=1)

root.mainloop()

