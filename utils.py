from datetime import datetime
class Utils:
    def create_date(Y,M,D,h=1,m=1,s=1):
        return datetime(Y, M, D, h, m, s)        
