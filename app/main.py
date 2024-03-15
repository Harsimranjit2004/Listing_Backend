from fastapi import Depends, FastAPI
from .routers import listing, user, auth
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine ,SessionLocal

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user.router)
app.include_router(listing.router)
app.include_router(auth.router)
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
