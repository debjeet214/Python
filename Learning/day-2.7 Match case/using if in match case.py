age = int(input("enter your current age: "))

match age:
  case age if age<18:
    print("You are not eligible to give vote")
  case age if age>18:
    print(" you are eligible to vote")
  case age if age == 18:
    month = int(input(" enter your month in number: "))
    match month:
      case month if month<6 :
        print(" You are not eligible as you are not 18+")
      case month if month >= 6:
        print("you are eligible as you are 18+")
  case _:
    print(" Wish you had a good voting experience")
