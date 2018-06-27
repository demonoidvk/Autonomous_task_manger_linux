import db, openapk
from db import *    

db.dbcon()      #call to establish db connection
cn=db.dbcon()   #using the returned val of function in cn
cur=db.cursor   #cur= variable for cursor in this file

class users:
    #common class for users
    query=("use minor_users")       #db name
    cur.execute(query)    
    def userpart(username):
        query=("select name from users where username=%s")
        cur.execute(query,(username,))
        name=cur.fetchone()
        stmt="Welcome "+name[0]+", How may i help you?"
        print(stmt)
        openapk.exec_cmd()
        
        
        
