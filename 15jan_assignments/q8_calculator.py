## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q8: create a class to a calculator functionalities add, sub,mul,div, log, exponenet, power

import logging
import math

logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")


class q8_calculator:
    
    def addition(self, list_arg):

        logging.info("this is start of addition fn")
        try:
            logging.info("inside try block of addition fn")
            
            sum = 0
            for i in list_arg:
                sum = sum + i
            
            print(f"addition of list is {str(sum)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with addition fn")
            logging.error(e)

    def subtraction(self, no1, no2):
        no1 = int(no1)
        no2 = int(no2)
        logging.info("this is start of subtraction fn")
        try:
            logging.info("inside try block of subtraction fn")
            
            if no1>no2:
                ans = no1-no2
            else:
                print("Given number 1 is grater than 2")
                return
            
            print(f"subtraction of {no1} and {no2} is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with subtraction fn")
            logging.error(e)

    def multipy(self, list_arg):
        logging.info("this is start of multipy fn")
        try:
            logging.info("inside try block of multipy fn")
            
            ans = 1
            for i in list_arg:
                ans = ans * i
            
            print(f"multipy of given number is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with multipy fn")
            logging.error(e)

    def division(self, no1, no2):
        no1 = int(no1)
        no2 = int(no2)
        logging.info("this is start of division fn")
        try:
            logging.info("inside try block of division fn")
            
            if no1>no2:
                ans = no1/no2
            else:
                print("Given number 1 is grater than 2")
                return
            
            print(f"division of {no1} and {no2} is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with division fn")
            logging.error(e)
    
    def log(self, no1):
        no1 = float(no1)
        
        logging.info("this is start of logarithm fn")
        try:
            logging.info("inside try block of logarithm fn")
                     
            ans = math.log(no1)            
            print(f"log of {no1} is {ans}")
            return
            
            print(f"division of {no1} and {no2} is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with .logarithm fn")
            logging.error(e)
          

obj = q8_calculator()

obj.addition([1,2,3,4])
obj.subtraction(45, 5)
obj.multipy([1,2,3,4])
obj.division(45, 5)
obj.log(100.12)





   
            











logging.basicConfig(filename='record_from_mongo.log', level=logging.DEBUG , filemode='w', format="%(asctime)s %(levelname)s %(message)s")

class Import_from_Mongo():
    
    def __init__(self, clienturl, filename):
        self.clienturl = clienturl
        self.filename = filename
        try:
            self.client = pymongo.MongoClient(self.clienturl)
        except Exception as e:
            print("Connection not established", e)
            logging.error("Connection not established", e)
        else:
            print("Connection to MongoDB is successful")
            logging.info("Connection to MongoDB is successful")
            
    def connect_to_collection(self, db_name, collection_name):
        try:
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]
        except Exception as e:
            print("Connection not established", e)
            logging.error("Connection not established", e)
        else:
            print("Connection to collection is successful")
            logging.info("Connection to collection is successful")
    
    def importing_record(self):
        try:
            record = []
            for i in self.collection.find():
                    record.append(i)
            with open(self.filename, 'a') as f:
                f.write(str(record))
        except Exception as e:
            print("Importing unsuccessful", e)
            logging.error("Importing unsuccessfull", e)
        else:
            print("Importing successful")
            logging.info("Importing successfull")
            
    def show_data(self):
        try:
            with open(self.filename, 'r') as f:
                record = f.read()
                print(record)
                logging.info("Reading operation is successful")
        except Exception as e:
            print("There is some error", e)
            logging.error("There is some error", e)
                
                
                
                
                
 ## Q8: create a class to a calculator functionalities add, sub,mul,div, log, exponenet, power

import logging
import math

logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")


