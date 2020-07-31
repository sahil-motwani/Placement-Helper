# -*- coding: utf-8 -*-
'''
Created on Thu Mar 21 20:17:34 2019

@author: Manav

'''
import sqlite3

conn = sqlite3.connect('jobs.db')


conn.execute('''CREATE TABLE COMPANY
         (name           TEXT    NOT NULL,
         dob             TEXT    NOT NULL,
         qualification   TEXT    NOT NULL,
         cgpa            FLOAT,
         email           VARCHAR(20) PRIMARY KEY,
         password        TEXT    NOT NULL,
         flag            INT);''')
print ("Table created successfully")


conn.execute("INSERT INTO COMPANY (name,dob,qualification,cgpa,email,password) \
      VALUES ('Manav Motwani','10/09/1999','B.E.', 9.15,'2017.manav.motwani@ves.ac.in','Manav@123' )");

conn.commit()
print ("Records created successfully")
conn.close()
'''

import smtplib
from email.mime.text import MIMEText

body="You have to come at VESIT on date 10 April 2019 in Room No. 303"

msg=MIMEText(body)

fromaddr="manav0090m@gmail.com"

toaddr="2017.manav.motwani@ves.ac.in"


msg['From']=fromaddr
msg['To']=toaddr
msg['subject']="Congo you are selected for interview!!!"


server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

server.login(fromaddr,"Mot@12345")

server.send_message(msg)
print('Mail sent....')

server.quit()'''
