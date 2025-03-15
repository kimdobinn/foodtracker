from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class FoodLog(Base):
    __tablename__ = "food_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    food = Column(String)
    calories = Column(Integer)
