from pymongo import Connection
connection = Connection()
connection = Connection('localhost', 27017)
db = connection.testdb
collection = db.chatbotqueries
for post in collection.find():
        print post
