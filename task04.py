# ===== Task 1: Create an inventory system using a dictionary =====
inventory = {
    "apple": 50,
    "banana": 30,
    "orange": 20,
    "mango": 15,
    "grapes": 40
}
print("Inventory System:", inventory)

print()

# ===== Task 2: Print the first five elements of a list using slicing =====
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
first_five = numbers[0:5]
print("First five elements:", first_five)

print()

# ===== Task 3: Demonstrate tuple immutability =====
my_tuple = (1, 2, 3, 4, 5)
print("Original tuple:", my_tuple)

try:
    my_tuple[0] = 100  # attempting to change a tuple element
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable — their elements cannot be changed.")

print()

# ===== Task 4: Print the marks of a student using a dictionary =====
student_marks = {
    "Maths": 90,
    "Science": 85,
    "English": 78,
    "History": 88,
    "Computer": 95
}
print("Student Marks:", student_marks)

print()

# ===== Task 5: Remove duplicate elements from a list using a set =====
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5, 5, 6]
unique_elements = list(set(list_with_duplicates))
print("List with duplicates:", list_with_duplicates)
print("List after removing duplicates:", unique_elements)