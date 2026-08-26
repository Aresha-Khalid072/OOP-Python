# 🐾 Python Inheritance Demo (Multilevel & Multiple Inheritance)

A simple Python project demonstrating two key object-oriented inheritance patterns — **multilevel inheritance** and **multiple inheritance** — using an animal classification example.

## Overview

This project models a small animal hierarchy to show how classes can inherit behavior from one or more parent classes:

- **Multilevel inheritance**: A class inherits from a parent, which itself inherits from another parent (a chain of inheritance).
- **Multiple inheritance**: A class inherits directly from more than one parent class at the same time.

## Class Hierarchy

```
Animal
├── Prey
│   └── Rabbit
├── Predator
│   └── Hawk
└── Fish (inherits from BOTH Prey and Predator)
```

- `Animal` — base class with shared behavior: `eat()`, `sleep()`
- `Prey` — inherits from `Animal`, adds `flee()`
- `Predator` — inherits from `Animal`, adds `hunt()`
- `Rabbit` — inherits from `Prey` (multilevel: Rabbit → Prey → Animal)
- `Hawk` — inherits from `Predator` (multilevel: Hawk → Predator → Animal)
- `Fish` — inherits from **both** `Prey` and `Predator` (multiple inheritance), gaining access to `flee()`, `hunt()`, `eat()`, and `sleep()`

## Features

- Demonstrates **multilevel inheritance** (`Rabbit`, `Hawk`)
- Demonstrates **multiple inheritance** (`Fish`)
- Shows Python's Method Resolution Order (MRO) in action
- Clean, minimal example ideal for learning OOP concepts

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
   python3 inheritance.py
   ```

## Example Output

```
This animal is fleeing
this animal is sleeping
This animal is hunting
this animal is eating
This animal is fleeing
This animal is hunting
this animal is sleeping
this animal is eating
```

## Method Resolution Order (MRO)

Since `Fish` inherits from both `Prey` and `Predator`, Python resolves method lookups using its Method Resolution Order (C3 linearization). You can inspect it with:

```python
print(Fish.__mro__)
```

Output:
```
(<class 'Fish'>, <class 'Prey'>, <class 'Predator'>, <class 'Animal'>, <class 'object'>)
```

## Project Structure

```
.
├── MultipleAndMultilevel.py    # Animal class hierarchy and demo usage
└── README.md         # Project documentation
```

## Possible Future Enhancements

- Add more animal types and behaviors (e.g. `Omnivore`, `Scavenger`)
- Add a `__str__` method to print readable animal descriptions
- Demonstrate method overriding conflicts and how MRO resolves them
- Add unit tests to verify inheritance behavior

## License

This project is open source and available for personal or educational use.