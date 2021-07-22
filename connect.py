import mysql.connector
mydb=mysql.connector.connect(
host='localhost',
user ='root',
password ='infinity24',
database ='newdatabase')
print(mydb.connection_id)
cur=mydb.cursor()
s="INSERT INTO STUDENTS(ROLL_NO,FIRST_NAME,MARKS) VALUES(%s%s%s)"
b1=(10,'vishal',80)
cur.execute()
mydb.commit()

