# continue statemenmt is used to skip a single iteration.
# here the loop will work for 19 times and it will skip all the loop where the age is less than 18 otherwise it'll execute the loop

for i in range(1, 20):
  check = int(input("Enter the age: "))
  if(check<=18):
    continue
  else:
    print("Voter no.", i, "is eligible to give vote")
