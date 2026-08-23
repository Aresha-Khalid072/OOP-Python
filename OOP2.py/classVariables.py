# shared among all instances of class
# defined outside the constructor


class Student:

#    class variables
    class_year = 2024 
    num_students = 0





    # these are instance variables
    def __init__(self, name,age):  
        self.name=name
        self.age=age
        Student.num_students += 1


student1= Student("Aresha",22) 
student2=Student("Kris",21)
student3=Student("Sandy",23)

print(student1.name)
print(student1.age)
print(student1.class_year)


print(student2.name)
print(student2.age)
# directly accessing from class
print(Student.class_year)



print(Student.num_students)


print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)