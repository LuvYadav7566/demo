import mysql.connector

mydb=mysql.connector.connect(
host="localhost",user="root",passwd="Mysql1@1234",database="DEMODB",use_pure=True
)

print(mydb)
cursor=mydb.cursor()
cursor.execute("CREATE TABLE STUDENT (NAME VARCHAR(255),ID INT);")