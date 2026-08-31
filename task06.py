

import math
import random
 

# ===== Task 1: Find the square root of a number using the math module =====
number = 64
sqrt_value = math.sqrt(number)
print("Square root of", number, "is:", sqrt_value)

print()

# ===== Task 2: Generate five random numbers between 1 and 50 =====
random_numbers = [random.randint(1, 50) for _ in range(5)]
print("Five random numbers between 1 and 50:", random_numbers)

print()

# ===== Task 3: Use our own module with multiplication and division functions =====
print("Multiplication (6 x 7):",(6, 7))
print("Division (20 / 4):", (20, 4))

print()

# ===== Task 4: Use random.choice() to select a random student name =====
students = ["Rithuu", "Mahendra", "Priya", "Karthik", "Sneha"]
selected_student = random.choice(students)
print("Randomly selected student:", selected_student)

print()

# ===== Task 5: Print the value of π and Euler's number (e) using the math module =====
print("Value of pi:", math.pi)
print("Value of Euler's number (e):", math.e)