from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

#SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:\
#{settings.database_port}/{settings.database_name}'
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres_nakisback_user:6pXOzUMMFi9q0rUwHYk7QUvkIg3n5QMH@dpg-coiiji779t8c738hild0-a.singapore-postgres.render.com/postgres_nakisback"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Connects to database directly using postgres
# while True:
#     try:
#         conn =  psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='1234567890', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
