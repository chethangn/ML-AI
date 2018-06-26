from pymongo import MongoClient
import numpy as np
import array
from bson.son import SON
import json
import pprint

client = MongoClient('192.168.2.35', 27017)
db = client.database
collection = db.post
database_array = np.empty([5,5])

topic_uni = np.array([0])
topic_unique = np.array([0])

topic_uni = collection.distinct('topic')
topic_unique = np.array(topic_uni).reshape((-1,1))
database_contents = collection.find({}, {'title':1, 'topic':1,'tags':1, '_id':0})



for topic_content in topic_unique:
	myList = []
	for content in database_contents:
		data_topic = content['topic']
		# print(topic_content)
		if topic_content == data_topic:
			data_title = content['title']
			myList.append("Hello")
			# myList.append(data_title)
	print(myList)