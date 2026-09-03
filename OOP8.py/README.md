# Static Methods vs Class Methods in Python

A comparison of **static methods** and **class methods** using two example classes: `Employee` and `Student`.

## Concept

- **Instance methods** — operate on a specific object (`self`). Best for logic tied to one instance's data.
- **Static methods** (`@staticmethod`) — belong to the class but don't need access to the class or its instances. Best for utility/helper functions that are logically related to the class but don't touch its data.
- **Class methods** (`@classmethod`) — take `cls` instead of `self`, and operate on class-level data shared across all instances (like counters or totals).

## Employee — Static Method Example

- `is_valid_pos(position)` is a `@staticmethod` — it checks if a job title is valid against a fixed list, without needing any specific `Employee` object's data.
- `get_info()` is a normal instance method — it needs `self.name` and `self.position`, which only exist on a specific object.

## Student — Class Method Example

- `count` and `total_gpa` are **class-level attributes**, shared across every `Student` instance.
- Every time a new `Student` is created, `__init__` increments `Student.count` and adds to `Student.total_gpa`.
- `get_count()` and `get_avg_gpa()` are `@classmethod`s — they report on the class as a whole (total students, average GPA), not on any single student.

## Usage

```bash
python staticClassMethods.py
```

Expected output:

```
True
False
 Aresha= CEO
 Ali= PA
Total no. of students is 2
3.68
```

## Key Takeaway

Use `@staticmethod` when the function is related to the class but doesn't need `self` or `cls`. Use `@classmethod` when the function needs to read or modify data shared across all instances of the class.