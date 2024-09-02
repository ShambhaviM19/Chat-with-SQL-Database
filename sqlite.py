import sqlite3

connection=sqlite3.connect("Student.db")
cursor=connection.cursor()

table_info="""
create table STUDENT(NAME VARCHAR(25),BRANCH VARCHAR(25),
MAILID VARCHAR(25),CGPA FLOAT)
"""
cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Shambhavi','IT','shambhavimishra328@gmail.com',8.83)''')
cursor.execute('''Insert Into STUDENT values('Pranav','CSE','pranavbhandari798@gmail.com',9.2)''')
cursor.execute('''Insert Into STUDENT values('Srinidhi','IT','sampathsrinidhi@gmail.com',8.0)''')
cursor.execute('''Insert Into STUDENT values('Aarav','ECE','aaravgupta123@gmail.com',8.75)''')
cursor.execute('''Insert Into STUDENT values('Meera','Mechanical','meerasharma456@gmail.com',8.5)''')
cursor.execute('''Insert Into STUDENT values('Rohan','EEE','rohanpatel789@gmail.com',8.95)''')
cursor.execute('''Insert Into STUDENT values('Neha','Civil','nehaverma234@gmail.com',8.1)''')
cursor.execute('''Insert Into STUDENT values('Kavya','CSE','kavyasharma567@gmail.com',9.0)''')
cursor.execute('''Insert Into STUDENT values('Ananya','IT','ananya.patel@gmail.com',8.65)''')
cursor.execute('''Insert Into STUDENT values('Vikram','Chemical','vikramkhanna789@gmail.com',8.3)''')
cursor.execute('''Insert Into STUDENT values('Ishaan','CSE','ishaansingh321@gmail.com',9.1)''')
cursor.execute('''Insert Into STUDENT values('Tara','Aerospace','tarachopra456@gmail.com',8.4)''')
cursor.execute('''Insert Into STUDENT values('Ritika','Biomedical','ritikamehta789@gmail.com',8.7)''')

print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)
connection.commit()
connection.close()

