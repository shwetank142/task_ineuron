import pymongo
client = pymongo.MongoClient("mongodb+srv://shwetank:shwetank123@cluster0.rjsvn.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {'name':'shwetank', 'email':'shwetankkumar196@gmail.com','surname':'kumar'}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)