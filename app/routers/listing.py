from .. import models, schemes, utils
from sqlalchemy.orm import joinedload
from sqlalchemy.sql import func
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
router = APIRouter(
    prefix="/listings",
    tags=['Listings']
)
@router.get("/", response_model=List[schemes.ListOut])
def get_listings(db:Session = Depends(get_db), search: Optional[str] = ""):
    lists = db.query(models.Listing).filter(
        models.Listing.title.contains(search)
    ).all()
    
    return lists
    

@router.post("/", response_model=schemes.ListOut)
def create_listing(list:schemes.CreateList, db:Session = Depends(get_db)):
    new_list = models.Listing(title = list.title, description = list.description, price= list.price,location = list.location, images = list.images, status = list.status )
    db.add(new_list)
    db.commit()
    db.refresh(new_list)
    return new_list
    

@router.get("/{id}", response_model=List[schemes.ListOut])
def getListing(id:int, db:Session = Depends(get_db)):
    list = db.query(models.Listing.listing_id == id).first()
    if not list:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"listing with id: {id} not found")
    return list

@router.put("/{id}", response_model=schemes.ListOut)
def updateListing(id:int,update_post:schemes.CreateList,  db:Session = Depends(get_db)):
    list_query = db.query(models.Listing).filter(models.Listing.id == id)
    list = list_query.first()
    if list == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
   
    list_query.update(update_post.dict(), synchronize_session=False)
    db.commit()

    return list_query.first()

@router.delete("/{id}", )
def delete():
    return {"listing": "delete lisitng"}