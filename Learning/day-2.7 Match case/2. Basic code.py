edu_standard = int(input("enter your last qualifucation 10 / 12: \n")) # user input

match edu_standard:
  case 12:
    print("you are eligible for the group C exam")
  case 10:
    print("you are eligible for group D exam")
  case _:   # default statement...
    print("there is no available excams for your standard of education")
