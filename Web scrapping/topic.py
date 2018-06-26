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

# tags_uni = np.array([0])
# tags_unique = np.array([0])
topic_uni = np.array([0])
topic_unique = np.array([0])


# tags_uni = np.append(tags_uni,[[collection.distinct('tags')]])
# tags_unique = np.array(tags_uni).reshape((-1,1))
topic_uni = np.append(topic_uni,[[collection.distinct('topic')]])
topic_unique = np.array(topic_uni).reshape((-1,1))
#database_contents = collection.find()
database_contents = collection.find({}, {'title':1, 'topic':1,'tags':1, '_id':0})
database_title = collection.find({}, {'title':1, '_id':0})
database_topic = collection.find({}, {'topic':1, '_id':0})
database_tags = collection.find({}, {'tags':1, '_id':0})

count = 0
count1 = 0

# for content in database_contents:
#   data = content['topic']
#   data = str(data)
#   count1 += 1
#   data_title = []
#   for content_unique in topic_unique:
#     if data == content_unique:
#       title = content['title']
#       data_title.append(title)
#       # print("Hello")
#     count += 1
#   # print(data_title,"\n")


countzz = 0
countxx = 0
countcc = 0
countvv = 0
countaa = 0
print(len(topic_unique),type(topic_unique),topic_unique.shape)
print(type(database_contents))
# for content_unique in topic_uni:
# 	print('outside ', content_unique)
# 	for content in database_contents:
# 		print('inside ', content_unique)







#print(countxx,countzz,countvv,countaa)


# print(count,count1,type(content_unique))
# data_array = np.array([])

# next_topic = None
# for content in tags_unique:
#   topic = content
#   data_title = []
#   for content in database_contents:
#     data = content['topic']
#     if topic == data:
#       title = content['title']
#       data_title.append('title')
#       # data_title = np.hstack((data_title,title))
#     print(data_title)
#   database_array = np.hstack((database_array,data_title))



































# data_array = np.empty((0, 100))
# result_array = np.empty(data_array.size)

# count1 = 0


# for content_unique in topic_unique:
#   unique_content = str(content_unique)
#   count += 1
#   for content_database in database_contents:
#     data = str(content_database['topic'])
#     # print(type(data),data,type(unique_content),unique_content)
#     if unique_content == data:
#       print("Hello")
#     count1 += 1
# print(count)

# count2 = 0
# count3 = 0
# for content_unique in topic_unique:
#   count2 += 1
# for content in database_contents:
#   print(content_database['topic'])
#   count3 += 1
# print(count2,count3)




















# for content in tags_unique:
#   topic = content
#   data_title = []
#   for content in database_contents:
#     data = content['topic']
#     if topic == data:
#       title = content['title']
#       data_title.append(title)
#       print(data)
  # try:
  #   conn = MongoClient('localhost', 27017)
  #   print("Connected successfully!!!")
  # except:
  #   print("Could not connect to MongoDB")
  # db = conn.database
  # collection = db.formatted_data
  # post_data = {
  #           'topic': topic,
  #           'title': [data_title]
  #       }
  # result = collection.insert_one(post_data)
  # data_array = np.append(data_array, [data_title], axis=0)
# print(data_array)












# print(database_array)
  #   if topic == data:
  #     print('Hello')

  # current_topic = content['topic']
  # if next_topic is not None:
  #   if current_topic == next_topic:
  #     print('Hello')
  # else:
  #   next_topic = content['topic']




# for post in collection.find():
#   print(post)
  # database_contents = np.append(database_contents,[[collection.distinct('tags')]])
  # pprint.pprint(post)


# database_contents = coll.find_one('_id': doc_id)

# tags_uni = np.append(tags_uni,[[collection.find('tags')]])
# database_contents = np.array(tags_uni).reshape((-1,1))


# print(database_contents)









# zzz = db.collection.distinct('tags').length
# print(zzz)
# var = db.collection.aggregate([
# { '$group':{
#     '_id':{'topic':"$topic"},
#     'uniqueId':{'$addToSet':"$_id"},
#     'count':{"$sum":1}
#   }
# },
# { '$match':{
#   'duplicate':{"$gt":1}
#  }
# }
# ])



# num = db.collection.aggregate(
#     {"$group" : {"_id": "$topic", "count": { "$sum": 1 } } },
#     {"$match": {"count" : {"$gt": 1} } }, 
#     {"$project": {"topic" : "$_id", "_id" : 0} }
# )





# var map = function(){
#    if(this.topic) {
#         emit(this.topic, 1);
#    }
# }

# var reduce = function(key, values){
#     return Array.sum(values);
# }

# var res = db.collection.mapReduce(map, reduce, {out:{ inline : 1}});
# db[res.result].find({value: {$gt: 1}}).sort({value: -1});


# data = db.collection.aggregate(
#     {"$match": {"name" :{ "$ne" : None } } }, 
#     {"$group" : {"_id": "$name", "count": { "$sum": 1 } } },
#     {"$match": {"count" : {"$gt": 1} } }, 
#     {"$project": {"name" : "$_id", "_id" : 0} }
# )
# data = db.collection.aggregate([
# {'$group' : { id: "$topic" , 'count' : { '$sum': 1}}},
# {'$match' : { 'count' : { '$gt' : 1 } }}, 
# {"$project": {"topic" : "$_id", "_id" : 0} } ])



# value = db.collection.aggregate([
#     {'$match': {'topic': {'$ne': None}}},
#     {'$group': { 
#         '_id': {'campaign_id': "$campaign_id",'campaign_name': "$campaign_name"},
#         'count': {'$sum': 1}
#     }}
# ])


# value = db.campaigns.aggregate([
#     {'$match': {'topic': {'$ne': None}}},
#     {'$group': { 
#         '_id': {'title': "$title"},
#         'count': {'$sum': 1}
#     }}
# ])


# for document in var:
#     print(document)
# print(list(var))
# print(value)
# print (np.shape(tags_unique))
# print (np.shape(topic_unique))
# print(list(value))
# for doc in collection.aggregate(value):
#     print(value)
# print (data)
# print (list(db.things.aggregate(num)))
