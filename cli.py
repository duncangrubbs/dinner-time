from Database import DatabaseInterface
from Query import Query
from Recommender import Recommender
from RandomMeal import RandomMeal

class CLI(object):
  @staticmethod
  def get_meal_from_user() -> object:
    '''Returns meal object that was generated by user'''
    name = input("Name: ")
    category = input("Category: ")
    season = input("Season: ")
    location = input("Location: ")
    time = int(input("Est. Time (mins): "))
    ingredients = []
    tags = []
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
    meal['category'] = category
    meal['season'] = season
    meal['location'] = location
    meal['time'] = time
    meal['ingredients'] = ingredients
    meal['last_suggested'] = 0
    meal['tags'] = tags
    return meal

  @staticmethod
  def print_meal(meal: object):
    '''Prints out a single meal cleary'''
    print(meal['name'] + ' - ' + str(meal['time']) + ' mins')
    print(meal['category'] + ', ' + meal['season'])
    print("Find recipe in: " + meal['location'])
    print("Ingredients:")
    for ingred in meal['ingredients']:
      print(ingred)
    print()

  @staticmethod
  def print_list(meal_list: list):
    '''Cleanly prints out a given list of meals'''
    i = 0
    for entry in meal_list:
      print(str(i) + ":")
      CLI.print_meal(entry)
      i += 1

  @staticmethod
  def repl():
    '''Main REPL loop for the program'''
    while True:
      data = DatabaseInterface.get_json_data(DatabaseInterface, 'database.json')
      user_input = input("Option: ")
      print()
      if (user_input == 'exit'):
        return
      if (user_input == 'l'):
        CLI.print_list(data['meals'])
      elif (user_input == 'q'):
        query_input = input("Query: ")
        r_category = Query.query_category(Query, query_input, data['meals'])
        r_season = Query.query_season(Query, query_input, data['meals'])
        
        CLI.print_list((r_season + r_category))
      elif (user_input == 'a'):
        meal = get_meal_from_user()
        meal['id'] = len(data['meals'])
        data['meals'].append(meal)

        DatabaseInterface.write_json_data(DatabaseInterface, data)
        print()
        print("Added Meal:")
        CLI.print_meal(meal)
      elif (user_input == 'r'):
        meal = RandomMeal.get_random_meal(data['meals'])
        CLI.print_meal(meal)
      elif (user_input == 'rr'):
        r = Recommender()
        meal = r.recommendation(data['meals'])
        CLI.print_meal(meal)

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