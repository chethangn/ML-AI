from pymongo import MongoClient
import numpy as np
import enchant
import array
word = enchant.Dict("en_US")

client = MongoClient('localhost', 27017)
db = client.cawiAdminPanel
collection = db.chatbotqueries
content = np.array([])

content = collection.find({"answered":False},{'query'})
content_unique = content.distinct('query')

count = 0;
for value in content_unique:
	words = value.split(" ")
	correctness = True
	for content in words:
		if content:
			value_correctness = word.check(content)
#			print content,value_correctness
		if value_correctness != True:
			correctness = False
	if correctness == True:
		value_correctness = True
	elif correctness == False:
		value_correctness = word.check(value)
	if value_correctness == True:
		print value
	count += 1
print count
