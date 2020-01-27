import random

class RandomMeal:
  @staticmethod
  def get_random_meal(meal_list: list) -> object:
    '''Returns random meal object from a list'''
    index = 0 if len(meal_list) == 1 else random.randint(1, len(meal_list) - 1)
    return meal_list[index]
