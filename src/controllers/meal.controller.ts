import { Request, Response } from 'express';
import { ResponseCodes } from '../constants/ResponseCodes';
import Meal from '../model/meal';
import MealDao from '../model/meal.dao';
import database from '../services/db';
import extractPayload from '../services/extract-payload';
import buildApiResponse from '../services/format-response';
import RestController from '../types/base.controller';

export default class MealController implements RestController {
  endpoint: string;

  name: string;

  constructor(endpoint: string, name: string) {
    this.endpoint = endpoint;
    this.name = name;
  }

  async get(req: Request, res: Response) {
    // TODO: find a better solution for this
    const dao = new MealDao(database.pool);

    const meals = await dao.getAllMeals();
    res
      .status(ResponseCodes.Success)
      .json(buildApiResponse('Success', meals));
  }

  async post(req: any, res: Response) {
    const meals: Meal[] = extractPayload(req).meals;
    const dao = new MealDao(database.pool);

    for (let i = 0; i < meals.length; i += 1) {
      await dao.addMeal(meals[i]);
    }

    res
      .status(ResponseCodes.Success)
      .json(buildApiResponse('Success'));
  }

  put(req: Request, res: Response) {
    res.status(ResponseCodes.Success).send('PUT /meals');
  }

  async delete(req: Request, res: Response) {
    const ids: number[] = extractPayload(req).ids;
    const dao = new MealDao(database.pool);

    for (let i = 0; i < ids.length; i += 1) {
      await dao.deleteMeal(ids[i]);
    }

    res
      .status(ResponseCodes.Success)
      .json(buildApiResponse('Success'));
  }
}