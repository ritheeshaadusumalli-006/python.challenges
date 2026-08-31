# ===== Task 1: Create a Car class with brand and model =====
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Car Brand:", self.brand, "| Model:", self.model)

car1 = Car("Toyota", "Corolla")
car1.display()

print()

# ===== Task 2: Create a Student class storing name and marks =====
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name, "| Marks:", self.marks)

student1 = Student("Rithuu", 92)
student1.display()

print()

# ===== Task 3: Create an Employee class and display salary =====
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        print("Employee:", self.name, "| Salary: ₹", self.salary)

employee1 = Employee("Karthik", 45000)
employee1.display_salary()

print()

# ===== Task 4: Create a Rectangle class to calculate area =====
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

rect1 = Rectangle(10, 5)
print("Rectangle Area:", rect1.calculate_area())

print()

# ===== Task 5: Create a Circle class to calculate circumference =====
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_circumference(self):
        return 2 * 3.14159 * self.radius

circle1 = Circle(7)
print("Circle Circumference:", circle1.calculate_circumference())