import json

class Saver:
    def __init__(self):
        self.data = []

    def save_data(self):
        with open('data.json', 'w') as f:  # writing JSON object
            json.dump(self.data, f)
            f.close()
            return True
        return False

    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                return data
        except: 
            print("json file not exist!")
        return[]   

    def add_measure(self,temperature,humidity,brightness,img_url):
        if(len(self.data)==0):
            self.data = self.load_data()
        measure = {"temperature":temperature,"humidity":humidity,"brightness":brightness,"img_url":img_url}
        self.data.append(measure)
        return self.save_data()
    
    def get_data(self):
        return self.data

