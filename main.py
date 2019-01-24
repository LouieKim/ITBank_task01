import datetime
import os
import getpass
import logging

if __name__ == "__main__":
    # writedata.py
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%y %I:%M:%S %p', filename='example.log', level=logging.DEBUG)
    logging.info('Make write main file')
    current_id = str(getpass.getuser())
    file_path = "/home/" + current_id + "/writed_main.txt"
    f = open(file_path, 'w')
    f.write(str(datetime.datetime.now()))
    f.close()
    logging.info('Done writed main file')
