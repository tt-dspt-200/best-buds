    # - `stain_name`: string
    # - `description`: string
    # - `strain_ailment`: string
    # - `strain_effect`: string

    # strain_name: str = Field(..., example='nice pot')
    # description: str = Field(..., example='lots of cool info about nice pot')
    # strain_ailments: str = Field(..., example='insomnia, anxiety')
    # strain_effects: str = Field(..., example='peace, chillness')
import os
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy

# load_dotenv()
# DB_NAME = os.getenv('DB_NAME', default='OOPS')
# DB_USER = os.getenv('DB_USER', default='OOPS')
# DB_PASS = os.getenv('DB_PASS', default='OOPS')
# DB_HOST = os.getenv('DB_HOST', default='OOPS')

load_dotenv()
database_url = os.getenv('DB_URL', default='OOPS')
# engine = sqlalchemy.create_engine(database_url)
# connection = engine.connect()
# try:
#     yield connection
# finally:
#     connection.close()
print(database_url)
# print(DATABASE_URL)