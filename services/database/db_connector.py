from ctypes import resize
from pymongo import MongoClient


class DBCollectionConnector:
    def __init__(self, db_host: str, db_port: str, database: str, collection: str) -> None:
        client = MongoClient(db_host, db_port)
        self.db = client[database]
        self.collection = self.db[collection]

    def insert_location(self, location: dict):
        self.collection.insert_one(location)
