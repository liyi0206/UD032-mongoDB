import json

def insert_data(data, db):
    for a in data:
        db.arachnid.insert(a)


if __name__ == "__main__":    
    from pymongo import MongoClient
    client = MongoClient("mongodb://localhost:27017")
    db = client.examples

    with open('C:/Benben/UD032 mongoDB/Lesson_4Problem_Set/02-Inserting_into_DB/arachnid.json') as f:
        data = json.loads(f.read())
        insert_data(data, db)
        print db.arachnid.find_one()