import time
from functools import wraps

# ===== Task 1: Decorator that prints "Program Started" before a function =====
def program_started(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Program Started")
        return func(*args, **kwargs)
    return wrapper

@program_started
def greet():
    print("Hello, welcome!")

greet()

print()

# ===== Task 2: Decorator to calculate execution time =====
def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.5f} seconds")
        return result
    return wrapper

@execution_time
def calculate_sum():
    total = sum(range(1000000))
    print("Sum calculated:", total)

calculate_sum()

print()

# ===== Task 3: Decorator that converts text output to uppercase =====
def uppercase_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_output
def say_hello():
    return "hello, this is python"

print(say_hello())

print()

# ===== Task 4: Decorator that checks whether a user is logged in =====
def login_required(func):
    @wraps(func)
    def wrapper(is_logged_in, *args, **kwargs):
        if is_logged_in:
            return func(is_logged_in, *args, **kwargs)
        else:
            print("Access denied. Please log in first.")
    return wrapper

@login_required
def view_dashboard(is_logged_in):
    print("Welcome to your dashboard!")

view_dashboard(True)
view_dashboard(False)

print()

# ===== Task 5: Create two decorators and apply both to the same function =====
def bold_text(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italic_text(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"_{result}_"
    return wrapper

@bold_text
@italic_text
def format_text():
    return "Python Decorators"

print(format_text())