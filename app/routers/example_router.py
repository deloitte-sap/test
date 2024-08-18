
from fastapi import APIRouter, Depends
from app.security import get_api_key

router = APIRouter()

@router.get("/example", dependencies=[Depends(get_api_key)])
def read_example():
    return {"Example": "This is an example endpoint"}
