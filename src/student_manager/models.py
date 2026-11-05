"""Data models."""

from dataclasses import dataclass

from student_manager.config import MAX_GRADE, MIN_GRADE
from student_manager.exceptions import InvalidStudentDataError


@dataclass
class Student:
    """Student with basic academic information."""

    first_name: str
    last_name: str
    group: str
    average_grade: float

    def __post_init__(self) -> None:
        if not self.first_name.strip() or not self.last_name.strip():
            raise InvalidStudentDataError("Name and surname must not be empty.")
        if not self.group.strip():
            raise InvalidStudentDataError("Group must not be empty.")
        if not MIN_GRADE <= self.average_grade <= MAX_GRADE:
            raise InvalidStudentDataError(
                f"Average grade must be in range {MIN_GRADE}..{MAX_GRADE}."
            )

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
