from fastapi import FastAPI
from pydantic import BaseModel

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from fastapi.middleware.cors import CORSMiddleware


import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

df = load_iris()

X, y = df.data, df.target

model = RandomForestClassifier()
model.fit(X, y)

class InputData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def home():
    return {"message": "ML API Running"}

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[df.sepal_length, df.sepal_width, df.petal_length, df.petal_width]])
    prediction = model.predict(features)[0]
    return {"prediction": int(prediction)}

