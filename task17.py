from contextlib import contextmanager

# ===== Task 1: Read a file using with =====
# First, let's create a sample file to read
with open("sample.txt", "w") as file:
    file.write("This is a sample file.\nCreated for Day 17 challenges.\n")

with open("sample.txt", "r") as file:
    content = file.read()
print("Task 1: File content read using 'with':")
print(content)

print()

# ===== Task 2: Write student details into a file =====
students = [
    {"name": "Rithuu", "marks": 92},
    {"name": "Mahendra", "marks": 88},
    {"name": "Priya", "marks": 95}
]

with open("students.txt", "w") as file:
    for student in students:
        file.write(f"Name: {student['name']}, Marks: {student['marks']}\n")

print("Task 2: Student details written to students.txt")

print()

# ===== Task 3: Create your own context manager (class-based) =====
class MyFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

with MyFileManager("students.txt", "r") as file:
    print("Task 3: Reading using custom context manager:")
    print(file.read())

print()

# ===== Task 4: Use contextlib.contextmanager to build a custom context manager =====
@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with open_file("sample.txt", "r") as file:
    print("Task 4: Reading using contextlib.contextmanager:")
    print(file.read())

print()

# ===== Task 5: Open two files simultaneously and copy data from one to another =====
with open("sample.txt", "r") as source_file, open("copy.txt", "w") as destination_file:
    data = source_file.read()
    destination_file.write(data)

print("Task 5: Data copied from sample.txt to copy.txt")

with open("copy.txt", "r") as file:
    print("Task 5: Content of copy.txt:")
    print(file.read())