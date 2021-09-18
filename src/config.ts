const dotenv = require('dotenv');

dotenv.config();

const config = {
  port: 5000,
  version: 'v1',
  db: {
    PG_USER: process.env.PG_USER || '',
    PG_DATABASE: process.env.PG_DATABASE || '',
    PG_PORT: process.env.PG_PORT || '',
    PG_HOST: process.env.PG_HOST || '',
  },
};

export default config;
