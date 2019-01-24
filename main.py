import datetime

if __name__ == "__main__":
    # writedata.py
    print("write txt")
    f = open("writed_main.txt", 'w')

    f.write(str(datetime.datetime.now()))
    f.close()
    print("Save file")
