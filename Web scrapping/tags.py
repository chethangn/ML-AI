from pymongo import MongoClient
import numpy as np
import array
client = MongoClient('localhost', 27017)
db = client.database
collection = db.post
content_unique = np.array([0])

content_unique = np.append(content_unique,[[collection.distinct('tags')]])
print (np.shape(content_unique))
