from typing import Any              
import pandas as pd
import json
from typing import Any
import os
from pymongo.mongo_client import MongoClient


class mongodb_ops:

    def __init__(self, client_url : str, database_name : str, collection_name : str = None):

        self.client_url = client_url
        self.database_name = database_name
        self.collection_name = collection_name

    def create_client(self):
        client = MongoClient(self.client_url)
        return client
    
    def create_database(self):
        client = self.create_client()
        database = client[self.database_name]
        return database
    
    def create_collection(self, collect_name: str = None):
        database = self.create_database()
        if collect_name == None:
            collection = database[self.collection_name]
        else:
            collection = database[collect_name]
        return collection
    
    def insert_data(self, record, collect_name :str = None):
        if type(record) == list:
            for data in record:
                if type(data) != dict:
                    raise TypeError("Record must be in the Dictionary format")
            
            collection = self.create_collection(collect_name)
            collection.insert_many(record)

        elif type(record) == dict:
            collection = self.create_collection(collect_name)
            collection.insert_one(record)

    def file_insert(self, filepath : str, collection_name : str = None ):
        self.path = filepath

        if self.path.endswith(".csv"):
            data = pd.read_csv(self.path, encoding = "utf-8")
            
        elif self.path.endswith(".xlsx"):
            data = pd.read_excel(self.path, encoding = "utf-8")

        datajson = json.loads(data.to_json(orient = "record"))
        collection = self.create_collection(collection_name)
        collection.insert_many(datajson)