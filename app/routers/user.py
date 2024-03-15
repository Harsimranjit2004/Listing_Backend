from .. import models, schemes, utils
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db


router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemes.UserOut)
def create_user(user:schemes.UserCreate, db:Session = Depends(get_db)):
    print(user)
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(email=user.email, password=user.password,firstName = user.firstName, lastName = user.lastName)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemes.UserOut)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")
    return user

@router.put("/{id}/change-password", response_model=schemes.UserOut)
def change_password(id:int, new_password:str, db:Session = Depends(get_db)):
    user  = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")
    hashed_password = utils.hash(new_password)
    user.password = hashed_password
    db.commit()
    db.refresh(user)
    return user