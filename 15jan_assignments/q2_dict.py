## 15th jan - Task List Assignments
## Q2: create a class for dict new element addition

import logging
logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")


class q2_dict:
    def __init__(self, mydict):
        self.mydict = mydict
    
    def add_key_values_fn(self, key_values):
        logging.info("this is start of add_key_values_fn ")
        try:
            logging.info("inside try block of add_key_values_fn ")

            self.mydict.update(key_values)
            
            return self.mydict
        except Exception as e:
            #print(e)
            logging.error("there is some issue with add_key_values_fn ")
            logging.error(e)
        



obj = q2_dict({'key1':'value1','key2':'value2','key3':'value3'})
new_dict = obj.add_key_values_fn({'key4':'value4'})
print(new_dict)

