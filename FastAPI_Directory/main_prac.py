from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 1) GET Method
@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/about")
def about():
    return {"message": "This is not a DRill"}

# 2) Path Parameters
@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

# 3) Query Parameters
@app.get("/items/")
def get_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit":limit}

# 4) POST MEthod
class User(BaseModel):
    name: str
    age: int

@app.post("/create_user/")
def create_user(user: User):
    return {
        "user": user
    }