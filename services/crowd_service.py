import joblib

# Load trained model
model = joblib.load("models/crowd_model.pkl")
encoder = joblib.load("models/destination_encoder.pkl")


def predict_crowd(destination, hour, weekend, temperature, humidity):

    # If destination wasn't in training data
    if destination not in encoder.classes_:
        destination = encoder.classes_[0]

    destination_encoded = encoder.transform([destination])[0]

    prediction = model.predict([[
        destination_encoded,
        hour,
        weekend,
        temperature,
        humidity
    ]])[0]

    prediction = int(round(prediction))

    # Crowd Level
    if prediction < 35:
        level = "Low"
        wait = "5-10 min"
    elif prediction < 70:
        level = "Medium"
        wait = "15-25 min"
    else:
        level = "High"
        wait = "30-45 min"

    # Parking prediction
    total_slots = 60
    available = max(0, total_slots - int(prediction * 0.6))

    return {
        "crowd_percentage": prediction,
        "crowd_level": level,
        "waiting_time": wait,
        "parking_available": available,
        "parking_total": total_slots
    }