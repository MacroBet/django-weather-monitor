from pymongo import MongoClient
from datetime import datetime
from pprint import pprint

class Mongo:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.pymongo_test
        self.debug=True

    def getDbs(self):
        print( self.client.list_database_names())

    def getDB(self):
        return self.db
        

    def add_measure(self,temperature,humidity,brightness,img_url=None):
        today = datetime.today()
        measures = self.db.measures
        measure_data = {
            'date': today.now().isoformat(),
            'temperature': temperature,
            'humidity': humidity,
            'brightness': brightness,
            'img_url': img_url
            
        }   
        result = measures.insert_one(measure_data)
        print('measure added : {0}'.format(result.inserted_id))

    def delete_all_measures(self):
        if(self.debug):
            x = self.db["measures"].delete_many({})

    def get_measures(self,date_from=None,date_to=None):
        meausures = self.db["measures"]
        return meausures.find({}).sort("date",1)
        
        



m=Mongo()
print(m.getDbs)
print(m.getDB().list_collection_names())
#m.add_measure(20,74.6,12)


cursor = m.get_measures()

for document in cursor: 
    pprint(document)


