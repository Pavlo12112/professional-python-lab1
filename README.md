# Student Manager

Laboratory project for the course
"Professional Python".

## Description

Console application for managing students
and calculating academic statistics.

## Requirements

Python 3.11+

## Installation

    python -m venv .venv

Activate the virtual environment
(Windows: `.venv\Scripts\activate`, Linux/macOS: `source .venv/bin/activate`).

    python -m pip install -e .

## Run

    python -m student_manager.main

Interactive menu:

    python -m student_manager.main --menu

or

    student-manager

## Example output

    Students of group PI-21:
    Anna Koval                PI-21      91.50
    Oleh Melnyk               PI-21      84.00
    Andrii Shevchenko         PI-21      88.70

    Group average: 88.07
    Best student: Iryna Bondar (95.20)

## Project structure

- `src/student_manager/models.py` - data models (`Student`).
- `src/student_manager/services.py` - business logic.
- `src/student_manager/config.py` - configuration constants.
- `src/student_manager/exceptions.py` - custom exception.
- `src/student_manager/main.py` - application entry point.
- `tests/` - automated tests.

## Author

Student: Tsiastun Pavlo
Group: FeP-33s
