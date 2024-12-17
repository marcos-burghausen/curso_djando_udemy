from pymongo import MongoClient

connection_string = "mongodb://root:root@localhost:27019"
client = MongoClient(connection_string)
db_connection = client['pdi']

print(db_connection)
print()

collection = db_connection.get_collection("contas")
print(collection)
print()

search_filter = {"ola": "Mundo"}
response = collection.find(search_filter)
print(f"response: {response}")
print()

for item in response:
    print(item)
