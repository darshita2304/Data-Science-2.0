## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q3: create a class for tuple data extraction operation

import logging
logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")

class q3_tuples:
    def __init__(self, tuples):
        self.tuples = tuple(tuples)
    
    def extract_fn(self, startp, endp):

        logging.info("this is start of extract fn")
        try:
            logging.info("inside try block of extract fn")
            
            return self.tuples[int(startp):int(endp)]

        except Exception as e:
            #print(e)
            logging.error("there is some issue with extract fn")
            logging.error(e)
            

obj = q3_tuples((2,"3","hello1",5,0.5,8))

print(obj.extract_fn(2,5))

print(obj.extract_fn("",-1))

print(obj.extract_fn(-1,3))

print(obj.extract_fn(1,""))



