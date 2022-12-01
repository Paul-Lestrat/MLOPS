from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"response": "JTM Josse"}

@app.post("/prediction")
def prediction(item):
    return