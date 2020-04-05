class Query(object):
    def query_season(self, query_string: str, meals: list) -> list:
        '''Returns a list of meals for the given season query string'''
        results = []
        for meal in meals:
            if meal['season'].upper() == query_string.upper():
                results.append(meal)
        return results

    def query_main_ingredient(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            if meal['main_ingredient'].upper() == query_string.upper():
                results.append(meal)
        return results

    def query_region(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            if meal['region'].upper() == query_string.upper():
                results.append(meal)
        return results

    def query_specialty(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            if meal['specialty'].upper() == query_string.upper():
                results.append(meal)
        return results

    def query_time(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            if meal['time'].upper() == query_string.upper():
                results.append(meal)
        return results

    def query_tags(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            for tag in meal['tags']:
                if tag.upper() == query_string.upper():
                    results.append(meal)
                    break
        return results
