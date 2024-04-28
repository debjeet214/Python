''' IV. difference() and difference_update():

The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets means only the first set's unique items.  The difference() method returns a new set whereas difference_update() method updates into the existing set from another set.  '''

City_Centers = {"Hong Kong", "Mumbai", "California", "Cairo", "Moscow", "Delhi", "Tokyo", "Shanghai", "Beijing", }
Asian_Captials = {"Delhi", "Beijing", "Tokyo", "Seoul", "Riadh", "Bangkok", "Hong Kong"}
outer_cities = {"Washington", "Paris", "London", "Cairo", "Moscow"}


NonCap_City_Centers = City_Centers.difference(Asian_Captials.union(outer_cities))
# this will return only those non capital cities where is the center.
print(NonCap_City_Centers)  # o/p = {'California', 'Mumbai', 'Shanghai'}

City_Centers.difference_update(Asian_Captials)  # thus existing set is updated.
print(City_Centers)

