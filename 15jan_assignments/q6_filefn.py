## 15th jan - Task List Assignments
## Author: Darshita Paghadal
## Q6: create a calss to perform append and delete operation in file and inherit it in child class

import logging
logging.basicConfig(filename='file_calss.log', level=logging.DEBUG, filemode='w', format="""%(asctime)s %(levelname)s %(message)s""")

class q6_filefn:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        logging.info("this is a start of a read operation")
        try:
            logging.info("inside try block of read fn")

            with open(self.filename, "r") as fo:
                str = fo.read()

                logging.info("i m able to read the file")
                #print(f"Read String is : {str}")
                # Close opend file
                fo.close()
                return str
        except FileNotFoundError as e:
            #print(e)
            logging.error("there is some issue with read file operation")
            logging.error(e)

    def write(self, txt):
        logging.info("this is a start of a write operation")
        try:
            with open(self.filename, "a") as fo:
                fo.write(txt)
                # Close opend file
                fo.close()
                logging.info("complete write operation")
                return
        except Exception as e:
            logging.error("there is some issue with write file operation")
            logging.error(e)
            

class child_filefn(q6_filefn):
    def __init__(self, filename):
        q6_filefn.__init__(self, filename)


# obj = q6_filefn("abc.txt")
# #obj.write("Hello, This is text file created using pythong programming..")
# obj.write("Practice makes Perfect.. Keep it up..")
# obj.read()

obj = child_filefn("abc1.txt")
obj.write("\n Hello, This is text file created using pythong programming..")
obj.write("\n Practice makes Perfect.. Keep it up..")
obj.read()