# Allows class to inherit attribute and methods from another class

class Animal:
    def __init__(self,name):
        self.name = name
        self.is_Alive =True


    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
          print(f"{self.name} is sleeping")


class Dog(Animal):
     def speak(self):
          print("WOOF!")


class Cat(Animal):
     def speak(self):
          print("MEOWWW!")


class Mouse(Animal):
      def speak(self):
               print("SQUEEK!")


dog=Dog("Scoby")
cat=Cat("Manoo")
mouse=Mouse("Mickey")


print(dog.name)
print(dog.is_Alive)
dog.sleep()
dog.eat()
dog.speak()