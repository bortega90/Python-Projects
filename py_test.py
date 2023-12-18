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
    conn.commit()



with conn:
    def list_entry():
        for file in fileList:
            #adding fileList into table
            cur.execute("INSERT fileList INTO tbl_list() VALUES(?)", (file))
        conn.commit()


list_entry() #call function


     
conn = sqlite3.connect('py_test.db')


with conn:
    cur = conn. cursor()
    cur.execute("SELECT * FROM tbl_list = 'txt'")
    varFile = cur.fetchall()
    for file in varFile:
        print(file)

conn.close()
    
