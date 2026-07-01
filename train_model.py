import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
df = pd.read_csv("data/crowd_data.csv")

# Convert destination names into numbers
encoder = LabelEncoder()
df["destination"] = encoder.fit_transform(df["destination"])

# Features and target
X = df[["destination", "hour", "weekend", "temperature", "humidity"]]
y = df["crowd"]

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model
joblib.dump(model, "models/crowd_model.pkl")

# Save encoder
joblib.dump(encoder, "models/destination_encoder.pkl")

print("✅ Model trained successfully!")