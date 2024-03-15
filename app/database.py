from sqlalchemy import create_engine
import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base





SQLALCHEMY_DATABASE_URL = "postgres://xotechuser:3btuqe2Ymiq9uANZ5EPMDAHyxFjuvdoC@dpg-cnq0ksmn7f5s73f7dcf0-a.oregon-postgres.render.com/xotech"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
Base = declarative_base()