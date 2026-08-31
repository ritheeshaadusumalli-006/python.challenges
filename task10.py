# ===== Task 1: Handle division by zero using try and except =====
try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ZeroDivisionError:
    print("Task 1: Error - Cannot divide by zero!")

print()

# ===== Task 2: Handle invalid user input when converting to an integer =====
try:
    value = "abc"
    converted_value = int(value)
except ValueError:
    print("Task 2: Error - Invalid input! Cannot convert to an integer.")

print()

# ===== Task 3: Program using try, except, else, and finally =====
try:
    num = 20
    den = 4
    result = num / den
except ZeroDivisionError:
    print("Task 3: Error - Division by zero!")
else:
    print("Task 3: Division successful, result:", result)
finally:
    print("Task 3: Execution completed.")

print()

# ===== Task 4: Raise an exception if a user's age is less than 18 =====
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    return "Access granted."

try:
    print("Task 4:", check_age(15))
except ValueError as e:
    print("Task 4: Error -", e)

print()

# ===== Task 5: Simple calculator that handles invalid operations without crashing =====
def calculator(a, b, operation):
    try:
        if operation == "+":
            return a + b
        elif operation == "-":
            return a - b
        elif operation == "*":
            return a * b
        elif operation == "/":
            return a / b
        else:
            raise ValueError("Invalid operation!")
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"
    except ValueError as e:
        return f"Error: {e}"

print("Task 5:", calculator(10, 5, "+"))
print("Task 5:", calculator(10, 0, "/"))
print("Task 5:", calculator(10, 5, "%"))