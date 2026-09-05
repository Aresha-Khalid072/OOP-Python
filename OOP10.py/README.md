# Python Decorators — Ice Cream Example

A demonstration of **decorators**, using a fun ice-cream analogy where toppings (`sprinkles`, `fudge`) are added on top of a base function without modifying it.

## Concept

A decorator is a function that wraps another function to extend its behavior — without changing the original function's source code. The base function is passed *into* the decorator as an argument, wrapped inside a new function, and returned. This wrapped version replaces the original when called.

Multiple decorators can be **stacked**, applied from the closest to the function outward.

## How It Works

- **`add_sprinkles(func)`** — wraps `func`, printing a sprinkles message before calling it.
- **`add_fudge(func)`** — wraps `func`, printing a fudge message before calling it.
- **`get_ice_cream(flavour)`** — the base function, decorated with both `@add_sprinkles` and `@add_fudge`.

### Order of Execution

```python
@add_sprinkles
@add_fudge
def get_ice_cream(flavour):
    ...
```

Decorators apply bottom-up, so the call order becomes:

```
add_sprinkles(add_fudge(get_ice_cream))
```

This means `add_fudge` wraps the original function first, and `add_sprinkles` wraps that result — so **sprinkles print first**, then **fudge**, then the base function runs.

## Requirements

- Python 3.x (no external dependencies)

## Usage

```bash
python decorator.py
```

### Expected Output

```
Here is your sprinkles 🎊
Here is your fudge added🍫
Here is your vanilla ice cream 🍦
```

## Key Takeaway

`*args` and `**kwargs` in the `wrapper` function let the decorator work with *any* function signature, forwarding whatever arguments were passed in (here, `flavour`) straight through to the original function.