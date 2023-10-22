from pymongo import MongoClient
import pymongo
client = MongoClient("localhost",27017)


dbs=client.list_database_names()
print(dbs)
db = client['my_store']
print(db)


print(db.list_collection_names())
users = db['user_data']


# CRUD OPERATIONS
users.insert_one({
    "name":"Soma",
    "age":23
})

# a=users.find_one({"name":"Soma"})
# print(a['age'])


# users.update_many({
#     "name":"Soma"
# },{"$set":{"name":"Raj","age":40}})

users.delete_many({"name":"Raj"})


# Insert Functionality

bag = {
    "bag":23.55,
}

note = {
    "name":"note",
    "price":90
}

prods = db['products']
prods.insert_many([bag,note])

# Find Functionality

#Curose 
ac =users.find({"name":"Soma"})
print(ac.alive) 
for i in ac:
    print(i)
print(ac.alive)

#sort
for i in users.find({"name":"Soma"}).sort("age",pymongo.ASCENDING):
    print(i)

page_limit = 3

for page in [1,2,3,4,5]:
    print(page)
    for doc in users.find({}).skip((page-1)*page_limit).limit(page_limit).sort("age",1):
        print(doc)