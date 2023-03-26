import pymongo

# Connect to the MongoDB server
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Get the database and collection to store the data in
db = client['mydatabase']
collection = db['mycollection']

# Define the data to be stored in the collection
data = {
    'name': 'John Smith',
    'age': 30,
    'email': 'john.smith@example.com'
}

# Insert the data into the collection
result = collection.insert_one(data)
print('Data saved to MongoDB:', result.inserted_id)