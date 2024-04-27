<h2>Sets, lists, and tuples are all data structures in Python, but they have some fundamental differences:</h2>

<h3><b>Mutability:</b></h3>
- Lists are mutable, meaning you can change their elements after they have been created. You can add, remove, or modify elements in a list.
- Tuples are immutable, meaning once they are created, their elements cannot be changed. You cannot add, remove, or modify elements in a tuple.
- Sets are mutable, but their elements are unique and immutable. However, you can add or remove items from a set.
<h3><b>Ordering:</b></h3>
- Lists & Tuples maintain the order of elements, meaning the elements are stored in the same order as they were inserted.
- Sets do not maintain any order. The elements of a set are unordered, which means you cannot rely on the order in which elements are stored.
<h3><b>Duplication:</b></h3>
- Lists and tuples can contain duplicate elements.
- Sets do not allow duplicate elements. If you try to add a duplicate element to a set, it will be ignored.
Syntax:
- Lists are defined using square brackets [], 
- Tuples are defined using parentheses (), 
- Sets are defined using curly braces {}, but they can also be created using the set() constructor.


```python
# List
my_list = [1, 2, 3, 3, 4]
# Tuple
my_tuple = (1, 2, 3, 3, 4)
# Set
my_set = {1, 2, 3, 3, 4}

print("List:", my_list)  # Output: List: [1, 2, 3, 3, 4]
print("Tuple:", my_tuple)  # Output: Tuple: (1, 2, 3, 3, 4)
print("Set:", my_set)  # Output: Set: {1, 2, 3, 4}'''
