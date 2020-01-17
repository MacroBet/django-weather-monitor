import pymongo
from pymongo import MongoClient
from datetime import datetime

class Mongo:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.pymongo_test
        self.debug=False

    def getDbs(self):
        print( self.client.list_database_names())

    def getDB(self):
        return self.db
        

    def add_measure(self,temperature,humidity,brightness,img_url=None):
        today = datetime.today()
        measures = self.db.measures
        measure_data = {
            'date': today,#.now().isoformat(),
            'temperature': temperature,
            'humidity': humidity,
            'brightness': brightness,
            'img_url': img_url
            
        }   
        result = measures.insert_one(measure_data)
        print('measure added : {0}'.format(result.inserted_id))

    def delete_all_measures(self):
        if(self.debug):
            x = self.db["posts"].delete_many({})

    def get_measures(self,date_from=None,date_to=None,sort=1):
        meausures = self.db["measures"]
        if(date_from!= None and date_to!=None):
            query= {"date": {"$lt": date_to,"$gte": date_from}}
        else:
            if(date_from!= None):
                query= {"date": {"$gte": date_from}}
            if(date_to!= None):
                query= {"date": {"$lt": date_to}}
        if(sort!=1 or sort!=-1):
            sort=1
        return meausures.find(query).sort("date",sort)
        

print("helo")
