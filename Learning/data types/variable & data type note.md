<h2><b>What is a variable?</b></h2>
Variable is like a container that holds data. Very similar to how our containers in kitchen holds sugar, salt etc Creating a variable is like creating a placeholder in memory and assigning it some value. In Python its as easy as writing:

a = 1
b = True
c = "Harry"
d = None

<h2>What is a Data Type?</h2>
Data type specifies the type of value a variable holds. This is required in programming to do various operations without causing an error.
In python, we can print the type of any operator using type function:

a = 1
print(type(a))
b = "1"
print(type(b))
By default, python provides the following built-in data types:

<h3>1. Numeric data: int, float, complex</h3>
- int: 3, -8, 0
- float: 7.349, -9.0, 0.0000001
- complex: 6 + 2i

<h3>2. Text data: str</h3>
str: "Hello World!!!", "Python Programming"

<h3>3. Boolean data:</h3>
Boolean data consists of values True or False.

<h3>4. Sequenced data: list, tuple</h3>
list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.

Example:

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
Output:

[8, 2.3, [-4, 5], ['apple', 'banana']]
Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.

Example:

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
Output:

(('parrot', 'sparrow'), ('Lion', 'Tiger'))
5. Mapped data: dict
dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.

Example:

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
Output:

{'name': 'Sakshi', 'age': 20, 'canVote': True}
