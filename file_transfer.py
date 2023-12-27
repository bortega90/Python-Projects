import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
from datetime import timedelta

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of GUI window
        self.master.title("File Transfer")

        #creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source",width=20, command = self.source_Dir)
        #postitons source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0,column=0, padx=(20,10), pady=(30,0))

        #create entry for source directory selection
        self.sourceDir = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.sourceDir.grid(row=0,column=1, columnspan=2, padx=(20,10),pady=(30,0))
        
        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width =20, command = self.destDir)
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
    def source_Dir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the .delete(0, END) will clear the content that is inserted in the Entry Widget
        #this allows the path to be inserted into the Entry widget properly
        self.sourceDir.delete(0,END)
        #the .insert method will insert the user selection to the source_dir Entry
        self.sourceDir.insert(0, selectSourceDir)
        #creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
  

        #creates function to select destination
    def destDir(self):
        selectDestDir=tkinter.filedialog.askdirectory()
        #the .delete (0,END) will clear the content inserted in the Entry widget, this allows
        #the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0,END)
        #the .insert method will insert the user selection to the destination_dir Entry widget
        self.destination_dir.insert(0,selectDestDir)
        #create button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)

        #creates function to move files 
    def transferFiles(self):
        #gets source directory
        source=self.sourceDir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in the source directory
        source_files = os.listdir(source)
        #runs thru each file in the source directory
        for i in source_files:
            #this iterates thru the source directory?
            file_path = os.path.join(source,i)
            #this will subtract now time from mod time
            twentyfourHrs_ago = datetime.datetime.now() - timedelta(hours = 24)
            mod_time = os.path.getmtime(file_path)
            #linking filepath with time stamp
            date_time_file = datetime.datetime.fromtimestamp(mod_time)
            if date_time_file > twentyfourHrs_ago:
            #moves each file from source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')

    def exit_program(self):
        #root is the main GUI window, the Tkinter destroy method tells python to terminate
        #root.mainloop and all widgets insid GUI window
        root.destroy()





if __name__ =="__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
