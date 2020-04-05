class Query(object):
    def query_season(self, query_string: str, meals: list) -> list:
        '''Returns a list of meals for the given season query string'''
        results = []
        for meal in meals:
            if meal['season'].lower() == query_string.lower():
                results.append(meal)
        return results

    def query_main_ingredient(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            if meal['main_ingredient'].lower() == query_string.lower():
                results.append(meal)
        return results

    def query_region(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            if meal['region'].lower() == query_string.lower():
                results.append(meal)
        return results

    def query_specialty(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            if meal['specialty'].lower() == query_string.lower():
                results.append(meal)
        return results

    def query_time(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            if meal['time'].lower() == query_string.lower():
                results.append(meal)
        return results

    def query_tags(self, query_string: str, meals: list) -> list:
        results = []
        for meal in meals:
            for tag in meal['tags']:
                if tag.lower() == query_string.lower():
                    results.append(meal)
                    break
        return results
