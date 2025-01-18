from fastapi import FastAPI
from gc_nace_classifier.models import InputData, OutputData
from gc_nace_classifier.classify import classify_purchases

app = FastAPI()

@app.post("/classify")
async def classify(data: InputData):
    return classify_purchases(data)