'''
II. intersection and intersection_update():
The intersection() and intersection_update() methods prints only items that are similar to both the sets means, only common items.
The intersection() method returns a new set whereas intersection_update() method updates into the existing set from another set. '''

City_Centers = {"Hong Kong", "Mumbai", "California", "Cairo", "Moscow", "Delhi", "Tokyo", "Shanghai", "Beijing", }
Asian_Captials = {"Delhi", "Beijing", "Tokyo", "Seoul", "Riadh", "Bangkok"}
outer_cities = {"Washington", "Paris", "London", "Cairo", "Moscow"}

Asian_Cap_centers = City_Centers.intersection(Asian_Captials) # this will find only those capital cities where is the city center.
print(Asian_Cap_centers)

# similarly it can be done by updating one set with other set's items through intersection using intersection_update method.

outer_cities.intersection_update(City_Centers)
print(outer_cities)                            # o/p = Moscow, Cairo

