"""Application entry point."""

import sys

from student_manager.config import DEFAULT_GROUP
from student_manager.exceptions import InvalidStudentDataError
from student_manager.models import Student
from student_manager.services import (
    add_student,
    calculate_group_average,
    filter_by_group,
    find_best_student,
    find_student,
    sort_by_grade,
)


def create_demo_students() -> list[Student]:
    """Create demo data."""
    return [
        Student("Anna", "Koval", "PI-21", 91.5),
        Student("Oleh", "Melnyk", "PI-21", 84.0),
        Student("Iryna", "Bondar", "PI-22", 95.2),
        Student("Andrii", "Shevchenko", "PI-21", 88.7),
    ]


def print_students(students: list[Student]) -> None:
    """Print students as a table."""
    print("\nStudents:")

    for student in students:
        print(
            f"{student.full_name:25}"
            f"{student.group:10}"
            f"{student.average_grade:6.2f}"
        )


def run_demo() -> None:
    """Non-interactive demonstration of all main operations."""
    students = create_demo_students()

    print_students(students)

    group = DEFAULT_GROUP
    group_students = filter_by_group(students, group)

    print(f"\nStudents of group {group}:")
    print_students(group_students)

    average = calculate_group_average(group_students)
    print(f"\nGroup average: {average:.2f}")

    best = find_best_student(students)
    if best is not None:
        print("\nBest student:", best.full_name, f"({best.average_grade:.2f})")

    student = find_student(students, "Melnyk")
    if student is not None:
        print("\nStudent found:", student.full_name, student.group)

    print("\nSorted by average grade (descending):")
    print_students(sort_by_grade(students))


def print_menu() -> None:
    """Print the menu."""
    print()
    print("1. Show all students")
    print("2. Find student")
    print("3. Show group")
    print("4. Show best student")
    print("5. Add student")
    print("6. Exit")


def read_new_student() -> Student:
    """Read a student from the keyboard with validation."""
    first_name = input("First name: ").strip()
    last_name = input("Last name: ").strip()
    group = input("Group: ").strip()
    grade_text = input("Average grade: ").strip().replace(",", ".")

    try:
        grade = float(grade_text)
    except ValueError as error:
        raise InvalidStudentDataError("Average grade must be a number.") from error

    return Student(first_name, last_name, group, grade)


def run_menu(students: list[Student]) -> None:
    """Menu-driven interface."""
    while True:
        print_menu()
        command = input("Select command: ").strip()

        if command == "1":
            print_students(students)

        elif command == "2":
            student = find_student(students, input("Last name: "))
            if student:
                print(student.full_name, student.group, student.average_grade)
            else:
                print("Student not found.")

        elif command == "3":
            print_students(filter_by_group(students, input("Group: ")))

        elif command == "4":
            best = find_best_student(students)
            if best:
                print("Best:", best.full_name, best.average_grade)

        elif command == "5":
            try:
                add_student(students, read_new_student())
                print("Student added.")
            except InvalidStudentDataError as error:
                print(f"Error: {error}")

        elif command == "6":
            print("Goodbye.")
            break

        else:
            print("Unknown command.")


def main() -> None:
    """Run demo by default or the menu with --menu."""
    if "--menu" in sys.argv[1:]:
        run_menu(create_demo_students())
    else:
        run_demo()


if __name__ == "__main__":
    main()
