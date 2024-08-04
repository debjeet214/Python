# first importing the threading and time module
import time
import threading

# declearing a function to do the operation
def longsquare(num, results):
  time.sleep(2)  # pause the program for 2 seconds
  results[num] = num**2  # this will found the square of the number and store in dictionary named 'result' and with key 'num'

results = {}   # assigning the empty dictionary results
threads = [threading.Thread(target=longsquare, args=(n, result)) for n in range(0, 10)]
# here we are defining the thread by targetting and taking input by args, with for loop
[t.start() for t in threads]  # starting the thread for all the t
[t.join() for t in threads]   # confirming that all the t's are executed successfully otherwise waits
print(result)   # aftre all done it will print the result wiht dictionary form.
