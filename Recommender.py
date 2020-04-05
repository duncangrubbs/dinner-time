import datetime

from Query import Query
from util import get_random_meal
from Database import DatabaseInterface
import time
import sys

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

    def update_sug_time(self, meal, time):
        meals = DatabaseInterface.get_meals()
        all_meals = { 'meals': [] }

        for m in meals:
            if m['name'] != meal['name']:
                all_meals['meals'].append(m)
        meal['last_suggested'] = time
        meal['id'] = len(all_meals['meals'])

        all_meals['meals'].append(meal)
        DatabaseInterface.write_json_data(all_meals)


    def recommendation(self, meal_list: list) -> object:
        '''Returns a random meal from a current season query'''
        current_date = datetime.datetime.now()
        current_time = time.time()
        current_season = self.get_season(current_date.month)

        meals_of_season = Query.query_season(self, current_season, meal_list)
        maxx = float('-inf')
        if (len(meals_of_season) == 0):
            selected_meal = None
            for meal in meal_list:
                if (current_time - meal['last_suggested'] > maxx):
                    maxx = current_time - meal['last_suggested']
                    selected_meal = meal
            self.update_sug_time(selected_meal, current_time)
            return selected_meal

        selected_meal = None
        for meal in meals_of_season:
            if (current_time - meal['last_suggested'] > maxx):
                maxx = current_time - meal['last_suggested']
                selected_meal = meal
        self.update_sug_time(selected_meal, current_time)
        return selected_meal
