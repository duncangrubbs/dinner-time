from flask import Flask, jsonify, request
from Database import DatabaseInterface
from RandomMeal import RandomMeal

app = Flask(__name__)

# API endpoints

@app.route('/api/meals/add', methods=['POST'])
def add_meal():
  meal = request.get_json()

  print(meal)
  return meal, 200

@app.route('/api/meals/all', methods=['GET'])
def get_meals():
  return '200 OK'

@app.route('/api/meals/<string:query_value>', methods=['GET'])
def query_meals():
  return '200 OK'

@app.route('/api/meals/recommended', methods=['GET'])
def recommended_meal():
  return '200 OK'

@app.route('/api/meals/random', methods=['GET'])
def random_meal():
  all_meals = DatabaseInterface.get_meals('database.json')
  meal = RandomMeal.get_random_meal(all_meals)
  return meal, 200

if __name__ == '__main__':
  app.run(debug=True, port=5000)