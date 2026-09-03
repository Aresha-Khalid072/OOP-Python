# Python `@property` Decorator — Getter, Setter, and Deleter

A demonstration of the `@property` decorator using a `Rectangle` class, showing how to control attribute access with validation and cleanup logic.

## Overview

The `@property` decorator lets a method be accessed like a plain attribute (`obj.width`) while still running custom logic behind the scenes. It provides three complementary decorators:

| Decorator | Purpose | Triggered by |
|---|---|---|
| `@property` | Getter — defines how the attribute is *read* | `rectangle.width` |
| `@width.setter` | Setter — defines how the attribute is *written*, with validation | `rectangle.width = 5` |
| `@width.deleter` | Deleter — defines cleanup logic when the attribute is *deleted* | `del rectangle.width` |

This pattern is the Pythonic alternative to writing explicit `get_width()` / `set_width()` methods, while still allowing validation (e.g., rejecting non-positive dimensions).

## Class: `Rectangle`

- Stores width and height internally as `_width` and `_height` (the leading underscore signals these are "private" and shouldn't be accessed directly).
- **Getter** (`width`, `height`) — returns the value formatted as a string with one decimal place and a `cm` unit (e.g., `"3.0cm"`).
- **Setter** (`width`, `height`) — only updates the value if it's greater than `0`; otherwise prints a warning and leaves the value unchanged.
- **Deleter** (`width`, `height`) — deletes the underlying attribute and prints a confirmation message.

## Requirements

- Python 3.x (no external dependencies)

## Usage

```bash
python propertymethod.py
```

### Example Behavior

```python
rectangle = Rectangle(3, 4)

rectangle.width = 5      # passes validation, updates _width
rectangle.height = 3     # passes validation, updates _height

del rectangle.width      # prints "Width has been deleted"
del rectangle.height     # prints "Height has been deleted"

print(rectangle.width)   # would raise AttributeError — _width no longer exists
```

## Key Takeaway

`@property` lets you expose attributes with a clean, attribute-style syntax (`obj.width`) while enforcing validation rules and controlling deletion behavior — all without changing how the attribute is used from the outside.