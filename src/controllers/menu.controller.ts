import { Request, Response } from 'express';
import { ResponseCodes } from '../constants/ResponseCodes';
import extractParams from '../services/extract-params';
import buildApiResponse from '../services/format-response';
import CreateMenu from '../services/menu/create-menu';
import RestController from '../types/base.controller';

export default class MenuController implements RestController {
  endpoint: string;

  name: string;

  constructor(endpoint: string, name: string) {
    this.endpoint = endpoint;
    this.name = name;
  }

  async get(req: Request, res: Response) {
    const params = extractParams(req);
    const days = parseInt(params.days);

    const createMenu = new CreateMenu(days);
    const menu = await createMenu.buildMenu();

    res
      .status(ResponseCodes.Success)
      .json(buildApiResponse('Success', { menu }));
  }

  post(req: Request, res: Response) {
    res.status(ResponseCodes.Success).send('POST /menu');
  }

  put(req: Request, res: Response) {
    res.status(ResponseCodes.Success).send('PUT /menu');
  }

  delete(req: Request, res: Response) {
    res.status(ResponseCodes.Success).send('DELETE /menu');
  }
}