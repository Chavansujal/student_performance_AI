from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

# Create FastAPI app
app = FastAPI(
    title="Student AI Predictor API",
    description="AI-powered student marks prediction system",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change later for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load trained ML model
model = joblib.load("student_model.pkl")


# Input data model
class StudentData(BaseModel):
    studytime: int
    absences: int
    g1: int
    g2: int


# Home route
@app.get("/")
def home():
    return {
        "message": "Student AI API Running Successfully"
    }


# Prediction route
@app.post("/predict")
def predict(data: StudentData):

    try:
        # Convert input into ML model format
        features = np.array([[
            data.studytime,
            data.absences,
            data.g1,
            data.g2
        ]])

        # Predict
        prediction = model.predict(features)

        predicted_marks = round(float(prediction[0]), 2)

        return {
            "success": True,
            "predicted_g3": predicted_marks
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }