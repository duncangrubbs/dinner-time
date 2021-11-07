import app from './app';
import config from './config';

app.listen(
  config.port,
  () => console.log(`[INFO] Local server on ${config.port}`),
);
