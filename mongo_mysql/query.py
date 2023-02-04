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


#cur.execute("update new_db.students set firstname='darshita' where studid=1")

#cur.execute("delete from new_db.students where studid=7 ")

#cur.execute("select min(studid) from new_db.students")

#cur.execute("select max(studid) from new_db.students")

cur.execute("select * from new_db.students")
for i in cur:
    print (i)

#cur.execute("drop table newdb.students")

cur.execute("select count(*),firstname from new_db.students group by firstname")
#cur.execute("select *from new_db.students")

for i in cur:
    print (i)
    
mydb.commit()