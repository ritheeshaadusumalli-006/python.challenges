import re

# ===== Task 1: Find all digits from a sentence =====
sentence = "I have 2 cats, 5 dogs, and 100 fish."
digits = re.findall(r'\d', sentence)
print("Task 1: Digits found:", digits)

print()

# ===== Task 2: Validate a phone number using Regex =====
def validate_phone(number):
    pattern = r'^[6-9]\d{9}$'  # 10-digit Indian phone number starting with 6-9
    if re.match(pattern, number):
        return "Valid phone number"
    else:
        return "Invalid phone number"

print("Task 2:", validate_phone("9876543210"))
print("Task 2:", validate_phone("12345"))

print()

# ===== Task 3: Validate an email address =====
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return "Valid email address"
    else:
        return "Invalid email address"

print("Task 3:", validate_email("rithuu@gmail.com"))
print("Task 3:", validate_email("rithuu@@gmail"))

print()

# ===== Task 4: Replace all spaces with underscores =====
text = "This is a Python coding challenge"
replaced_text = re.sub(r'\s', '_', text)
print("Task 4: Text with underscores:", replaced_text)

print()

# ===== Task 5: Count how many numbers are present in a paragraph =====
paragraph = "There are 12 apples, 45 mangoes, and 7 bananas in the basket, total 64 fruits."
numbers = re.findall(r'\d+', paragraph)
print("Task 5: Numbers found:", numbers)
print("Task 5: Count of numbers:", len(numbers))