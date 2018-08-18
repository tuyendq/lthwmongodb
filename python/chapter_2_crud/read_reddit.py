#!/usr/bin/env python

import json
# import urllib2
import urllib3
import pymongo

# connect to mongo
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the reddit database
db = connection.reddit
stories = db.stories

# drop existing collection
stories.drop()

# get the reddit home page
# reddit_page = urllib2.urlopen("https://www.reddit.com/r/technology/.json")
http = urllib3.PoolManager()
reddit_page = http.request("GET", "http://www.reddit.com/r/technology/.json")

# parse the json into python objects
# parsed = json.loads(reddit_page.read())
parsed = json.loads(reddit_page.data.decode('utf-8'))

# iterate through every news item on the page
for item in parsed['data']['children']:
    # put it in mongo
    stories.insert_one(item['data'])
