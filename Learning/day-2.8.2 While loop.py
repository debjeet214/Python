# normal while loop structure.
i = 1
while(i<3):     # condition check
  print(i, end=' ')      # inner code  here we printed all the o/p on the same line with a space separetor 
  i+=1          # incrementing the element

# checking grades using while loop

counting = 1
while( counting<=6 ):
  counting+= 1

  marks = int(input("Enter Your mark's percentage: "))
  if(marks>= 0 and marks<= 100):
    if( marks >= 90 ):
      print(" you got A")
    elif(marks >= 70 ):
      print("You got B")
    elif( marks >= 50 ):
      print("You got C")
    else:
      print("you failed in the exam")
  else:
    print("enter a valid marks !!!")
