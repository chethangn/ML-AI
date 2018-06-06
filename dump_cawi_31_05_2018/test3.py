from pymongo import MongoClient
import numpy as np
import enchant
import array
word = enchant.Dict("en_US")
#import grammar_check
#checker = grammar_check.LanguageTool('en-GB')
#import language_check
#tool = language_check.LanguageTool('en-US')

#gibberish = require('gibberish-detector');



client = MongoClient('localhost', 27017)
db = client.cawiAdminPanel
collection = db.chatbotqueries
content = np.array([])
#collection.find_one({"answered":"false"})
#print db.collection_names()

#var query={"answered": {$ne:false}};
#content = collection.find({});
content = collection.find({"answered":False},{'query'})
content_unique = content.distinct('query')

#content = collection.find({answered: {$ne: True}})

#content = collection.find({"$and":[ {"answered":{"$exists": True}}, {"answered":{"$ne": ""}}]})


#content = collection.find({}, {'answered':False})

#content = collection.find().distinct({'answered':False})
#content = collection.find({'answered':False})


#query1 = content.find().distinct('query')
#print content

#var query = db.collection.distinct('answered')
#print query
#content = collection.find({ answered: { $eq: 'false' } })
#print content.type

x = 0;
for value in content_unique:
	words = value.split(" ")
	if len(words) != 1 and content is None:
		for content in words:
			va = word.check(content)
			print content,va
	va = word.check(value)
	print value,va
#	matches = checker.check(value)
#	value2 = grammar_check.correct(value, matches)
	
#	value_gibberish = gibberish.detect(value)
#	print value, value_gibberish
#	matches_language = tool.check(value)
#	value3 = language_check.correct(value, matches_language)
	
#	value4 = asdfjkl(value);


	x += 1
print x
#for value1 in query1:
# 	print value1

#
#collection.find().toArray(function(err, docs){
#    console.log("retrieved records:");
#    console.log(docs);
#});
