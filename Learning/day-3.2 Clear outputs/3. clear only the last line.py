import sys
import time

#  "Use this function to delete the last line in the STDOUT"

def delete_last_line():
    sys.stdout.write('\x1b[1A')    #cursor up one line
    sys.stdout.write('\x1b[2K')    #delete last line

########## FOR DEMO ################
if __name__ == "__main__":
    print("hello")
    print("this line will be delete after 2 seconds")    # this line will be deleted after 2 seconds.
    time.sleep(2)
    delete_last_line()
####################################
