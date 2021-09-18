import { Request, Response } from 'express';
import RestController from '../types/RestController';

export default class MealController implements RestController {
  endpoint: string;

  name: string;

  constructor(endpoint: string, name: string) {
    this.endpoint = endpoint;
    this.name = name;
  }

  get(req: Request, res: Response) {
    res.status(200).send('GET /meals');
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