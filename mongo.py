from pymongo import MongoClient

class Mongo:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.pymongo_test
        posts = self.db.posts
        post_data = {
            'title': 'Python and MongoDB',
            'content': 'PyMongo is fun, you guys',
            'author': 'Scott'
        }   
        result = posts.insert_one(post_data)
        print('One post: {0}'.format(result.inserted_id))



