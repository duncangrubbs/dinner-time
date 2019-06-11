from Database import DatabaseInterface
import random

# we would have labels for each meal, possibly ingredients
# these could be tags like: summer, hearty, quick, fancy, etc.
# and then when we wanted to find something, we could use those,
# or just get a random one

# CATEGORIES:
# salads
# pan meals? (enchiladas, etc.)
# mexican
# italian
# asian
# american

# this is just an on-going list, not for actual use
["Caesar Salad",
"Fajitas",
"Enchiladas",
"Thai Sliders",
"Shrimp Masala",
"Pasta Salad",
"Lasagna",
"Spice Rub Grilled Chicken",
"Salad Nicoise",
"Thai Coconut Curry",
"Lentil Soup",
"Chili (Turkey or Beef)",
"Tofu Enchilada Casserole",
"Ruben Sandwiches",
"Twice Baked Potatoes",
"Kung Pao Chicken"]

def get_random_meal(meal_list):
  index = random.randint(1, len(meal_list) - 1)
  return meal_list[index]

def get_meal_from_user():
  name = input("Name: ")
  category = input("Category: ")
  season = input("Season: ")
  time = int(input("Est. Time: "))
  ingredients = []
  while True:
    ingred = input("Ingredient: ")
    if (ingred == 'done'):
      break
    ingredients.append(ingred)
  meal = {}
  meal['name'] = name
  meal['category'] = category
  meal['season'] = season
  meal['time'] = time
  meal['ingredients'] = ingredients
  return meal

def print_list(data):
  '''Cleanly prints out a given list of meals'''
  for entry in data:
    print(entry['name'] + ' - ' + str(entry['time']) + ' mins')
    print(entry['category'] + ', ' + entry['season'])
    print()

def run():
  print("Welcome to Dinner Time!")
  print("Add a meal:")
  print()

  meal = get_meal_from_user()

  db = DatabaseInterface()
  data = db.get_json_data('database.json')
  data['meals'].append(meal)
  print_list(data['meals'])

  db.write_json_data(data)

run()
