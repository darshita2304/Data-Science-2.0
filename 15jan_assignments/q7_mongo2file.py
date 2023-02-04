## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q7: create a class to import data into file from mongodb

import pymongo
import logging
logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")

class q7_mongo2file:
    
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

    def fetch_write_data(self, tbl_name, filename):
        try:
            logging.info("this is a fetch_write_data function")
            collection = self.database[tbl_name]
            cursor = collection.find({})            
            have_list = True if len(list(cursor)) else False;

            if have_list: # if table is empty...
                logging.info("collection has records..")

                fo = open(filename, "a")
                logging.info("file opened sucessfully...")

                for doc in collection.find({}):
                    fo.write(str(doc))
                
                fo.close()
                logging.info("records written sucessfully....")

            else:
                print("no records found.... empty table..")                
                    
        except Exception as e:
            logging.error("there is some issue with fetch_write_data fn")
            logging.error(e)

        
obj = q7_mongo2file("mongodb+srv://darshita:hello1@cluster0.b1kek.mongodb.net/?retryWrites=true&w=majority")
obj.fetch_write_data("q5_mongodb", "mongo.txt")

