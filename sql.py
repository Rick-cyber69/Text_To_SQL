import sqlite3

# connect to sqlite
Connection=sqlite3.connect("student.db")

# create a cursor object to insert record,create table,retrive
cursor=Connection.cursor()

# create the table
table_info="""
Create table STUDENT(NAME VARCGHAR(20), CLASS VARCHAR(20), SECTION VARCHAR(10), MARKS INT);
"""

cursor.execute(table_info)

# insert some more records

cursor.execute('''Insert into STUDENT values('Sandipan', 'Data Science', 'A', 90)''')
cursor.execute('''Insert into STUDENT values('Aniket', 'Data Science', 'B', 100)''')
cursor.execute('''Insert into STUDENT values('Subhojit', 'Data Science', 'A', 86)''')
cursor.execute('''Insert into STUDENT values('Arpan', 'DEVOPS', 'A', 50)''')
cursor.execute('''Insert into STUDENT values('Indradeep', 'DEVOPS', 'A', 35)''')

# display all the records 
print("The inserted records are :")

data=cursor.execute('''select * from STUDENT''')

for row in data:
    print(row)

# close the connection
Connection.commit()
Connection.close()
