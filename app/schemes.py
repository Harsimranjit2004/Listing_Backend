from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional, List



class CommentOut(BaseModel):
    id:int 
    user_id:int
    listing_id:int
    content:str
    timestamp:datetime

    class Config:
        from_attributes:True

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_At: datetime
   
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    firstName:str
    lastName:str

class ListOut(BaseModel):
    listing_id:int
    title:str
    description:str
    price:float
    location:str
    date_posted:datetime
    status:str
    images:str


    class Config:
        from_attributes = True

class CreateList(BaseModel):
    title:str
    description:str
    price:float
    location:str
    status:str
    images:str
    

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    token: str
    token_type: str

    class Config:
        from_attributes = True


class TokenData(BaseModel):
    id: Optional[str] = None