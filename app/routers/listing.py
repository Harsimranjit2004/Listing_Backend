from fastapi import APIRouter


router = APIRouter(
    prefix="/listings",
    tags=['Listings']
)
@router.get("/")
def get_listings():
    return {"listings": "all listings"}

@router.post("/")
def create_listing():
    return {"listing" : "create listing"}

@router.get("/{id}")
def getListing():
    return {"listing" : "get listing"}

@router.put("/{id}")
def updateListing():
    return {"listing": "update listing"}

@router.delete("/{id}")
def delete():
    return {"listing": "delete lisitng"}