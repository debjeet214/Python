''' 
1. finally block is always executed after leaving the try statement. In case if some exception was not handled by except block, it is       re-raised after execution of finally block.
2. finally block is used to deallocate the system resources.
3. One can use finally just after try without using except block, but no exception is handled in that case.

'''

# Scenario 1 Python program.
# Example where it will raises divide by zero exception.

try:          
	k = 5//0 
	print(k)
except ZeroDivisionError: 
	print("Can't divide by zero")
	
finally:
	print('This is always executed')  # still it will be printed at the end


# scenario 2 Python Program
# example where it will not raise error

try:
    k = 5//1 
    print(k)
except ZeroDivisionError:   
    print("Can't divide by zero")
     
finally:
    print('This is always executed')   # still it will be executed 

# scenario 3 Python program
# example where the exception is not handled

try:
    k = 5//0 # exception raised
    print(k)
     
finally:
    print('This is always executed')    # even still finally block will be executed.

