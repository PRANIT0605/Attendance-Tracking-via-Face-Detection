from dotenv import load_dotenv
import firebase_admin
import os
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")


load_dotenv("sensitive.env")  # This loads the .env file into environment variables
database_url = os.getenv("DATABASE_URL")
storage_bucket_url = os.getenv("STORAGE_BUCKET_URL")
ref = db.reference('Students')
data = {
    "134052":
        {
            "name": "Elon Musk",
            "major": "Robotics",
            "starting_year": 2017,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-07 00:54:34"
        },
    "145356":
        {
            "name": "Robert Oppenheimer",
            "major": "Astrophysics",
            "starting_year": 1972,
            "total_attendance": 42,
            "standing": "A",
            "year": 6,
            "last_attendance_time": "2023-07-05 00:33:44"
        },
    "334256":
        {
            "name": "Pranit Gore",
            "major": "CS",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-06-05 00:05:30"
        }
}

for key, value in data.items():
    ref.child(key).set(value)