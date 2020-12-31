from dotenv import load_dotenv
import os
import psycopg2

# Load .env file and get credentials
load_dotenv()
DB_NAME = os.getenv('DB_NAME', default='OOPS')
DB_USER = os.getenv('DB_USER', default='OOPS')
DB_PASS = os.getenv('DB_PASS', default='OOPS')
DB_HOST = os.getenv('DB_HOST', default='OOPS')

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        '''
        CREATE TABLE IF NOT EXISTS bb_users(
            user_id SERIAL PRIMARY KEY,
            user_name VARCHAR(30) UNIQUE NOT NULL,
            password VARCHAR (20) NOT NULL,
            user_ailment TEXT,
            user_effect TEXT
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS bb_strains(
            strain_id SERIAL PRIMARY KEY,
            strain_name VARCHAR(30) UNIQUE NOT NULL,
            strain_ailment TEXT,
            strain_effect TEXT
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS bb_iventory(
            user_id INT NOT NULL,
            strain_id INT NOT NULL,
            FOREIGN KEY(user_id)
                REFERENCES bb_users(user_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY(strain_id)
                REFERENCES bb_strains(strain_id)
                 ON UPDATE CASCADE ON DELETE CASCADE
        )
        '''
        )
    conn = None
    try:
        # connect to the PostgreSQL server
        conn = psycopg2.connect(
                                dbname=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST
                                )

        cursor = conn.cursor()
        # create table one by one
        for command in commands:
            cursor.execute(command)
        # close communication with the PostgreSQL database server
        cursor.close()
        # commit the changes
        conn.commit()
        print('done')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()