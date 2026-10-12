"""Input validation helpers."""
import re

SUBJECTS = ["Maths", "Science", "English", "Computer", "History"]


def get_text(prompt, allow_blank=False):
    """Ask for a non-empty text value."""
    while True:
        value = input(prompt).strip()
        if value or allow_blank:
            return value
        print("  ! This field cannot be empty.")


def get_name(prompt, allow_blank=False):
    while True:
        value = input(prompt).strip()
        if not value and allow_blank:
            return value
        if re.fullmatch(r"[A-Za-z][A-Za-z .'-]{1,49}", value):
            return value.title()
        print("  ! Enter a valid name (letters only, 2-50 characters).")


def get_int(prompt, minimum, maximum, allow_blank=False):
    """Ask for an integer in [minimum, maximum]."""
    while True:
        raw = input(prompt).strip()
        if not raw and allow_blank:
            return None
        try:
            number = int(raw)
        except ValueError:
            print("  ! Please enter a whole number.")
            continue
        if minimum <= number <= maximum:
            return number
        print(f"  ! Value must be between {minimum} and {maximum}.")


def get_marks(subject, allow_blank=False):
    """Ask for marks (0-100) for one subject."""
    while True:
        raw = input(f"  Marks in {subject} (0-100): ").strip()
        if not raw and allow_blank:
            return None
        try:
            marks = float(raw)
        except ValueError:
            print("  ! Please enter a number.")
            continue
        if 0 <= marks <= 100:
            return round(marks, 2)
        print("  ! Marks must be between 0 and 100.")


def get_roll(prompt):
    while True:
        value = input(prompt).strip().upper()
        if re.fullmatch(r"[A-Z0-9]{2,10}", value):
            return value
        print("  ! Roll number must be 2-10 letters/digits (e.g. S101).")
