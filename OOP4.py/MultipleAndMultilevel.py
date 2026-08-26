# Multiple
# child can inherit from multiple parents


# Multilevel 
# inherit from a parent which has inherit from another parent



class Animal:
    def eat(self):
        print("this animal is eating")

    def sleep(self):
        print("this animal is sleeping")

class Prey(Animal):
    def flee(self):
        print("This animal is fleeing")

      

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")
        
     


class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass


# inherit from more than one parent multiple inheritance

class Fish(Prey,Predator):
    pass

rabbit = Rabbit()
hawk =Hawk()
fish = Fish()

rabbit.flee()
rabbit.sleep()
hawk.hunt()
hawk.eat()
fish.flee()
fish.hunt()
fish.sleep()
fish.eat()