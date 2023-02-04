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

#cur.execute("create table tb1 (name varchar(40), roll_no int, mail_id varchar(50))")

cur.execute("insert into tb1 values ('darshi', 34, 'abc@gmail.com')")

mydb.commit()