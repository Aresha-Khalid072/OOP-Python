#static method is a method that belongs to a class rather than any object from that class
# instance methods best for operations on instances of class (objects)
# static methods best for utility functions thatt do not need to access class data


class Employee:
    def __init__(self, name,position):
        self.name=name
        self.position=position

    def get_info(self):
        return f" {self.name}= {self.position}"

    @staticmethod
    def is_valid_pos(position):
        valid_pos=["Manager","Cook","Cashier"]
        return position in valid_pos



print(Employee.is_valid_pos("Cook"))
print(Employee.is_valid_pos("Scientist"))

employee1=Employee("Aresha", "CEO")
employee2=Employee("Ali","PA")
print(employee1.get_info())
print(employee2.get_info())



# Class methods
# best for class level data
# Allow operations related to the class itself
class Student:

    count=0
    total_gpa=0

    def __init__(self,name,gpa):
        self.name= name
        self.gpa=gpa
        Student.count +=1
        Student.total_gpa +=gpa



    # Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"


    # class methods
    @classmethod
    def get_count(cls):
        return f"Total no. of students is {cls.count}"


    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa/cls.count:.2f}"




student1= Student("Aresha",3.46)
student2=Student("Ali",3.9)
print(Student.get_count())

print(Student.get_avg_gpa())


        


    