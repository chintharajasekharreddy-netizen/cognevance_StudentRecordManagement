"""Student Record Management System - menu-driven entry point."""
import storage
import student_manager as sm
import reports

MENU = """
=========================================
     STUDENT RECORD MANAGEMENT SYSTEM
=========================================
 1. Add Student
 2. Update Student
 3. Delete Student
 4. Search Student
 5. View All Students
 6. Performance Report
 7. Exit
"""


def main():
    students = storage.load_students()
    actions = {
        "1": sm.add_student,
        "2": sm.update_student,
        "3": sm.delete_student,
        "4": sm.search_student,
        "5": sm.list_students,
        "6": reports.performance_report,
    }
    while True:
        print(MENU)
        try:
            choice = input("Enter your choice (1-7): ").strip()
            if choice == "7":
                print("Goodbye!")
                break
            action = actions.get(choice)
            if action:
                action(students)
            else:
                print("! Invalid choice. Please select 1-7.")
        except (KeyboardInterrupt, EOFError):
            print("\nExiting safely. Goodbye!")
            break
        except Exception as err:  # last-resort safety net
            print(f"! Unexpected error: {err}")


if __name__ == "__main__":
    main()
