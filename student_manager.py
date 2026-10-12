"""CRUD operations for student records."""
import storage
import validators as v


def calculate_grade(average):
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 50:
        return "D"
    return "F"


def _build_result(marks):
    total = round(sum(marks.values()), 2)
    average = round(total / len(marks), 2)
    return total, average, calculate_grade(average)


def add_student(students):
    print("\n--- Add Student ---")
    roll = v.get_roll("Roll number: ")
    if roll in students:
        print("  ! A student with this roll number already exists.")
        return
    name = v.get_name("Name: ")
    age = v.get_int("Age (5-100): ", 5, 100)
    course = v.get_text("Course/Class: ")
    marks = {subject: v.get_marks(subject) for subject in v.SUBJECTS}
    total, average, grade = _build_result(marks)
    students[roll] = {
        "roll": roll, "name": name, "age": age, "course": course,
        "marks": marks, "total": total, "average": average, "grade": grade,
    }
    if storage.save_students(students):
        print(f"  Student {name} added successfully. Grade: {grade}")


def update_student(students):
    print("\n--- Update Student ---")
    roll = v.get_roll("Roll number to update: ")
    student = students.get(roll)
    if not student:
        print("  ! Student not found.")
        return
    print("  (Press Enter to keep the current value)")
    name = v.get_name(f"Name [{student['name']}]: ", allow_blank=True)
    age = v.get_int(f"Age [{student['age']}]: ", 5, 100, allow_blank=True)
    course = v.get_text(f"Course [{student['course']}]: ", allow_blank=True)
    if name:
        student["name"] = name
    if age is not None:
        student["age"] = age
    if course:
        student["course"] = course
    for subject in v.SUBJECTS:
        new = v.get_marks(f"{subject} [{student['marks'][subject]}]", allow_blank=True)
        if new is not None:
            student["marks"][subject] = new
    student["total"], student["average"], student["grade"] = _build_result(student["marks"])
    if storage.save_students(students):
        print("  Student updated successfully.")


def delete_student(students):
    print("\n--- Delete Student ---")
    roll = v.get_roll("Roll number to delete: ")
    if roll not in students:
        print("  ! Student not found.")
        return
    confirm = input(f"  Delete {students[roll]['name']}? (y/n): ").strip().lower()
    if confirm == "y":
        del students[roll]
        if storage.save_students(students):
            print("  Student deleted.")
    else:
        print("  Deletion cancelled.")


def display_student(s):
    print(f"\n  Roll: {s['roll']} | Name: {s['name']} | Age: {s['age']} | Course: {s['course']}")
    for subject, mark in s["marks"].items():
        print(f"    {subject:<10}: {mark}")
    print(f"  Total: {s['total']} | Average: {s['average']} | Grade: {s['grade']}")


def search_student(students):
    print("\n--- Search Student ---")
    query = v.get_text("Enter roll number or name: ").lower()
    matches = [s for s in students.values()
               if query == s["roll"].lower() or query in s["name"].lower()]
    if not matches:
        print("  No matching students found.")
        return
    for s in matches:
        display_student(s)


def list_students(students):
    print("\n--- All Students ---")
    if not students:
        print("  No records available.")
        return
    print(f"  {'Roll':<8}{'Name':<22}{'Course':<14}{'Avg':>7}{'Grade':>7}")
    print("  " + "-" * 58)
    for s in sorted(students.values(), key=lambda x: x["roll"]):
        print(f"  {s['roll']:<8}{s['name']:<22}{s['course']:<14}{s['average']:>7}{s['grade']:>7}")
