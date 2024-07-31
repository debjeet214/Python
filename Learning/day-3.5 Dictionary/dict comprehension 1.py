#In Python, a dictionary comprehension is a concise way to create dictionaries. It allows you to generate dictionary entries in a single line of code, making it more readable and often more efficient than using traditional loops.

animallist = [('a', 'African Lion'), ('b', 'Buffalo'), ('c', "Cheetha")]
animallist = {item[0] : item[1] for item in animallist}
print(animallist)
