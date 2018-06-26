import requests
from bs4 import BeautifulSoup
from random import choice
from pymongo import MongoClient
import time
import re
count = 0
next_page = '//slashdot.org'

while next_page and count <= 150:
    next_page = 'https:'+ str(next_page)
   
    desktop_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']


    def random_headers():
        return {'User-Agent': choice(desktop_agents),'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'}
    time.sleep(2)

    try:
        conn = MongoClient('localhost', 27017)
        print("Connected successfully!!!")
    except:  
        print("Could not connect to MongoDB")
    db = conn.database
    collection = db.post

    page = requests.get(next_page,headers=random_headers())
    soup = BeautifulSoup(page.content, 'html.parser')

    for content in soup.select(".fhitem-story"):
        title_content = content.find(class_="story-title").get_text()
        topic_content_array = [d["title"] for d in content.select(".topic img")]
        topic_content = ''.join(map(str, topic_content_array))
        tag_content = [sd.get_text() for sd in content.select(".popular")]
        
        post_data = {
            'title': title_content,
            'topic': topic_content,
            'tags': tag_content
        }
        result = collection.insert_one(post_data)
        print(title_content,topic_content,tag_content)

    for link in soup.findAll('a', href=True, text='Older »'):
        next_page = link['href']
    print (next_page)
    count += 1
    print(count)

