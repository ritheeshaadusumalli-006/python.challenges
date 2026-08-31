# ===== Task 1: Largest of Two Numbers =====
num1 = 12
num2 = 25

if num1 > num2:
    print("Largest of two numbers:", num1)
else:
    print("Largest of two numbers:", num2)

print()

# ===== Task 2: Largest of Three Numbers =====
a = 10
b = 45
c = 23

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print("Largest of three numbers:", largest)

print()

# ===== Task 3: Even or Odd =====
number = 17

if number % 2 == 0:
    print(number, "is Even")
else:
    print(number, "is Odd")

print()

# ===== Task 4: Leap Year Checker =====
year = 2024

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is Not a Leap Year")

print()

# ===== Task 5: Grade Calculator =====
marks = 85

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 40:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)