# lthwmongodb


##Aggredation

db.grades.aggregate([{'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1}])
