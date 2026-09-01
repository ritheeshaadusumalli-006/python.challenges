from collections import deque
import heapq

# ===== Task 1: Implement a stack using a list =====
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print("Task 1: Stack after pushes:", stack)

popped = stack.pop()
print("Task 1: Popped element:", popped)
print("Task 1: Stack after pop:", stack)

print()

# ===== Task 2: Implement a queue using deque =====
queue = deque()
queue.append("Person1")
queue.append("Person2")
queue.append("Person3")
print("Task 2: Queue after enqueues:", queue)

removed = queue.popleft()
print("Task 2: Dequeued element:", removed)
print("Task 2: Queue after dequeue:", queue)

print()

# ===== Task 3: Find the smallest element using a heap =====
numbers = [25, 10, 45, 3, 60, 18]
heapq.heapify(numbers)
smallest = heapq.heappop(numbers)
print("Task 3: Original list turned into heap:", numbers)
print("Task 3: Smallest element:", smallest)

print()

# ===== Task 4: Reverse a string using a stack =====
def reverse_string(s):
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str

original = "Python"
print("Task 4: Original string:", original)
print("Task 4: Reversed string:", reverse_string(original))

print()

# ===== Task 5: Simulate a ticket booking queue using a queue =====
ticket_queue = deque()

def book_ticket(name):
    ticket_queue.append(name)
    print(f"{name} added to the ticket booking queue.")

def process_ticket():
    if ticket_queue:
        person = ticket_queue.popleft()
        print(f"Ticket booked for {person}.")
    else:
        print("No one in the queue.")

book_ticket("Rithuu")
book_ticket("Mahendra")
book_ticket("Priya")

process_ticket()
process_ticket()
print("Task 5: Remaining queue:", ticket_queue)