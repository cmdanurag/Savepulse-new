import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta
from pathlib import Path

fake = Faker()

# CONFIGURATION

NUM_HOSPITALS = 50
NUM_USERS = 200

LAT_MIN, LAT_MAX = 22.45, 22.65
LON_MIN, LON_MAX = 88.25, 88.45

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# HOSPITAL NAME GENERATION

prefixes = [
    "CityCare","Sunrise","GreenLife","MetroCare","Apollo Care",
    "Mediview","Hopewell","Silver Oak","Zenith","LifeLine",
    "Global","Harmony","Prime","Medico","VitalCare"
]

suffixes = [
    "Hospital",
    "Medical Center",
    "Multispeciality Hospital",
    "Healthcare",
    "Medical Institute"
]

# HOSPITAL DATA GENERATION

hospitals = []

for i in range(1, NUM_HOSPITALS + 1):

    # hospital size distribution
    size_category = random.choices(
        ["small","medium","large"],
        weights=[0.3,0.5,0.2]
    )[0]

    if size_category == "small":
        total_beds = random.randint(40,80)
    elif size_category == "medium":
        total_beds = random.randint(80,150)
    else:
        total_beds = random.randint(150,300)

    icu_beds = random.randint(1, max(3, total_beds // 20))
    general_beds = random.randint(5, max(10, total_beds // 5))
    oxygen_beds = random.randint(3, max(8, total_beds // 10))

    hospital = {
        "hospital_id": i,
        "hospital_name": random.choice(prefixes) + " " + random.choice(suffixes),

        "latitude": round(random.uniform(LAT_MIN, LAT_MAX),6),
        "longitude": round(random.uniform(LON_MIN, LON_MAX),6),

        "trauma_center": random.random() < 0.35,
        "cardiac_center": random.random() < 0.50,

        "icu_beds_available": icu_beds,
        "general_beds_available": general_beds,
        "oxygen_beds_available": oxygen_beds,

        "total_beds": total_beds,

        "current_occupancy_rate": round(random.uniform(0.65,0.95),2),

        "hospital_rating": round(random.uniform(3.4,4.8),1)
    }

    hospitals.append(hospital)

hospital_df = pd.DataFrame(hospitals)

# USER REQUEST GENERATION

emergency_types = ["general","cardiac","trauma"]
severity_levels = ["CRITICAL","URGENT","STABLE"]

users = []

for i in range(1, NUM_USERS + 1):

    timestamp = datetime.now() - timedelta(minutes=random.randint(0,1440))

    users.append({
        "request_id": i,
        "user_id": random.randint(1,100),

        "latitude": round(random.uniform(LAT_MIN, LAT_MAX),6),
        "longitude": round(random.uniform(LON_MIN, LON_MAX),6),

        "emergency_type": random.choices(
            emergency_types,
            weights=[0.5,0.3,0.2]
        )[0],

        "severity_level": random.choices(
            severity_levels,
            weights=[0.3,0.4,0.3]
        )[0],

        "request_timestamp": timestamp
    })

user_df = pd.DataFrame(users)

# SAVE CSV FILES

hospital_file = DATA_DIR / "hospitals.csv"
users_file = DATA_DIR / "users.csv"

hospital_df.to_csv(hospital_file, index=False)
user_df.to_csv(users_file, index=False)

print("Datasets generated successfully")
print(f"Hospitals -> {hospital_file}")
print(f"Users -> {users_file}")