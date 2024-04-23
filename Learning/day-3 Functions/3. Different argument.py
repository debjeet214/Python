'''Function Arguments and return statement
Default Arguments
Keyword Arguments
Variable length Arguments
Required Arguments

Default arguments:  We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.


Keyword arguments:   We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.



Required arguments:   In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.


Variable-length arguments:
Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of tuple.


Keyword Arbitrary Arguments:
While creating a function, pass a * before the parameter name while defining the function. The function accesses the arguments by processing them in the form of dictionary.

