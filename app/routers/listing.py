from .. import models, schemes, utils
from sqlalchemy.orm import joinedload,Query
from sqlalchemy.sql import func
from fastapi import FastAPI, Depends, status, Response, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from random import randint , choice
from typing import List, Optional,Union
router = APIRouter(
    prefix="/listings",
    tags=['Listings']
)
@router.get("/", response_model=List[schemes.ListOut])
def get_listings(db: Session = Depends(get_db), search: Optional[str] = "",
                bathrooms: Optional[Union[int, str]] = None,
                rooms: Optional[Union[int, str]] = None,status: Optional[str] = None,
                type:Optional[str] = None,
                min_price: Optional[Union[float, str]] = None, max_price: Optional[Union[float, str]] = None):
    
    query: Query = db.query(models.Listing)

    if search  or type is not None or bathrooms is not None or \
          rooms is not None or min_price is not None or max_price is not None or status is not None:
        
        query = query.filter(models.Listing.title.ilike(f"%{search}%"))
        
        
        if bathrooms is not None and bathrooms != "any":
            query = query.filter(models.Listing.nBathrooms <= int(bathrooms))
        if rooms is not None and rooms != "any" :
            query = query.filter(models.Listing.nRooms <= int(rooms))
        if min_price is not None and min_price != "any" :
            query = query.filter(models.Listing.price >= float(min_price))
        if max_price is not None and max_price != "any":
            query = query.filter(models.Listing.price <= float(max_price))
        if status is not None and status != "any" :
            query = query.filter(models.Listing.status.ilike(f"%{status}"))
        if type is not None and type != "any":
            query = query.filter(models.Listing.type.ilike(f"%{status}"))
    lists = query.all()
    return lists



@router.post("/", response_model=schemes.ListOut)
def create_listing(list:schemes.CreateList, db:Session = Depends(get_db)):
    new_list = models.Listing(title = list.title, description = list.description, price= list.price,location = list.location, images = list.images, status = list.status, nBathrooms = list.nBathrooms, nRooms = list.nBathrooms, type = list.type)
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
    list_query = db.query(models.Listing).filter(models.Listing.listing_id == id)
    list = list_query.first()
    if list == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
   
    list_query.update(update_post.dict(), synchronize_session=False)
    db.commit()

    return list_query.first()

@router.delete("/{id}", )
def delete(id:int,  db:Session = Depends(get_db)):
    list_query = db.query(models.Listing).filter(models.Listing.listing_id == id)
    list = list_query.first()
    if list == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    list_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)