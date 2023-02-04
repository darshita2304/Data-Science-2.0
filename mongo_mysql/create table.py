import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)

cur = mydb.cursor()

#cur.execute("create database new_db")

cur.execute("use new_db")

cur.execute("create table students (studid int,firstname varchar(40), class int, mail_id varchar(50))")

mydb.commit()