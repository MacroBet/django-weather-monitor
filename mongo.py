from pymongo import MongoClient
from datetime import datetime

class Mongo:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.pymongo_test

    def getDbs(self):
        print( self.client.list_database_names())

    def getDB(self):
        return self.db
        

    def add_measure(self,temperature,humidity,brightness,img_url=None):
        today = datetime.today()
        measures = self.db.measures
        measure_data = {
            'date': today,
            'temperature': temperature,
            'humidity': humidity,
            'brightness': brightness,
            'img_url': img_url
            
        }   
        result = measures.insert_one(measure_data)
        print('measure added : {0}'.format(result.inserted_id))

    def get_measure(self,date_from=None,date_to=None):
        



m=Mongo()
print(m.getDbs)
print(m.getDB().list_collection_names())
m.add_measure(20,74.6,12)

