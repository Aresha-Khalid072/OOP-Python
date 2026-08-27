# function used in child class
# call methods from parent class


class Shape:
      def __init__(self,color,is_filled):
            self.color = color
            self.is_filled = is_filled

      def describe(self):
            print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")



class Circle(Shape):
    def __init__(self,color,is_filled,radius):
        super().__init__(color,is_filled)

        self.radius = radius

    def describe(self):
         super().describe()
         print(f"It is a circle with area of {3.14 * self.radius *self.radius}cm ^2")

class Square(Shape):
    def __init__(self,color,is_filled,width):
            super().__init__(color,is_filled)

            self.width = width

    def describe(self):
         super().describe()
         print(f"It is a square with area of {self.width * self.width}cm ^2")

class Triangle(Shape):
    def __init__(self,color,is_filled,width,height):
                super().__init__(color,is_filled)

                self.width = width
                self.height=height

    def describe(self):
         super().describe()
         print(f"It is a triangle with area of {0.5 * self.width * self.height}cm ^2")



circle=Circle(color="blue",is_filled=True,radius=5)
square=Square(color="red",is_filled=True,width=6)
triangle=Triangle(color="green",is_filled=False,width=4,height=3)

circle.describe()
square.describe()
triangle.describe()