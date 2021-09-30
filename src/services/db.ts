import { Pool } from 'pg';
import config from '../config';

class PostgreSQLDatabase {
  user: string;

  database: string;

  port: number;

  host: string;

  pool: Pool;

  constructor(user: string, database: string, port: number, host: string) {
    this.user = user;
    this.database = database;
    this.port = port;
    this.host = host;

    this.pool = this.connect();
  }

  connect() {
    console.log('here');
    return new Pool({
      user: this.user,
      host: this.host,
      database: this.database,
      port: this.port,
      max: 20,
      idleTimeoutMillis: 30000,
      connectionTimeoutMillis: 2000,
    });
  }
}

// this is a test
const database = new PostgreSQLDatabase(
  config.db.PG_USER,
  config.db.PG_DATABASE,
  parseInt(config.db.PG_PORT, 10),
  config.db.PG_HOST,
);

export default database;
