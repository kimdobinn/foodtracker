from fastapi import APIRouter
from app.services.food_service import get_food_log

router = APIRouter()

@router.get("/")
def get_food():
    return get_food_log()
