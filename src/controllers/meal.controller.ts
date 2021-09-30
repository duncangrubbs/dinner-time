import { Request, Response } from 'express';
import MealDao from '../model/meal.dao';
import database from '../services/db';
import RestController from '../types/base.controller';

export default class MealController implements RestController {
  endpoint: string;

  name: string;

  constructor(endpoint: string, name: string) {
    this.endpoint = endpoint;
    this.name = name;
  }

  async get(req: Request, res: Response) {
    // this isn't super efficient but I can't find a workaround
    const dao = new MealDao(database.pool);

    const meals = await dao.getAllMeals();
    res.status(200).json(meals);
  }

  post(req: Request, res: Response) {
    res.status(200).send('POST /meals');
  }

  put(req: Request, res: Response) {
    res.status(200).send('PUT /meals');
  }

  delete(req: Request, res: Response) {
    res.status(200).send('DELETE /meals');
  }
}