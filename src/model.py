import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from src.preprocessing import clean_text

MODEL_PATH = "models/job_scam_model.pkl"

def train_model():
    data = pd.read_csv("data/job_postings.csv")
    data["clean"] = data["text"].apply(clean_text)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(data["clean"])
    y = data["label"]

    model = LogisticRegression()
    model.fit(X, y)

    joblib.dump((model, vectorizer), MODEL_PATH)

def predict(text):
    model, vectorizer = joblib.load(MODEL_PATH)
    clean = clean_text(text)
    vec = vectorizer.transform([clean])
    return model.predict(vec)[0]

