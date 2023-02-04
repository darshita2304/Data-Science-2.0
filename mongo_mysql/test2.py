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

cur.execute("select *from new_db.tb1")

for i in cur:
    print(i)
    
