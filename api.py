from flask import Flask, jsonify, request
from Database import DatabaseInterface
from util import get_random_meal
from Recommender import Recommender
from Query import Query

def validate_meal(meal):
    assert meal['ingredients'] != None
    assert meal['time'] != None
    assert meal['season'] != None
    assert meal['category'] != None
    assert meal['name'] != None

app = Flask(__name__)

# API endpoints
@app.route('/api/meals/add', methods=['POST'])
def add_meal():
    meal = request.get_json()
    all_meals = DatabaseInterface.get_json_data()

    # validate and clean our meal
    validate_meal(meal)
    meal['last_suggested'] = 0
    meal['id'] = len(all_meals['meals'])
    
    # append to list and write-back data
    all_meals['meals'].append(meal)
    DatabaseInterface.write_json_data(all_meals)

    return meal, 200

@app.route('/api/meals/all', methods=['GET'])
def get_meals():
    all_meals = DatabaseInterface.get_meals()
    return jsonify(all_meals), 200

@app.route('/api/meals', methods=['GET'])
def query_meals():
    season = request.args.get('season')
    category = request.args.get('category')
    all_meals = DatabaseInterface.get_meals()
    query = Query()

    if (season == None):
        result = query.query_category(category, all_meals)
    else:
        result = query.query_season(season, all_meals)
    
    return jsonify(result), 200

@app.route('/api/meals/recommended', methods=['GET'])
def recommended_meal():
    all_meals = DatabaseInterface.get_meals()
    rec = Recommender()
    meal = rec.recommendation(all_meals)
    
    return meal, 200

@app.route('/api/meals/random', methods=['GET'])
def random_meal():
    all_meals = DatabaseInterface.get_meals()
    meal = get_random_meal(all_meals)
    return meal, 200

def run():
    app.run(debug=True, port=5000)
    