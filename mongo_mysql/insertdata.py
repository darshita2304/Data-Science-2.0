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

cur.execute("insert into students values (3,'darshi', 34, 'abc@gmail.com')")
cur.execute("insert into students values (2,'hello', 9, 'sd@gmail.com')")

cur.execute("insert into students values (4,'darshi', 4, 'asdf@gmail.com')")

cur.execute("insert into students values (5,'darshi', 5, 'abfghc@gmail.com')")

cur.execute("insert into students values (6,'darshi', 7, 'cxvb@gmail.com')")

cur.execute("insert into students values (7,'darshi', 8, 'zdf@gmail.com')")

mydb.commit()