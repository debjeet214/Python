# Definition:
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

## Meta Characters:
Metacharacters are characters with a special meaning:
```
- []	it is used to get a set of characters	" like [a-m]"	
- \	Signals a special sequence (can also be used to escape special characters)	"\d"	
- .	Any character (except newline character)	"he..o"	
- ^	Starts with	"^hello"	
- $	Ends with	"planet$"	
- *	Zero or more occurrences	"he.*o"	
- +	One or more occurrences	"he.+o"	
- ?	Zero or one occurrences	"he.?o"	
- {}	Exactly the specified number of occurrences	"he.{2}o"	
- |	Either or	"falls|stays"	
- ()	Capture and group
```

## Special Sequence :
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:
```
- \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
- \b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"
- \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
- \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"
- \D	Returns a match where the string DOES NOT contain digits	"\D"
- \s	Returns a match where the string contains a white space character	"\s"
- \S	Returns a match where the string DOES NOT contain a white space character	"\S"
- \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
- \W	Returns a match where the string DOES NOT contain any word characters	"\W"
- \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	
```

## Sets
A set is a set of characters inside a pair of square brackets [] with a special meaning:
```
- [arn]	  Returns a match where one of the specified characters (a, r, or n) is present
- [a-n]	  Returns a match for any lowercase character, alphabetically between a and n
- [^arn]	Returns a match for any character EXCEPT a, r, and n
- [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
- [0-9]	  Returns a match for any digit between 0 and 9
- [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59
- [a-zA-Z]	  Returns a match for any character alphabetically between a and z, lower case OR upper case	
- [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
```
