import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb.is_connected())
cur = mydb.cursor()
cur.execute("show databases")

for i in cur:
    print(i)

