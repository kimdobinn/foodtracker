from fastapi import FastAPI
from app.routes import users, food

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, FastAPI is running!"}

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(food.router, prefix="/food", tags=["Food"])

#docker-compose up --build
#docker-compose down
#docker-compose down --volumes