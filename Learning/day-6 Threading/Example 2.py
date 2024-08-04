import threading
import time

def download_file(file_id):
    time.sleep(2)  # Simulate a file download
    print(f"Downloaded file {file_id}")

threads = []
for i in range(5):
    thread = threading.Thread(target=download_file, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All files downloaded")
