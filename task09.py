from abc import ABC, abstractmethod

# ===== Task 1 & 2: Create a Person class, inherit a Student class, and override a method =====
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Person Name:", self.name, "| Age:", self.age)

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks

    def display(self):  # overriding the parent class method
        print("Student Name:", self.name, "| Age:", self.age, "| Marks:", self.marks)

student1 = Student("Rithuu", 20, 92)
student1.display()

print()

# ===== Task 3: Create a BankAccount class with a private balance =====
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.__balance

account1 = BankAccount("Rithuu", 5000)
account1.deposit(2000)
account1.withdraw(1000)
print("Account Owner:", account1.owner, "| Balance:", account1.get_balance())

print()

# ===== Task 4: Implement polymorphism using Car and Bike classes =====
class Car:
    def sound(self):
        print("Car goes Vroom Vroom!")

class Bike:
    def sound(self):
        print("Bike goes Brrrm Brrrm!")

for vehicle in (Car(), Bike()):
    vehicle.sound()  # same method name, different behavior (polymorphism)

print()

# ===== Task 5: Create an abstract class Vehicle with a start() method =====
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class ElectricVehicle(Vehicle):
    def start(self):
        print("Electric vehicle starts silently with a button press.")

ev = ElectricVehicle()
ev.start()