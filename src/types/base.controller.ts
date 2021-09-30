import { Request, Response } from 'express';
import BaseDAO from './base.dao';

export default interface RestController {
  endpoint: string;
  name: string;

  get: (req: Request, res: Response) => void;
  post: (req: Request, res: Response) => void;
  put: (req: Request, res: Response) => void;
  delete: (req: Request, res: Response) => void;
}