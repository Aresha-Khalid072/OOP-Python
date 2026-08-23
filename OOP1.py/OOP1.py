# Objects and Classes
from car import Car


car1= Car("BMW",2024,"Black", False)
car2= Car("Charger",2026,"Yellow", True)
print(car1.model)
print(car1.color)
print(car1.year)
print(car1.for_sale)

car2.stop()
car1.drive()
car1.describe()
car2.describe()
          