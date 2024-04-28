# Sets in python more or less work in the same way as sets in mathematics. We can perform operations like union and intersection on the sets just like in mathematics.
'''
1. union() and update():
The union() and update() methods prints all items that are present in the two sets.
The union() method returns a new set in a different set. 
whereas update() method adds item into the existing set from another set means just update the exisating set. '''


City_Centers = {"Hong Kong", "Mumbai", "California", "Cairo", "Moscow", "Delhi", "Tokyo", "Shanghai", "Beijing", }
Asian_Captials = {"Delhi", "Beijing", "Tokyo", "Seoul", "Riadh", "Bangkok"}
outer_cities = {"Washington", "Paris", "London", "Cairo", "Moscow"}

Asian_cities = City_Centers.union(Asian_Captials)    # this will print all the cities including the captials and centers.
print(Asian_cities) 

Asian_Captials.update(City_Centers)    # this will update the asian_capital set by including all the items from the city_centers.
print(Asian_Captials)


