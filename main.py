import sqlite3

con=sqlite3.connect('mycompany.db')
cObj=con.cursor()

cObj.execute("INSERT into employees VALUES(1,'Rachit',100000,'python', 'senior analyst')")
con.commit()

cObj.close()
con.close()
