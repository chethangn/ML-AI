import numpy as np
data = np.array([])
from pymongo import MongoClient
connection = MongoClient()
db = connection.cawiAdminPanel
# data = db.getCollection('chatbotqueries').find({})
# print(data)

data = db.getCollectionNames()
print(data)
