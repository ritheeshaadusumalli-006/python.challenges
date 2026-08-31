# ===== Task 1: Write your name into a file =====
with open("data.txt", "w") as file:
    file.write("Rithuu\n")
print("Task 1: Name written into data.txt")

print()

# ===== Task 2: Read and print the contents of a file =====
with open("data.txt", "r") as file:
    content = file.read()
print("Task 2: File contents:")
print(content)

print()

# ===== Task 3: Append your college name to a file =====
with open("data.txt", "a") as file:
    file.write("Sri Venkateswaraa College of Technology\n")
print("Task 3: College name appended to data.txt")

print()

# ===== Task 4: Count the number of lines in a file =====
with open("data.txt", "r") as file:
    lines = file.readlines()
    line_count = len(lines)
print("Task 4: Number of lines in file:", line_count)

print()

# ===== Task 5: Count the number of words in a file =====
with open("data.txt", "r") as file:
    content = file.read()
    word_count = len(content.split())
print("Task 5: Number of words in file:", word_count)