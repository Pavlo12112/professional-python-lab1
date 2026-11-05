"""Business logic: operations over the list of students."""

from student_manager.models import Student


def add_student(students: list[Student], student: Student) -> None:
    """Add a student to the list."""
    students.append(student)


def calculate_group_average(students: list[Student]) -> float:
    """Return the average grade of the given students."""
    if not students:
        return 0.0

    total = sum(student.average_grade for student in students)

    return total / len(students)


def find_best_student(students: list[Student]) -> Student | None:
    """Return the student with the highest average grade."""
    if not students:
        return None

    return max(students, key=lambda student: student.average_grade)


def filter_by_group(students: list[Student], group: str) -> list[Student]:
    """Return students of the given group."""
    return [student for student in students if student.group == group]


def find_student(students: list[Student], last_name: str) -> Student | None:
    """Find a student by last name (case-insensitive)."""
    for student in students:
        if student.last_name.lower() == last_name.lower():
            return student

    return None


def search_students(
    students: list[Student],
    group: str | None = None,
    min_grade: float | None = None,
) -> list[Student]:
    """Search by several criteria: group and/or minimal average grade."""
    result = students

    if group is not None:
        result = filter_by_group(result, group)

    if min_grade is not None:
        result = [s for s in result if s.average_grade >= min_grade]

    return result


def sort_by_grade(
    students: list[Student], descending: bool = True
) -> list[Student]:
    """Return a new list sorted by average grade."""
    return sorted(
        students,
        key=lambda student: student.average_grade,
        reverse=descending,
    )
