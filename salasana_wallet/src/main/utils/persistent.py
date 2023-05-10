"""Persistent resources"""
from pymongo import MongoClient


def initialize_database(database,collection):
    client = MongoClient('mongodb://localhost:27017/')
    database = client['mydatabase']
    collection = database[collection]
    return client, database,collection