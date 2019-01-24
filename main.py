import datetime
import os
import getpass

if __name__ == "__main__":
    # writedata.py
    print("write txt")
    current_id = str(getpass.getuser())
    file_path = "/home/" + current_id + "/writed_main.txt"
    f = open(file_path, 'w')
    f.write(str(datetime.datetime.now()))
    f.close()
    print("Save file")
