from Database import DatabaseInterface
from Query import Query
from Recommender import Recommender
from util import print_list, print_meal, get_random_meal

class CLI(object):
    @staticmethod
    def get_meal_from_user() -> object:
        '''Returns meal object that was generated by user'''
        name = input("Name: ")
        region = input("Region: ").upper()
        main_ingred = input("Main Ingredient: ").upper()
        specialty = input("Specialty: ").upper()
        season = input("Season: ").upper()
        location = input("Location: ")
        time = input("Cook Time: ").upper()

        ingredients = []
        tags = []

        print('Ingredients and Tags')
        print("Type 'done' when done")
        while True:
            ingred = input("Ingredient: ")
            if (ingred == 'done'):
                break
            ingredients.append(ingred)
        while True:
            tag = input("Tag: ")
            if (tag == 'done'):
                break
            tags.append(tag)

        meal = {}
        meal['name'] = name
        meal['region'] = region
        meal['season'] = season
        meal['location'] = location
        meal['time'] = time
        meal['main_ingredient'] = main_ingred
        meal['specialty'] = specialty
        meal['ingredients'] = ingredients
        meal['last_suggested'] = 0
        meal['tags'] = tags
        return meal

    @staticmethod
    def user_query(data):
        query_input = input("Query: ")
        queries = query_input.split(' ')

        result = []
        for q in queries:
            res = []
            res += Query.query_region(Query, q, data['meals'])
            res += Query.query_main_ingredient(Query, q, data['meals'])
            res += Query.query_specialty(Query, q, data['meals'])
            res += Query.query_time(Query, q, data['meals'])
            res += Query.query_tags(Query, q, data['meals'])
            res += Query.query_season(Query, q, data['meals'])

            result += res

        print_list(result)

    @staticmethod
    def user_add(data):
        meal = CLI.get_meal_from_user()
        meal['id'] = len(data['meals'])
        data['meals'].append(meal)

        DatabaseInterface.write_json_data(data)
        print()
        print("Added Meal:")
        print_meal(meal) 

    @staticmethod
    def repl():
        '''Main REPL loop for the CLI'''
        while True:
            data = DatabaseInterface.get_json_data()
            user_input = input("Option: ")
            print()
            if (user_input == 'exit'):
                return
            if (user_input == 'l'):
                print_list(data['meals'])
            elif (user_input == 'q'):
                CLI.user_query(data)
            elif (user_input == 'a'):
                CLI.user_add(data)
            elif (user_input == 'r'):
                meal = get_random_meal(data['meals'])
                print_meal(meal)
            elif (user_input == 'rr'):
                r = Recommender()
                meal = r.recommendation(data['meals'])
                print_meal(meal)
            else:
                print('Invalid Command....')

    @staticmethod
    def run():
        print("Welcome to Dinner Time!")
        print("exit - to exit")
        print("l - to list meals in DB")
        print("q - to query")
        print("a - to add a meal")
        print("r - for random meal")
        print("rr - for recommended meal")
        print()

        CLI.repl()
