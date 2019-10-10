import datetime

from Query import Query
from RandomMeal import RandomMeal

class Recommender:
  def __init__(self, *args, **kwargs):
    return super().__init__(*args, **kwargs)

  def get_season(self, month: int) -> str:
    '''Returns the season string from the current month'''
    if (month >= 6 and month <= 8):
      return 'SUMMER'
    elif (month >= 9 and month <= 10):
      return 'FALL'
    elif (month >= 3 and month <= 5):
      return 'SPRING'
    elif (month >= 11 or month < 3):
      return 'WINTER'
  
  def recommendation(self, data: list) -> object:
    '''Returns a random meal from a current season query'''
    now = datetime.datetime.now()
    season = self.get_season(now.month)
    list_season = Query.query_season(self, season, data)
    if (len(list_season) == 0):
      return None
    return RandomMeal.get_random_meal(self, list_season)
