import sys
import time

str = "!!! Welcome to kon banega crorepati !!!\n"
x = str.title()
print(x.center(173))
total_won = 0
# Use this function to delete the last line in the STDOUT
def delete_last_line():

    sys.stdout.write('\x1b[1A') #cursor up one line
    sys.stdout.write('\x1b[2K') #delete last line

 # the function is done here -----------------------------------

# Delete the multiple lines in the STDOUT.
def delete_multiple_lines(n=1):
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line
        
# delete multiple lines .........................................


# main function for the option choice in the question:
def QA(lists, ans, prize):
    global passed 

    for i in range(len(lists)):
        print(lists[i])
        time.sleep(0.5)
    x = input("Enter Your Answer: ")
    if x != ans:
        print("That's wrong answer")
        print("Sorry, but it's finished and you can't procced furthur!!")
        passed == 0
    else:
        print("Correct Answer")
        time.sleep(1)
        delete_multiple_lines(n=7)
        print("you have won ",prize," rupees")
        time.sleep(1)
        passed = 1
# finishing this main function

if __name__ == "__main__":
    print("Description of the Rules :")
    print(" ")
    time.sleep(3)
    if __name__ == "__main__":
        print("You will be seeing a question on the screen for 60 sec.")
        print("You have to choose the correct answer.")
        print("Only type 'a' for first option, 'b' for second option, 'c' for third option and 'd' for forth options only.")
        time.sleep(9)
        delete_multiple_lines(n=3)

    if __name__ == "__main__":
        print("Enter any one option at once. ")
        print("Only if you enter the correct answer, you will be directed to the next question :")
        time.sleep(8)
        delete_multiple_lines(n=2)
    time.sleep(0)
    delete_multiple_lines(n = 3)

# question and correct answers are here

ques1 = ["Who invented the Java?", "James Gosling", "Norten tensy", "Issac Newton", "Mother teresa"]
ques2 = ["Who invented the C?", "Dennis Ritchie", "Lovely ghosh", "Brenden Sandy", "Never inevnted"]
ques3 = ["Who invented the C++?","Frankline Roze", "Santur Lorris", "Bjarne Stroustrup", "Jennifer lorin"]
ques4 = ["Who invented the Python?","Fernaldo Alonso", "Guido van Rossum", "Gerorge Russell", "Hamilton"]
ques5 = ["Who invented the Javascript?", "Antalio Sandy", "Brendan Eich", "Erinburg glotty", "Sandy warner"]
ques6 = ["Who invented the Ruby?", "Rabindranath", "Lavendar dutta","Amitav bacchan","Yukihiro Matsumoto"]
ques7 = ["Who invented the Swift?", "Matsuyama yatamare", "Richard colifer", "Chris Lattner", "Snigdha roy"]

print("\nStarting The Questions: ")

answer = input("Are you ready? Enter 'y' for YES and 'n' for NO:\n")
if(answer == 'y'):
    QA(ques1, "a", 40000)
    if(passed == 1):
        total_won += 40000
        QA(ques2, "a",60000)
        if(passed == 1):
            total_won += 60000
            QA(ques3, "c", 100000)
            if(passed == 1):
                total_won += 100000
                QA(ques4, "b", 500000)
                if(passed == 1):
                    total_won += 500000
                    QA(ques5, "b", 1000000)
                    if(passed == 1):
                        total_won += 1000000
                        QA(ques6, "d", 3500000)
                        if(passed == 1):
                            total_won += 3500000
                            QA(ques7, "c", 4800000)
                            if(passed == 1):
                                total_won += 4800000
                                print(" ")
                                print("Congratulations !! You are now the new crorePati !! ")
                                print("You have won",total_won," rupees in total .... Congrats bro!!")

else:
    print("BYE BYE  !!!")
