from pymongo import MongoClient

class MqttDBConnector:
    def __init__(self, client: MongoClient, database: str, collection: str) -> None:
        self.client = client
        self.db = client[database]
        self.collection = self.db[collection]

    
    def insert_location(self, location: dict):
        self.collection.insert_one(location)