from elasticsearch import Elasticsearch
import json
from collections import OrderedDict
import datetime
import time
import logging
import random

class Insert_search:
    def __init__(self):
        self.index_id = 130
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%y %I:%M:%S %p', filename="insert_search.log", level=logging.DEBUG)

    #convert time format to insert in Elasticsearch
    def convert_timeToelasticsearch(self, date):
        convertedDate = date.replace(" ", "T") + "Z"
        logging.info("[convert_timeToelasticsearch]: " + convertedDate)

        return convertedDate

    def makejsonformat(self, convertedDate):
        temp = random.randrange(20,40)
        humi = random.randrange(40,90)

        group_data = OrderedDict()
        albums = OrderedDict()

        group_data["time_slot"] = convertedDate
        group_data["name"] = "Dansungsa"
        group_data["location"] = "37.570927,126.990279"
        group_data["temp"] = temp
        group_data["humi"] = humi

        json_doc = json.dumps(group_data, ensure_ascii=False, indent="\t")
        logging.info("[makejsonformat]: " + json_doc)

        print(json_doc)

        return json_doc

    def insert_elasticsearch(self, json_doc, index_id):
        es = Elasticsearch([{'host': 'search-roomcondition-wmednft2d2wtrun3vrh4tifv5m.us-west-2.es.amazonaws.com', 'port':80}])
        es.index(index="roomcondition", doc_type = "_doc" ,id=index_id, body=json_doc)

        logging.info("[insert_elasticsearch]: complete insert")

    def test_code(self):
        Year = 2019
        Month = 1
        Day = 20
        Hour = 0
        Min = 0
        Sec = 0

        test_date = str(dt.datetime(Year, Month, Day, Hour, Min, Sec))
        return test_date

    def current_date(self):
        now = datetime.datetime.utcnow()
        current_date_str = str("%04d-%02d-%02d %02d:%02d:%02d" % (now.year, now.month, now.day, now.hour, now.minute, now.second))

        logging.info("[current_date]: " + current_date_str)

        return current_date_str

    def main(self):
        while True:
            current_date_str = self.current_date()
            converted_date_str = self.convert_timeToelasticsearch(current_date_str)
            json_doc = self.makejsonformat(converted_date_str)
            self.insert_elasticsearch(json_doc, self.index_id)
            self.index_id = self.index_id + 1
            logging.info("[main-index_id]: " + str(self.index_id))
            time.sleep(30)

if __name__ == '__main__':
    Insert_search = Insert_search()
    Insert_search.main()
