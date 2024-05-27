# try block is used to ented a piece of code to check if it is ok or not.
# if the try block is satisfied then the except block is skipped but
# if the try block is false then it will not show error but it will enter the except block and execute the code in it.

marks = input("enter your mnarks: ")

try:
    score = int(marks)
except:
    print("please enter a number")

print("You entered", marks)

marks = input("enter your mnarks: ")

try:
    score = int(marks)
except:
    print("please enter a number")

print("You entered now", marks)
