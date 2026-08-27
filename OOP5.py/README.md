# 🔺 Python Shapes (OOP Inheritance Demo)

A simple Python project demonstrating core object-oriented programming concepts — class inheritance, `super()` calls, and method overriding — using geometric shapes as an example.

## Overview

This project defines a base `Shape` class with common attributes (`color`, `is_filled`) and a `describe()` method. Three subclasses — `Circle`, `Square`, and `Triangle` — inherit from `Shape`, add their own unique attributes (radius, width, height), and override `describe()` to:

1. Call the parent class's `describe()` via `super()` (to print the shared color/fill info)
2. Print shape-specific details, including the calculated area

## Features

- Demonstrates **inheritance** (`Circle`, `Square`, `Triangle` all extend `Shape`)
- Demonstrates **method overriding** with `super()` calls to reuse parent logic
- Calculates and displays the area of each shape
- Clean, readable output describing each shape's properties

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
   python3 shapes.py
   ```

## Example Output

```
It is blue and filled
It is a circle with area of 78.5cm ^2
It is red and filled
It is a square with area of 36cm ^2
It is green and not filled
It is a triangle with area of 6.0cm ^2
```

## Class Structure

| Class | Inherits From | Unique Attributes | Area Formula |
|-------|---------------|--------------------|--------------|
| `Shape` | — | `color`, `is_filled` | — |
| `Circle` | `Shape` | `radius` | `π × r²` |
| `Square` | `Shape` | `width` | `width × width` |
| `Triangle` | `Shape` | `width`, `height` | `0.5 × width × height` |

## Project Structure

```
.
├── super.py     # Shape classes and demo usage
└── README.md     # Project documentation
```

## Possible Future Enhancements

- Add more shapes (Rectangle, Pentagon, etc.)
- Add input validation (e.g. reject negative dimensions)
- Add a `perimeter()` method alongside area calculation
- Use `__str__`/`__repr__` for cleaner object printing
- Add unit tests for area calculations

## License

This project is open source and available for personal or educational use.