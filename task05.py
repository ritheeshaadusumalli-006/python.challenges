# ===== Task 1: Function to find the square of a number =====
def square(num):
    return num ** 2

print("Square of 5:", square(5))

print()

# ===== Task 2: Function to check whether a number is even or odd =====
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

print(check_even_odd(17))

print()

# ===== Task 3: Function to find the largest of three numbers =====
def largest_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Largest of three numbers:", largest_of_three(10, 45, 23))

print()

# ===== Task 4: Function to calculate the factorial of a number =====
def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

print("Factorial of 5:", factorial(5))

print()

# ===== Task 5: Function to return the average of three numbers =====
def average_of_three(a, b, c):
    return (a + b + c) / 3

print("Average of 10, 20, 30:", average_of_three(10, 20, 30))