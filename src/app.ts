import express from 'express';
import * as expressWinston from 'express-winston';
import cors from 'cors';

import loggerOptions from './services/logger';
import config from './config';
import endpoints from './endpoints';

const app = express();

app.use(express.json());
app.use(cors());
app.use(expressWinston.logger(loggerOptions));

app.use(`/api/${config.version}`, endpoints);

app.get('*', (req, res) => {
  res
    .status(404)
    .send('Not Found');
});

export default app;
