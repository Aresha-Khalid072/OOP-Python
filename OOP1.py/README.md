# OOP1 — Objects & Classes 🐍

This lesson covers the very first concept of Object-Oriented Programming in Python: **creating a class and making objects (instances) from it.**

## 📂 Files

- `car.py` — defines the `Car` class
- `OOP1.py` — creates `Car` objects and uses their attributes & methods

## 🧠 Concepts Covered

- Defining a class using `class`
- The `__init__()` constructor method
- Instance attributes (`self.model`, `self.year`, `self.color`, `self.for_sale`)
- Instance methods (`drive()`, `stop()`, `describe()`)
- Creating multiple objects from the same class
- Accessing object attributes and calling object methods

## 📄 Code

**car.py**
```python
class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")
```

**OOP1.py**
```python
from car import Car

car1 = Car("BMW", 2024, "Black", False)
car2 = Car("Charger", 2026, "Yellow", True)

print(car1.model)
print(car1.color)
print(car1.year)
print(car1.for_sale)

car2.stop()
car1.drive()
car1.describe()
car2.describe()
```

## ▶️ How to Run

```bash
python OOP1.py
```

## 📤 Sample Output

```
BMW
Black
2024
False
You stop the Yellow Charger
You drive the Black BMW
2024 Black BMW
2026 Yellow Charger
```

## 👤 Author

**Aresha Khalid**
GitHub: [@Aresha-Khalid072](https://github.com/Aresha-Khalid072)