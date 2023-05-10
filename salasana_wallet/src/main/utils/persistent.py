"""Persistent resources"""
from pymongo import MongoClient


def initialize_database():
    client = MongoClient('mongodb://localhost:27017/')
    database = client['mydatabase']
    collection = database['mycollection']
    return client, database,collection