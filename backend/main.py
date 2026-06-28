from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.post("/predict")
def predict_sentiment(data: TextData):
    # จำลองการทำงานของ ML Model
    sentiment = "Positive" if "ดี" in data.text else "Neutral/Negative"
    return {"input": data.text, "prediction": sentiment}
