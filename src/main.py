from mongo import Mongo
from utils import Utils
from pprint import pprint
#USAGE EXAMPLE HERE

        
m=Mongo()


m.add_measure(20,74.6,12)


#m.delete_all_measures() #BE CAREFUL WITH THAT

from_date=Utils.create_date(2019,10,13,20,56,25)
to_date= Utils.create_date(2020,1,1)

cursor = m.get_measures(from_date,to_date)

for document in cursor: 
    pprint(document)

