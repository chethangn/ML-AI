from pymongo import MongoClient
import numpy as np
import array
from bson.son import SON
import json
import pprint
import pandas as pd
import itertools
import time
topic_split = []

client = MongoClient('192.168.2.35', 27017)
db = client.database
collection = db.post
pd.options.display.max_colwidth = 100
data = pd.DataFrame(list(collection.find()))
# title_split = data['title'].head(1).to_string(index=False).split(" ")
# print(title_split)
# title_split = data['title'].head(1).to_string(index=False).split(" ")
# topic_split = data['topic']
# topic_split = data[['topic','title']].to_string(index=False)
# print(topic_split[0])


# formattedData = np.append(formattedData,[['EmpID','EmpName','InTime','OutTime','Date']])
# formattedData = formattedData.reshape((formattedData.shape[0], 1))
# formattedData = formattedData.reshape(-1, 2)

# formattednewData = np.append(formattednewData,[['topic','title','InTime','OutTime','Date']])



formatted_data = data[['topic','title']]
title_split = formatted_data['title'][1].split(" ")
# print(title_split)
mylist = np.array([])
topic_array = np.array([])
final_data = np.array([])
i = 0
perm_data = []
premuted_data = np.array([])
j = 0
formatted_data_length = len(formatted_data) - 1
while i < formatted_data_length:
    topic = formatted_data['topic'][i]
    title_split = formatted_data['title'][i].split(" ")
    title_length = len(title_split)
    perm_data = []
    for l in list(itertools.permutations(title_split)):
        perm_data.append(" ".join(l))
        j += 1
        print(j)
    premuted_data = np.append(premuted_data, np.array(perm_data)).reshape((-1,1))
    # for data in title_split:
    #     topic_array = np.append(topic_array, np.array(topic)).reshape((-1,1))        
    # mylist = np.append(mylist, np.array(title_split)).reshape((-1,1))
    # premuted_data = np.append(premuted_data, np.array(perm_data)).reshape((-1,1))
    i += 1
    print(i)
    time.sleep(2)
print(i,j)
# final_data = np.append(topic_array, premuted_data, axis=1)
print(premuted_data.shape)
# print(premuted_data.shape)
#     title_split =  formatted_data['title'][i].split(" ")

#     print(i)
#     print(title_split[i])

# for l in list(itertools.permutations(title_split)):
#     premuted_data.append(" ".join(l))
# y = np.array(premuted_data)
# print(premuted_data.shape)
# print(len(list(itertools.permutations(title_split))))



#print("".join(list(itertools.permutations(sent))))
# df = data.groupby('topic').count().reset_index().sort_values('title', ascending=False)
# print df
#for (topic, title) in data.groupby('topic'):
#    print("{0:30s} shape={1}".format(title,topic))
