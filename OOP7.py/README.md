# Duck Typing in Python

A quick example of **duck typing** — polymorphism achieved without shared inheritance.

## Concept

> "If it looks like a duck and quacks like a duck, it's a duck."

Python doesn't care what class an object belongs to — only whether it has the method or attribute you're trying to use. `Dog` and `Cat` share a parent class (`Animal`), but `Car` doesn't inherit from `Animal` at all. It still works in the loop below because it defines its own `speak()` method and `alive` attribute.

## Classes

- **`Animal`** — base class with `alive=True`
- **`Dog`** / **`Cat`** — inherit from `Animal`, each define their own `speak()`
- **`Car`** — a completely unrelated class, but defines `speak()` and `alive` on its own

## Usage

```bash
python DuckTyping.py
```

Expected output:

```
WOOF!
True
MEOWWW!
True
HONK!
False
```

## Key Takeaway

Polymorphism doesn't require inheritance. As long as an object has the method being called, Python will call it — regardless of the object's class hierarchy.