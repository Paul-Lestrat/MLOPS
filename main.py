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

@app.get("/welcome")
def welcome():
    return {"response": "Hello world"}

@app.post("/prediction")
def prediction(item: PredictionItem):
    # chargement des données
    item = load_data(item)
    # feature engineering + ML
    item = transform_data(item)
    item = predicted(item)
    # Envoi des données  
    return {"prediction": int(item)}

def load_data(item):
    item = pd.DataFrame(pd.Series(item.dict())).T
    return item 

def transform_data(item):
    return item

def predicted(item):
    item = model.predict(item)
    return item