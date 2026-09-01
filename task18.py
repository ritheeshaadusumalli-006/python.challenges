# ===== Task 1: Create a class using type() =====
MyClass = type("MyClass", (), {})
obj1 = MyClass()
print("Task 1: Created class using type():", MyClass)
print("Task 1: Object of MyClass:", obj1)

print()

# ===== Task 2: Add attributes dynamically using type() =====
MyClassWithAttrs = type("MyClassWithAttrs", (), {"brand": "Toyota", "model": "Corolla"})
obj2 = MyClassWithAttrs()
print("Task 2: Brand:", obj2.brand)
print("Task 2: Model:", obj2.model)

print()

# ===== Task 3: Add methods dynamically =====
def display(self):
    print(f"Car: {self.brand} {self.model}")

MyClassWithMethod = type("MyClassWithMethod", (), {"brand": "Honda", "model": "Civic", "display": display})
obj3 = MyClassWithMethod()
obj3.display()

print()

# ===== Task 4: Create a metaclass that prints a message whenever a class is created =====
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class: {name}")
        return super().__new__(cls, name, bases, dct)

class SampleClass(metaclass=MyMeta):
    pass

print()

# ===== Task 5: Modify class attributes automatically using a metaclass =====
class UpperAttrMeta(type):
    def __new__(cls, name, bases, dct):
        new_dct = {}
        for key, value in dct.items():
            if not key.startswith("__") and isinstance(value, str):
                new_dct[key.upper()] = value
            else:
                new_dct[key] = value
        return super().__new__(cls, name, bases, new_dct)

class Config(metaclass=UpperAttrMeta):
    name = "config1"
    version = "1.0"

print("Task 5: Modified attribute NAME:", Config.NAME)
print("Task 5: Modified attribute VERSION:", Config.VERSION)