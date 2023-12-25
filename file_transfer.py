import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import stat
import time
import shutil
import datetime
from datetime import timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of GUI window
        self.master.title("File Transfer")

        #creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source",width=20)
        #postitons source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0,column=0, padx=(20,10), pady=(30,0))

        #create entry for source directory selection
        self.sourceDir = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.sourceDir.grid(row=0,column=1, columnspan=2, padx=(20,10),pady=(30,0))
        
        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width =20)
        #postions destination buttons in GUI using tkinter grid() on the next row
        #under the source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))
        
        #creates entry for destination directory selection
        self.destination_dir=Entry(width=75)
        #postitions entry in GUI using tkinter grid() padx and pady are the same as the
        #button to ensure they will line up
        self.destination_dir.grid(row=1,column=1,columnspan=2, padx=(20,10), pady=(15,10))
 


        #creates button to transfer files
        self.transfer_btn=Button(text="Transfer Files", width = 20, command=self.transferFiles)
        #positions transfer files button
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))
        #creates exit button
        self.exit_btn=Button(text="Exit", width=20, command=self.exit_program)
        #positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,40),pady=(0,15))
        
       

        #creates function to select source Directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delet(0, END) will clear the content that is inserted in the Entry Widget
        #this allows the pasth to be inserted into the Entry widget properly
        self.source_dir.delete(0,END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)
        #creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
  

        
    def destDir(self):
        selectDestDir=tkinter.filedialog.askdirectory()
        #the .delete (0,END) will clear the content inserted in the Entry widget, this allows
        #the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0,END)
        #the .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0,selectDestDir)
        #create button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)

        
    def transferFiles(self):
        #gets source directory
        source=self.sourceDir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs thru each file in the source directory
        for i in source_files:
            #moves each file from source to the destination
            shutil.move(source + '/' + i, destination)
            print(i + ' was successfully transferred.')
     

    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method tells python to terminate
        #root.mainloop and all widgets insid GUI window
        root.destroy()

#get the file path
filepath = r"C:\Users\britn\OneDrive\Desktop\Customer Destination\Nu_txt_doc1.txt"
#getting time when it was last modified via the file path
last_access_time=os.path.getmtime(filepath)
#converting time to years month days hours/mins/secs local time
fileTime=time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime(last_access_time))
print('{} last modified time on: {}'.format(filepath, fileTime))


filepath = r"C:\Users\britn\OneDrive\Desktop\Customer Destination\Nu_txt_doc2.txt"
last_access_time=os.path.getmtime(filepath)
fileTime=time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime(last_access_time))
print('{} last modified time on: {}'.format(filepath, fileTime))


filepath = r"C:\Users\britn\OneDrive\Desktop\Customer Destination\Nu_txt_doc3.txt"
last_access_time=os.path.getmtime(filepath)
fileTime=time.strftime('%Y-%m-%d/%H:%M:%S', time.localtime(last_access_time))
print('{} last modified time on: {}'.format(filepath, fileTime))





if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
