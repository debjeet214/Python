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
