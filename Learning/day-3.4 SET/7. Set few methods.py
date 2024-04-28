# isdisjoint method

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo1", "Seoul", "Kabul", "Madrid2"}
print(cities.isdisjoint(cities2))                 # will return True as no items in cities2 is in cities set.

#issuperset method

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))                 # this will return false as not all the cities2 items are in the citites set

cities3 = { "Madrid","Tokyo"}
print(cities.issuperset(cities3)) # but this will return True

#issubset method

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities))


