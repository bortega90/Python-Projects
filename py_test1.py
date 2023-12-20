import sqlite3

#list of file names needed for database
fileList = ('information.docx', 'Hello.txt', 'myImage.png',\
            'mymovie.png', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#creating data base named 'py_test.db' saved as conn
conn = sqlite3.connect('py_test.db')
#adding info in database by opening the datebase file
with conn:
    cur = conn.cursor()
    #use SQL in python to add table with two 2 required fields (auto-increment int and data type 'string')
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_list( \
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fList STRING \
                )")  
    #inputting data in fileList to table 'tbl_list'
    for file in fileList:
        if file.endswith('txt'):
            #adding fileList into table
            cur.execute("INSERT INTO tbl_list(col_fList) VALUES(?)", (file,)) 
            print(file)
    conn.commit()
conn.close()



    
