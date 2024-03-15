from fastapi import Depends, FastAPI
from .routers import listing
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
from psycopg2.extras import RealDictCursor
from . import models
from .database import engine ,SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(listing.router)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message":"Welcome to xo spacetech"}
@app.get("*")
def noPage():
    return {"message" : "404 Page"}
