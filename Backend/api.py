import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

# Load model + vectorizer
model = joblib.load("svm_sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

app = FastAPI()


class Review(BaseModel):
    text: str



@app.get("/")
def home():
    return {"message": "Sentiment Analysis API is running"}


@app.post("/predict")
def predict_sentiment(review: Review):
    text_vec = vectorizer.transform([review.text])
    prediction = model.predict(text_vec)[0]

    sentiment = "Positive" if prediction == 1 else "Negative"

    return {
        "review": review.text,
        "sentiment": sentiment
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)