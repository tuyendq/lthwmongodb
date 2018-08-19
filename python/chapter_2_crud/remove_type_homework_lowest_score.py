import pymongo


# connection to database
connection = pymongo.MongoClient("mongodb://localhost")

db = connection.students
grades = db.grades2

query = {'type': 'homework'}
sort_options = [("student_id", pymongo.ASCENDING), ("score", pymongo.ASCENDING)]
try:
    cursor = grades.find(query).sort(sort_options)
    count = 0
    for doc in cursor:
        # print doc
        # print doc['_id']
        doc_id = doc['_id']
        # print doc_id
        # print doc['order']
        
        # grades.update_one({'_id': doc_id}, {'$set': {'order': count}})
        if (count % 2 == 0):
            try:
                grades.remove({'_id': doc_id})
            except Exception as e:
                print "Exception: ", type(e), e
        count += 1
    
except Exception as e:
    print "Exception: ", type(e), e




