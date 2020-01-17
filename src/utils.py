from datetime import datetime
class Utils:
    def create_date(Y,M,D,h=1,m=1,s=1):
        return datetime(Y, M, D, h, m, s)
    def getTimeStamp():
        date = datetime.now()
        print(date)
        return (date.strftime("%d-%m-%Y_%H_%M"))


#Utils.getTimeStamp()
        
