from datetime import datetime
class Utils:
    def create_date(y,m,d,h=0,m=0,s=1):
        return datetime(y, m, d, h, m, s)        
