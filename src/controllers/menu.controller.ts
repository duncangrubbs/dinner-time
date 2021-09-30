import { Request, Response } from 'express';
import RestController from '../types/base.controller';

export default class MenuController implements RestController {
  endpoint: string;

  name: string;

  constructor(endpoint: string, name: string) {
    this.endpoint = endpoint;
    this.name = name;
  }

  get(req: Request, res: Response) {
    res.status(200).send('GET /menu');
  }

  post(req: Request, res: Response) {
    res.status(200).send('POST /menu');
  }

  put(req: Request, res: Response) {
    res.status(200).send('PUT /menu');
  }

  delete(req: Request, res: Response) {
    res.status(200).send('DELETE /menu');
  }
}