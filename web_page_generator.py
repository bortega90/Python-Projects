import tkinter as tk
from tkinter import *
from tkinter import ttk
import webbrowser





class ParentWindow(Frame):
    def __init__(self,master):
        #creating the window to popup
        Frame.__init__(self,master)
        #creating the title of the window
        self.master.title("Web Page Generator")
        #create label
        
        #creating a button called DEFAULT HTML PAGE
        self.defaultHTML_btn=Button(text="Default HTML Page",width=20, command=self.defaultHTML)
        #placing the button in the frame
        self.defaultHTML_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15))
        #create button called 'submit custom text'
        self.submitTxt_btn=Button(text='Submit Custom Text',width=20, command=self.submitText)
        #placing the button in the frame
        self.submitTxt_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))
        

        #create Entry for Default HTML page button
        self.lbl_text = tk.Label(self.master,text="Enter Custom text: ")
        self.lbl_text.grid(row=0, column=1, padx=(10,40),pady=(0,15))
        self.submitWords = Entry(width=75)
        #positions entry in GUI using tkinter grid() padx and pady are the same as
        #the button to ensure they will line up
        self.submitWords.grid(row=1,column=1, columnspan=2, padx=(20,10),pady=(30,10))
       



    #adding function to the Default HTML Page button
    def defaultHTML(self):
        htmlText = "Stay tuned for our amazing summer news!"
        htmlFile = open('index.html','w')
        htmlContent = '<html>\n<body>\n<h1>' + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab('index.html')
    #adding function to the Submit Custom Text button
    def submitText(self):
        submitWords = ""
        htmlFile = open('index.html','w')
        submitContent = '<html>\n<body>\n<h1>' + submitWords + '</h1>\n</body>\n</html>'
        submitWords.config(text=submitWords.get(), font=('Helvetica 13'))
        htmlFile.write(submitContent)
        htmlFile.close()
        webbrowser.open_new_tab('index.html')
        

        
       
     



       














if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
