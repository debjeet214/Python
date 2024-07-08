while True :
  age = int(input("Enter your age: "))
  print("your age is ",age)
  if(age<18):
    print("You can not join the Exam")
    break


# another example of doing this

i = 1
while True:
  print(i)
  
  if(i%10 == 0):
    break
  i += 1
