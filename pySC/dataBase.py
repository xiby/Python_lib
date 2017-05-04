import sqlite3
import os

class libdb:

    def __init__(self):
        print("calling _init_")
        dirlist=list()
        dirlist=os.listdir("../")
        if "myLib.db" not in dirlist:
            print("未创建数据库")
            self.__db=sqlite3.connect("../myLib.db")           #connect to database
            self.__db.execute("create table catalog (name varchar(50) ,publicher varchar(80),addYear integer,addMonth integer,addDay integer,state integer,primary key(name,publicher))")
            self.Cursor=self.__db.cursor()
            self.bookNum=0
            print("刚刚创建了数据库")
        else:
            self.__db=sqlite3.connect("../myLib.db")           #connect to database
            self.Cursor=self.__db.cursor()
    def getDB(self):                                    #get the database
        return self.__db

    def initCursor(self):                               #init the cursor
        cursor=self.__db.cursor()

    def getCursor(self):                                #get the cursor for query
        return self.Cursor

    def getNum(self):                                       #get the numbers of my books                             
        return self.bookNum

    def insert(self,book):                              #insert a book to my library
        try:
            self.__db.execute("insert into catalog values (?,?,?,?,?,?)",book)
            self.__db.commit()
            return 'insert success'
        except sqlite3.IntegrityError as e:
            print(book,end=" ")
            return "该记录已经存在，若要更新，请选择更新选项"

    def search(self):                                   #search all books
        self.Cursor.execute("select * from catalog")
        return self.Cursor.fetchall()

    def searchByName(self,bookName):
        sql="select * from catalog WHERE name= "+"'"+bookName+"'"
        self.Cursor.execute(sql)
        return self.Cursor.fetchall()

    def searchByPub(self,publisher):
        sql="select * from catalog WHERE publicher= "+"'"+publisher+"'"
        self.Cursor.execute(sql)
        return self.Cursor.fetchall()

    def update(self,tmpbook):
        pass
