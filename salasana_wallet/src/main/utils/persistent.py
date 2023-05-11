"""Persistent resources"""
from pymongo import MongoClient, errors


def initialize_database_passwords(users_collection, password_collection):
    client = MongoClient('mongodb://localhost:27017/')
    database = client['data']
    users_collection = database[users_collection]
    password_collection = database[password_collection]
    return client, database, users_collection, password_collection

def initialize_database_users(users_collection):
    client = MongoClient('mongodb://localhost:27017/')
    database = client['data']
    users_collection = database[users_collection]
    return client, database, users_collection

def connect_to_mongodb():
    """
    Connect to the MongoDB server.
    :return: MongoClient object representing the connection.
    """
    try:
        # Connect to the MongoDB server
        client = MongoClient('mongodb://localhost:27017/')
        return client
    except Exception as e:
        print(f"Failed to connect to MongoDB: {str(e)}")
        return None