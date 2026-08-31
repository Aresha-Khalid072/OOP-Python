# Polymorphism
# To hav many forms


from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 *self.radius **2

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height

    def area(self):
        return self.base*self.height*0.5

class Square(Shape):
    def __init__(self,side):
        self.side=side

    def area(self):
        return self.side **2


class Pizza(Circle):
    def __init__(self, radius,topping):
        # self.radius=radius
        super().__init__(radius)
        self.topping=topping

shapes=[Circle(4),Triangle(6,7),Square(5),Pizza(15,"peprooni")]


for shape in shapes:
    print(shape.area())