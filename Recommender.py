import datetime

from Query import Query
from util import get_random_meal

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

    def recommendation(self, meal_list: list) -> object:
        '''Returns a random meal from a current season query'''
        current_date = datetime.datetime.now()
        current_season = self.get_season(current_date.month)

        meals_of_season = Query.query_season(self, current_season, meal_list)
        if (len(meals_of_season) == 0):
            return get_random_meal(meal_list)
        return get_random_meal(meals_of_season)
