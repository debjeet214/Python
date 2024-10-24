# The sub() function replaces the matches with the text of your choice. means if i want to repce every a with b, i can do here.

import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt) # here it will replace all white space with 9 only.
print(x)   # -> The9rain9in9Spain

# ex - 2
import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2) # replaceonly the first 2 matching.
print(x)  # -> The9rain9in Spain
