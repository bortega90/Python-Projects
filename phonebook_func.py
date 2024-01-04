import os
from tkinter import *
import tkinter as tk
import sqlite3

#adding other file to call on information
import phonebook_main
import phonebook_gui




def center_window(self,w,h): #pass in the tkinter frame(master) reference and the w and h
    #get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.hinfo_screenheight()
    #calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo + self.master.geometery('{}x{}+{}+{}'.format(w,h,y))
    return centerGeo

#catch if the user's clicks on the windows upper-right 'x' to ensure they want to close
def ask_quit(self):
    if messagebox.askokcancel('Exit program', 'Okay to exit application'):
        #this closes app
        self.master.destroy()
        os._exit(0)




#=======================================================================================
def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            ):')
        # you must commit changes using commit() to save table into database for sqlite3
       conn.commit()
    conn.close()
