from bson.json_util imfrom bson.json_util import loads
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.computers
collection = db.senators

if(collection.count()==0):
    file = open("senators", "r")
    content = loads(file.read())["objects"]
    for line in content:
        collection.insert_one(line)

def gender(gender):
    return collection.find({"person.gender" : gender}, {"person.name" : 1})

def state(state):
    return collection.find({"state" : state}, {"person.name" : 1})

def party(party):
    return collection.find({"party" : party}, {"person.name" : 1})

def website(fname):
    return collection.find({"person.firstname" : fname}, {"person.name" : 1, "website" : 1})

def description(lname):
    return collection.find({"person.lastname" : lname}, {"person.name" : 1, "description" : 1})

def printer(data):
    for item in data:
        print(item["person"])

print("Male representatives\n")
printer(gender("male"))
print("Democrats\n")
printer(party("Democrat"))
print("ME senators\n")
printer(state("ME"))
print("Elizabeth's website\n")
printer(website("Elizabeth"))
print("Amy Klobuchar description\n")
printer(description("Klobuchar"))
