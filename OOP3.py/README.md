# 🐕 Python Basic Inheritance Demo

A simple Python project demonstrating **single inheritance** in object-oriented programming — showing how a child class can inherit attributes and methods from a parent class, while also defining its own unique behavior.

## Overview

This project defines a base `Animal` class with shared attributes (`name`, `is_Alive`) and shared methods (`eat()`, `sleep()`). Three subclasses — `Dog`, `Cat`, and `Mouse` — inherit all of this shared functionality from `Animal`, while each defining its own unique `speak()` method.

## Class Hierarchy

```
Animal
├── Dog
├── Cat
└── Mouse
```

- `Animal` — base class with:
  - `name` and `is_Alive` attributes
  - `eat()` and `sleep()` methods
- `Dog`, `Cat`, `Mouse` — each inherits from `Animal` and adds a unique `speak()` method

## Features

- Demonstrates **single inheritance** (child classes inheriting from one parent)
- Demonstrates **method overriding/extension** (`speak()` is unique to each subclass)
- Shows how inherited methods and attributes remain accessible in child classes
- Clean, minimal example ideal for learning core OOP concepts

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
   python3 animals.py
   ```

## Example Output

```
Scoby
True
Scoby is sleeping
Scoby is eating
WOOF!
```

## Class Behavior Summary

| Class | Inherits From | Unique Method | Sound |
|-------|---------------|----------------|-------|
| `Animal` | — | — | — |
| `Dog` | `Animal` | `speak()` | WOOF! |
| `Cat` | `Animal` | `speak()` | MEOWWW! |
| `Mouse` | `Animal` | `speak()` | SQUEEK! |

## Project Structure

```
.
├── Inheritance.py     # Animal class hierarchy and demo usage
└── README.md      # Project documentation
```

## Possible Future Enhancements

- Add more animals and behaviors (e.g. `Bird`, `Fish`)
- Add a `describe()` method to print a full summary of each animal
- Add input validation (e.g. prevent empty names)
- Track and toggle `is_Alive` status with methods (e.g. simulate aging)
- Add unit tests for inherited behavior

## License

This project is open source and available for personal or educational use.