class q8_calculator:
    
    def addition(self, list_arg):

        logging.info("this is start of addition fn")
        try:
            logging.info("inside try block of addition fn")
            
            sum = 0
            for i in list_arg:
                sum = sum + i
            
            print(f"addition of list is {str(sum)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with addition fn")
            logging.error(e)

    def subtraction(self, no1, no2):
        no1 = int(no1)
        no2 = int(no2)
        logging.info("this is start of subtraction fn")
        try:
            logging.info("inside try block of subtraction fn")
            
            if no1>no2:
                ans = no1-no2
            else:
                print("Given number 1 is grater than 2")
                return
            
            print(f"subtraction of {no1} and {no2} is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with subtraction fn")
            logging.error(e)

    def multipy(self, list_arg):
        logging.info("this is start of multipy fn")
        try:
            logging.info("inside try block of multipy fn")
            
            ans = 1
            for i in list_arg:
                ans = ans * i
            
            print(f"multipy of given number is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with multipy fn")
            logging.error(e)

    def division(self, no1, no2):
        no1 = int(no1)
        no2 = int(no2)
        logging.info("this is start of division fn")
        try:
            logging.info("inside try block of division fn")
            
            if no1>no2:
                ans = no1/no2
            else:
                print("Given number 1 is grater than 2")
                return
            
            print(f"division of {no1} and {no2} is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with division fn")
            logging.error(e)
    
    def log(self, no1):
        no1 = float(no1)
        
        logging.info("this is start of logarithm fn")
        try:
            logging.info("inside try block of logarithm fn")
                     
            ans = math.log(no1)            
            print(f"log of {no1} is {ans}")
            return
            
            print(f"division of {no1} and {no2} is {str(ans)}")
        except Exception as e:
            #print(e)
            logging.error("there is some issue with .logarithm fn")
            logging.error(e)
          

obj = q8_calculator()

obj.addition([1,2,3,4])
obj.subtraction(45, 5)
obj.multipy([1,2,3,4])
obj.division(45, 5)
obj.log(100.12)




import time
import tracemalloc

class Complexity:
    def __init__(self):
        pass
    
    @staticmethod
    def time_complexity(fn, *args):
        start_time = time.time()
        fn(*args)
        end_time = time.time()
        return end_time - start_time
    
    
    def space_complexity(self , fn , *args):
        tracemalloc.start()
        fn(*args)
        current, peak =  tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        return current, peak
        
        
        
        
        
        
        
        
        
        
        
        
        
 import logging
import mysql.connector as conn

import csv

logging.basicConfig(filename="sql_bulk_upload.log", level=logging.DEBUG, filemode='w', format = "%(asctime)s %(levelname)s %(message)s")

class MySQL_Bulk_Upload():
    
    def __init__(self, host, user, password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
    def create_connection(self):
        try:
            mydb = conn.connect(host = self.host, user = self.user, passwd = self.password, database = self.database)
            cursor = mydb.cursor()
            self.mydb = mydb
            self.cursor = cursor
            logging.info("Connection to DB successful")
            print("Connection to DB successful")
        except Exception as e:
            logging.error("Exception occurred", e)
        
        
    def create_table(self, table_name, columns):
        try:
            self.table_name = table_name
            self.columns = columns
            self.cursor.execute(f"CREATE TABLE if not exists {self.table_name}({self.columns})")
            self.mydb.commit()
            logging.info("table has created")
            print("Table has created")
        except Exception as e:
            logging.error("Exception occurred", e)
        
    def insert_data(self,csv_file):
        try:
            with open(csv_file, "r") as f:
                data  = csv.reader(f, delimiter = '\n')
                next(data)
                for i in data:
                    self.cursor.execute(f'insert into {self.database}.{self.table_name} values({str(i[0])})')
            self.mydb.commit()
            logging.info("Bulk Upload is successful")
        
        except Exception as e:
            print(e)
            logging.error("Exception occurred",e)
                   
        
    def show_data(self):
        try:
            self.cursor.execute(f"SELECT * from {self.table_name}")
            logging.info("Showing Data from table is successful")
            print(self.cursor.fetchall())
        except Exception as e:
            logging.error("Exception occurred", e)


obj = MySQL_Bulk_Upload("localhost", "abc", "password", "ineuron")

obj.create_connection()

obj.create_table("glassdata2", "col1 INT(10), col2 float(30,10), col3 float(30,10), col4 float(30,10), col5 float(30,10), col6 float(30,10), col7 float(30,10), col8 float(30,10), col9 float(30,10), col10 float(30,10), col11 INT(10)")


obj.insert_data("glass.data")


obj.show_data()




def test() -> int : 
    
    return "sudh" 