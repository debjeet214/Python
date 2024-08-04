# Daemon threads run in the background and do not prevent the program from exiting. You can set a thread as a daemon thread using the daemon property.
# In this example, the background task runs indefinitely, but the program will exit after 5 seconds, stopping the daemon thread.

import threading
import time

def background_task():
    while True:
        print("Running in the background")
        time.sleep(1)

# Create a daemon thread
thread = threading.Thread(target=background_task)
thread.daemon = True

# Start the thread
thread.start()

# Main program continues
time.sleep(5)
print("Main program exiting")
