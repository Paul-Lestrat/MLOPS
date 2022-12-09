from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import joblib

model = joblib.load("model.joblib")

class PredictionItem(BaseModel):
    PassengerId : Optional[int]#4,
    Pclass : Optional[int]#1,
    Name : Optional[str]#'Futrelle, Mrs. Jacques Heath (Lily May Peel)',
    Sex : Optional[str]#'female',
    Age : Optional[float]#35.0,
    SibSp : Optional[int]#1,
    Parch : Optional[int]#0,
    Ticket : Optional[str]#'13803',#
    Fare : Optional[float]#53.1,
    Cabin : Optional[str]#'C123',
    Embarked : Optional[str]#'S'

app = FastAPI()

@app.get("/")
def welcome():
    return {"hello": "world"}

@app.post("/prediction")
def requetage(item: PredictionItem):
    data = load_data(item)
    data = transform_data(data)
    predicted = prediction(data)
    return {"prediction": int(predicted)}

def load_data(data):
    data = pd.DataFrame(pd.Series(data.dict())).T
    return data

def transform_data(data):

    return data

def prediction(data):
    predicted = model.predict(data)
    return predicted
