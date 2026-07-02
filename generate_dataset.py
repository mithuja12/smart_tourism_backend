import pandas as pd
import random

# Tourist destinations in Kodaikanal
destinations = {
    "Coaker's Walk": 30,
    "Bryant Park": 28,
    "Silver Cascade Falls": 25,
    "Guna Caves": 27,
    "Pine Forest": 22,
}

rows = []

for _ in range(5000):

    # Select a random tourist destination
    destination = random.choice(list(destinations.keys()))

    # Popularity score (higher = usually more crowded)
    popularity = destinations[destination]

    # Features
    hour = random.randint(6, 20)
    weekend = random.choice([0, 1])
    temperature = random.randint(15, 30)
    humidity = random.randint(50, 95)

    # Synthetic crowd calculation
    crowd = (
        popularity
        + (hour * 2)
        + (weekend * 20)
        + temperature
        + (humidity * 0.2)
        + random.randint(-8, 8)
    )

    # Keep crowd percentage between 5 and 100
    crowd = max(5, min(100, int(crowd)))

    rows.append([
        destination,
        hour,
        weekend,
        temperature,
        humidity,
        crowd
    ])

# Create DataFrame
df = pd.DataFrame(
    rows,
    columns=[
        "destination",
        "hour",
        "weekend",
        "temperature",
        "humidity",
        "crowd"
    ]
)

# Save dataset
df.to_csv("data/crowd_data.csv", index=False)

print("Dataset generated successfully!")