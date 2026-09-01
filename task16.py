# ===== Task 1: Generator to print numbers from 1 to 20 =====
def number_generator():
    for i in range(1, 21):
        yield i

print("Task 1: Numbers from 1 to 20:")
for num in number_generator():
    print(num, end=" ")

print("\n")

# ===== Task 2: Generator that returns odd numbers =====
def odd_number_generator(limit):
    for i in range(1, limit + 1):
        if i % 2 != 0:
            yield i

print("Task 2: Odd numbers from 1 to 20:")
for num in odd_number_generator(20):
    print(num, end=" ")

print("\n")

# ===== Task 3: Generate the first 15 Fibonacci numbers using yield =====
def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("Task 3: First 15 Fibonacci numbers:")
for num in fibonacci_generator(15):
    print(num, end=" ")

print("\n")

# ===== Task 4: Use iter() and next() to traverse a tuple =====
my_tuple = (10, 20, 30, 40, 50)
tuple_iterator = iter(my_tuple)

print("Task 4: Traversing tuple using iter() and next():")
print(next(tuple_iterator))
print(next(tuple_iterator))
print(next(tuple_iterator))
print(next(tuple_iterator))
print(next(tuple_iterator))

print()

# ===== Task 5: Generator expression to produce cubes of numbers from 1 to 10 =====
cubes = (x ** 3 for x in range(1, 11))

print("Task 5: Cubes of numbers from 1 to 10:")
for cube in cubes:
    print(cube, end=" ")
print()