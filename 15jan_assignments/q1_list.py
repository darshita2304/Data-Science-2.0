## 15th jan - Task List Assignments
## Q1 - q1 : create your own class to perform list search opearations

import logging
logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")


class q1_list:
    def __init__(self, list_arg):
        self.list_arg = list_arg
    
    def search_fn(self, search_arg):

        logging.info("this is start of search fn")
        try:
            logging.info("inside try block of search fn")
            
            if search_arg in self.list_arg:
                msg = str(search_arg) + " is found in given list"
            else:
                msg = str(search_arg) + " is found in given list"

            return msg
        except Exception as e:
            #print(e)
            logging.error("there is some issue with search fn")
            logging.error(e)
            

obj = q1_list([2,3,4,5,9,7,8])
print(obj.search_fn(3))

obj2 = q1_list(['hello','world','this','is','india'])
print(obj2.search_fn('hello'))

