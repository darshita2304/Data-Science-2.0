## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q4: create a class to implement all insert, update,delete for mysql

import mysql.connector
import logging
logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")

class q4_mysql:
    
    def __init__(self, host, username, password, ):
        logging.info("this is connection intitial fn")
        try:
            self.conn =  mysql.connector.connect(host=host, user=username,password=password)
            self.cur = self.conn.cursor()
            logging.info("connection sucessful")

            #self.cur.execute("create database studentsdb")
            self.cur.execute("use studentsdb")
            logging.info("students db is in use...")

        except Exception as e:
            logging.error("there is some issue with conncetion with mysql")
            logging.error(e)

    def insert_data(self, query):
        logging.info("this is insert operation")
        try:
            self.cur.execute(query)
            self.conn.commit()
            logging.info("record inserted sucessfully..")

        except Exception as e:
            logging.error("there is some issue with inserting data in mysql")
            logging.error(e)
            self.conn.rollback()
        # finally:
        #     self.conn.close()
    
    def update_data(self, query):
        logging.info("this is update operation")
        try:
            self.cur.execute(query)
            self.conn.commit()
            logging.info("record updated sucessfully..")

        except Exception as e:
            logging.error("there is some issue with updating data in mysql")
            logging.error(e)
            self.conn.rollback()
        # finally:
        #     self.conn.close()
    

    def delete_data(self, query):
        logging.info("this is update operation")
        try:
            self.cur.execute(query)
            self.conn.commit()
            logging.info("record updated sucessfully..")

        except Exception as e:
            logging.error("there is some issue with updating data in mysql")
            logging.error(e)
            self.conn.rollback()
        # finally:
        #     self.conn.close()
    
obj = q4_mysql("localhost",'abc','password')

#query = "create table tbl_students (name varchar(40), roll_no int, mail_id varchar(50))"

insert_query = "insert into tbl_students values ('shinu', 3, 'abc@gmail.com')"
obj.insert_data(insert_query)


update_query = "update tbl_students set name='darshita paghadal' where roll_no=3"
obj.update_data(update_query)

delete_query = "delete from tbl_students where roll_no=34"
obj.delete_data(delete_query)



