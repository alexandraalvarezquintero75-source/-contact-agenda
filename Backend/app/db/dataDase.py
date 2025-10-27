from sqlalchemy import create_engine,MetaData
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

meta_data = MetaData()

try: 
    with engine.connect() as connection:
        print("successful connection to database")
except Exception as e:
    print("not connected to database")