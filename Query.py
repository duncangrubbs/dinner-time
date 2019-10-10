class Query:
  def query_season(self, query_string: str, meals: list) -> list:
    '''Returns a list of meals for the given season query string'''
    results = []
    for meal in meals:
      if meal['season'] == query_string:
        results.append(meal)
    return results

  def query_category(self, query_string: str, meals: list) -> list:
    '''Returns a list of meals for the given catergory query string'''
    results = []
    for meal in meals:
      if meal['category'] == query_string:
        results.append(meal)
    return results
