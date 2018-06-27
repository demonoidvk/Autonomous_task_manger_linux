#This would be only to work on front end of the program
import getpass,os
import db,man,users             #importing supporting files 
from db import dbcon              #connection to the database

import openapk                  #open and terminating apks 

def checkuser():
    # get username
    uname=input("Enter username: ")
    query=("use minorusers_test")       #db name
    cur.execute(query)
    # print(cur.fetchall())
    query=("select username from users where username=%s")
    cur.execute(query,(uname,))
    if cur.fetchone() is not None:
        for i in range(3):
            password=input("Enter password:")
            query=("select password from users where username=%s AND password=%s")
            cur.execute(query,(uname,password))
            if cur.fetchone() is not None:
                os.system("clear")
                users.users.userpart(uname)
                break
            else:
                print("\nWrong Password! Input again:")
                continue            
            
    else:
        print("Username does not EXISTS!")
        ask=input("Do you wnat to register?(Yes/NO):")
        ask=ask.lower()
        if ask=="yes":
            username=input("Enter Username again:")
            password=input("Enter the password again:")
            name=input("Enter your full name: ")
            query=("insert into users values(%s,%s,%s)")
            cur.execute(query,(username,password,name))
            cn.commit()
            checkuser()
        else:
            print("\n\nSee you next time, bye!")
            exit
            
db.dbcon()      #call to establish db connection
cn=db.dbcon()   #database connection element
cur=db.cursor   #cur= variable for cursor in this file
cur.execute("Select version()") #if executed properly will show the version of MySql
result=cur.fetchone()
if result:
    checkuser()
else:
    print("Connection to DB failed!")





