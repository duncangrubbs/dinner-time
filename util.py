import random

def print_meal(meal: object):
    '''Prints out a single meal cleary'''
    print(meal['name'] + ' - ' + str(meal['time']) + ' mins')
    print(meal['category'] + ', ' + meal['season'])
    print("Find recipe in: " + meal['location'])
    print("Ingredients:")
    for ingred in meal['ingredients']:
        print(ingred)
    print()

def print_list(meal_list: list):
    '''Cleanly prints out a given list of meals'''
    i = 0
    for entry in meal_list:
        print(str(i) + ":")
        print_meal(entry)
        i += 1

def get_random_meal(meal_list: list) -> object:
    '''Returns random meal object from a list'''
    index = 0 if len(meal_list) == 1 else random.randint(1, len(meal_list) - 1)
    return meal_list[index]
