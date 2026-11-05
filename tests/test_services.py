"""Unit tests for services and model validation."""

import unittest

from student_manager.exceptions import InvalidStudentDataError
from student_manager.models import Student
from student_manager.services import (
    calculate_group_average,
    filter_by_group,
    find_best_student,
    find_student,
    search_students,
    sort_by_grade,
)

DATA = [
    Student("Anna", "Koval", "PI-21", 90.0),
    Student("Oleh", "Melnyk", "PI-21", 80.0),
    Student("Iryna", "Bondar", "PI-22", 95.0),
]


class ServicesTest(unittest.TestCase):
    def test_average(self) -> None:
        self.assertEqual(
            calculate_group_average(filter_by_group(DATA, "PI-21")), 85.0
        )
        self.assertEqual(calculate_group_average([]), 0.0)

    def test_best(self) -> None:
        best = find_best_student(DATA)
        self.assertIsNotNone(best)
        self.assertEqual(best.last_name, "Bondar")
        self.assertIsNone(find_best_student([]))

    def test_find_and_search(self) -> None:
        self.assertEqual(find_student(DATA, "melnyk").first_name, "Oleh")
        self.assertIsNone(find_student(DATA, "none"))
        self.assertEqual(
            len(search_students(DATA, group="PI-21", min_grade=85)), 1
        )

    def test_sort(self) -> None:
        self.assertEqual(sort_by_grade(DATA)[0].last_name, "Bondar")

    def test_validation(self) -> None:
        with self.assertRaises(InvalidStudentDataError):
            Student("A", "B", "PI-21", 150.0)


if __name__ == "__main__":
    unittest.main()
