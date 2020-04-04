import json
import os

TEST_DB = './db/test_database.json'
PROD_DB = './db/database.json'

DB_PATH = TEST_DB

class DatabaseInterface:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    @staticmethod
    def get_json_data():
        '''Returns the JSON data from the DB file'''
        with open(DB_PATH) as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def get_meals():
        '''Returns the meal data from the DB file'''
        with open(DB_PATH) as json_file:
            data = json.load(json_file)
            return data['meals']

    @staticmethod
    def write_json_data(data):
        '''Basic DB writing function, just does a JSON dump'''
        with open(DB_PATH, 'w') as outfile:
            json.dump(data, outfile)
