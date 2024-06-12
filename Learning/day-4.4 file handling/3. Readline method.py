f = open('ff.txt', 'r')
i = 0

while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"Marks in the maths for student {i} is {m1}")
    print(f"Marks in the science for student {i} is {m2}")
    print(f"Marks in the english for student {i} is {m3}\n")
    print(line)
