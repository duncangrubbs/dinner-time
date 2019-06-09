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

# this is just an on-going list, not for acutal use
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
  season = input("Season: ")
  time = int(input("Est. Time: "))
  meal = {}
  meal['name'] = name
  meal['season'] = season
  meal['time'] = time
  meal['ingredients'] = []  
  return meal

def run():
  print("Welcome to Dinner Time!")
  print("Options:")
  print("Query - q")
  print("Write - w")
  print("Help - h")
  db = DatabaseInterface()
  data = db.get_json_data('database.json')
  print(data['meals'][0]['name'])

run()

