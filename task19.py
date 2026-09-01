import threading
import multiprocessing
import time

# ===== Task 1: Create two threads printing numbers =====
def print_numbers(name, count):
    for i in range(1, count + 1):
        print(f"{name}: {i}")
        time.sleep(0.1)

thread1 = threading.Thread(target=print_numbers, args=("Thread-1", 5))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2", 5))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print()

# ===== Task 2: Create a multiprocessing program =====
def square_numbers():
    for i in range(1, 6):
        print("Square:", i * i)
        time.sleep(0.1)

def cube_numbers():
    for i in range(1, 6):
        print("Cube:", i ** 3)
        time.sleep(0.1)

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=square_numbers)
    process2 = multiprocessing.Process(target=cube_numbers)

    process1.start()
    process2.start()
    process1.join()
    process2.join()

    print()

    # ===== Task 3: Demonstrate thread synchronization using a lock =====
    balance = 0
    lock = threading.Lock()

    def deposit(amount, times):
        global balance
        for _ in range(times):
            with lock:
                balance += amount

    thread3 = threading.Thread(target=deposit, args=(10, 100))
    thread4 = threading.Thread(target=deposit, args=(10, 100))

    thread3.start()
    thread4.start()
    thread3.join()
    thread4.join()

    print("Task 3: Final balance (with lock):", balance)

    print()

    # ===== Task 4: Compare thread execution time with sequential execution =====
    def task():
        time.sleep(1)

    # Sequential execution
    start_seq = time.time()
    task()
    task()
    end_seq = time.time()
    print("Task 4: Sequential execution time:", round(end_seq - start_seq, 2), "seconds")

    # Threaded execution
    start_thread = time.time()
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_thread = time.time()
    print("Task 4: Threaded execution time:", round(end_thread - start_thread, 2), "seconds")

    print()

    # ===== Task 5: Download multiple files simultaneously using threads (simulation) =====
    def download_file(filename):
        print(f"Starting download: {filename}")
        time.sleep(1)  # simulating download time
        print(f"Completed download: {filename}")

    files = ["file1.zip", "file2.zip", "file3.zip"]
    download_threads = []

    for file in files:
        t = threading.Thread(target=download_file, args=(file,))
        download_threads.append(t)
        t.start()

    for t in download_threads:
        t.join()

    print("Task 5: All files downloaded simultaneously!")