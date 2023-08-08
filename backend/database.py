# this file will connect to the mysql database for python using sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("DB_URI"))

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()