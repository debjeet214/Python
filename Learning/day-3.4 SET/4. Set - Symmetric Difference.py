'''III. symmetric_difference and symmetric_difference_update():
The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set.'''

City_Centers = {"Hong Kong", "Mumbai", "California", "Cairo", "Moscow", "Delhi", "Tokyo", "Shanghai", "Beijing", }
Asian_Captials = {"Delhi", "Beijing", "Tokyo", "Seoul", "Riadh", "Bangkok", "Hong Kong"}
outer_cities = {"Washington", "Paris", "London", "Cairo", "Moscow"}

NonCap_Centers = City_Centers.symmetric_difference(Asian_Captials.union(outer_cities))
# here we first union all the capital centers & then finds all  the unique cities that are only in one set
print(NonCap_Centers)

Asian_Captials.symmetric_difference_update(outer_cities)
print(Asian_Captials)  # this prints all the different capitals that is not in both sets.
