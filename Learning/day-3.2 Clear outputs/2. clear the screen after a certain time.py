import os
from time import sleep

# some text
print("a")
print("b")
print("c")
print("d")
print("e")
print("Screen will now be cleared in 5 Seconds")

sleep(10) # Waiting for 10 seconds, and then the screen will be cleared

# Clearing the Screen
os.system('cls')
