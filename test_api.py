import requests
from time import perf_counter
import json

response = requests.post('http://localhost:8000/prediction',
                        json={
                        "PassengerId": 1,
                        "Pclass": 3,
                        "Name": "Braund, Mr. Owen Harris",
                        "Sex": "male",
                        "Age": 22,
                        "SibSp": 1,
                        "Parch": 0,
                        "Ticket": "A/5 21171",
                        "Fare": 7.25,
                        "Cabin": None,
                        "Embarked": "S"
                        })

json_obj = json.loads(response.text)
print(json_obj["prediction"])
