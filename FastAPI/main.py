from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}

@app.get("/about")
def about():
    return {"message": "This is not a DRill"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
