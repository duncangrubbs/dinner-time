import { Pool } from 'pg';
import BaseDAO from '../types/base.dao';
import Meal from './meal';

export default class MealDao implements BaseDAO {
  database: Pool;

  table = 'meals';

  constructor(database: Pool) {
    this.database = database;
  }

  async getAllMeals() {
    return (await this.database.query(`SELECT * FROM ${this.table}`)).rows;
  }

  async addMeal(meal: Meal) {
    const query = {
      text: `INSERT INTO ${this.table} (name, season, category, ingredients, url, last_suggested) VALUES ($1, $2, $3, $4, $5, $6)`,
      values: [
        meal.name,
        meal.season,
        meal.category,
        meal.ingredients,
        meal.url,
        meal.lastSuggested,
      ],
    };
    await this.database.query(query);
  }

  async deleteMeal(id: number) {
    const query = {
      text: `DELETE FROM ${this.table} WHERE id = $1`,
      values: [
        id,
      ],
    };
    await this.database.query(query);
  }
}