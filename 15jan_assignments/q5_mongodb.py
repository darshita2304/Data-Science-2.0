## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q5: create a calss to implement isnert, update and delete in mongodb

import pymongo
import logging
logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")

class q5_mongodb:
    
    def __init__(self, conn_str):
        logging.info("this is mongodb connection intitial fn")
        try:
            self.client = pymongo.MongoClient(conn_str)
            logging.info("mongodb connection sucessful")

            #selecting/creating db
            self.database = self.client['mynew_db']
            logging.info("mynew_db is in use...")

        except Exception as e:
            logging.error("there is some issue with conncetion with mongodb")
            logging.error(e)

    def insert_data(self, tbl_name, json_data):
        logging.info("this is insert operation")
        try:
            collection = self.database[tbl_name]
            collection.insert_many(json_data)
            logging.info("record inserted sucessfully..")

        except Exception as e:
            logging.error("there is some issue with inserting data in mongodb....")
            logging.error(e)       
    
    # def update_data(self, query):
    #     logging.info("this is update operation")
    #     try:
    #         self.cur.execute(query)
    #         self.conn.commit()
    #         logging.info("record updated sucessfully..")

    #     except Exception as e:
    #         logging.error("there is some issue with updating data in mysql")
    #         logging.error(e)
    #         self.conn.rollback()
    #     # finally:
    #     #     self.conn.close()
    

    # def delete_data(self, query):
    #     logging.info("this is update operation")
    #     try:
    #         self.cur.execute(query)
    #         self.conn.commit()
    #         logging.info("record updated sucessfully..")

    #     except Exception as e:
    #         logging.error("there is some issue with updating data in mysql")
    #         logging.error(e)
    #         self.conn.rollback()
    #     # finally:
    #     #     self.conn.close()
    
obj = q5_mongodb("mongodb+srv://darshita:hello1@cluster0.b1kek.mongodb.net/?retryWrites=true&w=majority")

json_data = [{"class name " : "javascript 2.0 " ,
        "topic name " : "react js ",
        "todays date ": "8th jan 2023"
},{"class name " : "PHP " ,
        "topic name " : "MYSQL ",
        "todays date ": "9th jan 2023"
},{"class name " : "Flex programming " ,
        "topic name " : "SQL server ",
        "todays date ": "10th jan 2023"
}]
obj.insert_data("q5_mongodb", json_data)



