from services.weather_service import get_weather
from fastapi import FastAPI
from dotenv import load_dotenv
from services.crowd_service import predict_crowd
from datetime import datetime
from services.ai_service import get_ai_recommendation
from fastapi.middleware.cors import CORSMiddleware
import os

load_dotenv()

app = FastAPI(
    title="Smart Tourism AI Backend",
    description="Backend API for Smart Tourism AI App",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # For development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


@app.get("/")
def home():
    return {
        "message": "Smart Tourism AI Backend is Running!"
    }


@app.get("/keys")
def check_keys():
    return {
        "OpenWeather Loaded": OPENWEATHER_API_KEY is not None,
        "Gemini Loaded": GEMINI_API_KEY is not None
    }
@app.get("/weather")
def weather(city: str):
    return get_weather(city)
@app.get("/crowd")
def crowd(
    destination: str,
    temperature: float,
    humidity: int
):

    now = datetime.now()

    hour = now.hour

    weekend = 1 if now.weekday() >= 5 else 0

    return predict_crowd(
        destination,
        hour,
        weekend,
        temperature,
        humidity
    )

@app.get("/tourism")
def tourism(destination: str):

    # Get live weather
    weather = get_weather(destination)

    if "error" in weather:
        return weather

    now = datetime.now()

    hour = now.hour
    weekend = 1 if now.weekday() >= 5 else 0

    # ML Prediction
    prediction = predict_crowd(
        destination,
        hour,
        weekend,
        weather["temperature"],
        weather["humidity"]
    )

    # Gemini Recommendation
    ai = get_ai_recommendation(
        destination,
        prediction["crowd_level"],
        weather["condition"]
    )

    return {
        "destination": destination,
        "weather": weather,
        "crowd": prediction,
        "ai_recommendation": ai
    }