from fastapi import APIRouter
from app.services.user_service import get_user_by_id

router = APIRouter()

@router.get("/{user_id}")
def get_user(user_id: int):
    return get_user_by_id(user_id)
