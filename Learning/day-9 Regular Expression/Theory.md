## Definition:
A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.

Python has a built-in package called re, which can be used to work with Regular Expressions.

```python
import re
```

Example - Search the string to see if it starts with "The" and ends with "Spain":
```python
import re
txt = "The rain in Spain"
// here "^ ." - is used for the starting & "*$" - is used for the ending word.
x = re.search("^The.*Spain$", txt) 
```

### Functions:

- findall	-> Returns a list containing all matches
- search	-> Returns a Match object if there is a match anywhere in the string
- split	-> Returns a list where the string has been split at each match
- sub	-> Replaces one or many matches with a string
