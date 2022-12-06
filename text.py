#the file name is text and the log file is test
import logging
logging.basicConfig(filename='test.log',level=logging.INFO)
logging.info('this is my very 1st code for logging')
logging.warning('this will try to load a warning message')
logging.error('this is a error message from system')
l=[1,2,3,4,5,6,7,7]
for i in l:
    if i==2:
        logging.info(l)
        logging.warning('this is a warning for a user that they have found out 2 in list')
logging.shutdown()










