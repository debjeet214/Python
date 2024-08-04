import threading
import time

def worker(thread_id):
    print(f"Thread {thread_id} is starting")
    time.sleep(2)
    print(f"Thread {thread_id} is finishing")

threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have finished")
