import pandas as pd
import random

destinations = [
    "Kodaikanal",
    "Ooty",
    "Munnar",
    "Coorg",
    "Yercaud"
]

rows = []

for _ in range(5000):

    destination = random.choice(destinations)

    hour = random.randint(6, 20)

    weekend = random.choice([0, 1])

    temperature = random.randint(15, 30)

    humidity = random.randint(50, 95)

    # Crowd calculation (synthetic target)
    crowd = (
        hour * 3
        + weekend * 20
        + temperature * 1.5
        + humidity * 0.4
        + random.randint(-10, 10)
    )

    crowd = max(5, min(100, int(crowd)))

    rows.append([
        destination,
        hour,
        weekend,
        temperature,
        humidity,
        crowd
    ])

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

df.to_csv("data/crowd_data.csv", index=False)

print("Dataset generated successfully!")