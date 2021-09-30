import { Pool } from 'pg';
import BaseDAO from '../types/base.dao';
import Meal from './Meal';

export default class MealDao implements BaseDAO {
  database: Pool;

  table = 'meals';

  constructor(database: Pool) {
    this.database = database;
  }

  async getAllMeals() {
    return (await this.database.query(`SELECT * FROM ${this.table}`)).rows;
  }

  addMeal(meal: Meal) {
    const query = {
      text: `INSERT INTO ${this.table} (name, season, category, ingredients, url, last_suggested) VALUES ($1, $2, $3, $4, $5, $6)`,
      values: [
        meal.name,
        'FALL',
        meal.category,
        meal.ingredients,
        meal.url,
        meal.lastSuggested,
      ],
    };
    return this.database.query(query);
  }
}