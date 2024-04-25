import time
j = 100
print("Counting down:")
for j in range(10, 0, -1):
    print(j, end='\r')
    time.sleep(1)
print("Blast off!")
