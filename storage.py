"""File handling: load and save student records as JSON."""
import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "students.json")


def load_students():
    """Return a dict {roll: record}. Returns {} if the file is missing or corrupt."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("! Data file is corrupted. Starting with an empty database.")
        return {}


def save_students(students):
    """Write all records to disk."""
    try:
        os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(students, f, indent=4)
        return True
    except OSError as err:
        print(f"! Could not save data: {err}")
        return False
