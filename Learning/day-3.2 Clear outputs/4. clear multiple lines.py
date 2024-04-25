# Delete the multiple lines in the STDOUT.
def delete_multiple_lines(n=1):
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line
        
# delete multiple lines .........................................
# Demo

if __name__ == "__main__":
    print("You will be seeing a question on the screen for 60 sec.")
    print("You have to choose the correct answer.")
    print("Only type 'a' for first option, 'b' for second option, 'c' for third option and 'd' for forth options only.")
    time.sleep(9)                # there will be a 9 sec pause before next line execution
    delete_multiple_lines(n=3)   # this will delete the last 3 lines 
