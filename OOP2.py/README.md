# 🎓 Python Class Variables vs Instance Variables

A simple Python project demonstrating the difference between **class variables** (shared across all instances) and **instance variables** (unique to each object), using a `Student` class as an example.

## Overview

This project defines a `Student` class with:

- **Class variables** (`class_year`, `num_students`) — defined outside the constructor, shared by every instance of the class.
- **Instance variables** (`name`, `age`) — defined inside `__init__`, unique to each individual student object.

A class variable (`num_students`) is also automatically incremented every time a new `Student` object is created, demonstrating how class-level state can track information across all instances.

## Key Concepts Demonstrated

- **Class variables** are defined at the class level (outside `__init__`) and shared by all instances — changing them via the class affects every object.
- **Instance variables** are defined inside `__init__` using `self` — each object gets its own independent copy.
- Class variables can be accessed either through an instance (`student1.class_year`) or directly through the class (`Student.class_year`).
- Updating a class variable via `Student.num_students += 1` inside the constructor lets the class keep a running count of how many instances have been created.

## Requirements

- Python 3.6+

No external dependencies required.

## Installation

1. Clone or download this repository.
2. Ensure Python 3 is installed:
   ```bash
   python3 --version
   ```
3. Run the script:
   ```bash
   python3 student.py
   ```

## Example Output

```
Aresha
22
2024
Kris
21
2024
3
My graduating class of 2024 has 3 students
Aresha
Kris
Sandy
```

## Class Structure

| Variable | Type | Shared? | Example Value |
|----------|------|---------|----------------|
| `class_year` | Class variable | Yes (same for all students) | `2024` |
| `num_students` | Class variable | Yes (auto-updates on creation) | `3` (after 3 students created) |
| `name` | Instance variable | No (unique per student) | `"Aresha"`, `"Kris"`, `"Sandy"` |
| `age` | Instance variable | No (unique per student) | `22`, `21`, `23` |

## Project Structure

```
.
├── classVariables.py     # Student class with class/instance variable demo
└── README.md      # Project documentation
```

## Possible Future Enhancements

- Add a `describe()` method to print a full student summary
- Add a method to update `class_year` for graduating classes
- Add validation (e.g. prevent negative ages)
- Track students in a list at the class level for iteration
- Add unit tests to confirm shared vs unique variable behavior

## License

This project is open source and available for personal or educational use.