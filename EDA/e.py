from pymongo import MongoClient

client = MongoClient('mongodb+srv://scrap:scrap123@cluster0.a3bbo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


db = client['mydatabase']
collection = db['mycollection']

document = {"name": "sk", "city": "bengaluru"}
inserted_document = collection.insert_one(document)

print(f"Inserted Document ID: {inserted_document.inserted_id}")
client.close()
