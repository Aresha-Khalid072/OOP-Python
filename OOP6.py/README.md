# Polymorphism in Python (OOP Example)

A demonstration of **polymorphism** using an abstract base class `Shape` and several subclasses that each implement `area()` in their own way.

## Concept

Polymorphism means "many forms" — different classes can share the same method name (`area()`), but each implements the behavior differently depending on the shape. This lets you loop over a list of different shape objects and call `.area()` on each one without caring what specific type it is.

## Classes

- **`Shape`** (abstract base class) — defines the `area()` method as abstract, meaning every subclass *must* implement it. It cannot be instantiated directly.
- **`Circle`** — takes a `radius`, area = π × r²
- **`Triangle`** — takes `base` and `height`, area = ½ × base × height
- **`Square`** — takes a `side`, area = side²
- **`Pizza`** — inherits from `Circle` (a pizza is round!), adds a `topping` attribute on top of the radius

## Requirements

- Python 3.x (uses the built-in `abc` module — no external installs needed)

## Usage

```bash
python Polymorphism.py
```

Expected output:

```
50.24
21.0
25
706.5
```


## Notes

- Because `Shape` is abstract, trying to run `Shape()` directly will raise: `TypeError: Can't instantiate abstract class Shape with abstract method area`
- `Pizza` reuses `Circle`'s `area()` method via inheritance — it doesn't need to redefine `area()` itself.