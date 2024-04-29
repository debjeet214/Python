ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90, 341: 99}

ep1.update(ep2)       # this will update the dict 1 by adding items from ep2
print(ep1)

ep1.pop(122)          # this will pop out a item from dictionary
print(ep1)

ep1.popitem()         # this will pop the last element from dictionary
print(ep1)

del ep1[566]          # this will delete elements from the beginning side
print(ep1)

ep1.clear()           # this will fully clear the items from the dictionary
print(ep1)
