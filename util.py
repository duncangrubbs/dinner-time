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