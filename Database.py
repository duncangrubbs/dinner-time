import json
import os


class DatabaseInterface:
    def __init__(self, *args, **kwargs):
        return super().__init__(*args, **kwargs)

    def get_json_data(self, filename):
        '''Returns the JSON data from the DB file'''
        with open(filename) as json_file:
            data = json.load(json_file)
            return data

    @staticmethod
    def get_meals(filename):
        '''Returns the meal data from the DB file'''
        with open(filename) as json_file:
            data = json.load(json_file)
            return data['meals']

    def write_json_data(self, data):
        '''Basic DB writing function, just does a JSON dump'''
        with open('database.json', 'w') as outfile:
            json.dump(data, outfile)
