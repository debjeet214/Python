weight = int(input("Enter your age in Kg or grams: "))
unit = input("enter the unit of the entered age in form of K for kg and g for grams ")

wish = input("if you want to modify enter 'Y': ")
if wish.upper() == 'Y':
  if unit.upper() == 'K' :
    modified = weight * 1000
    print("Weight in grams :" + str(modified))
  elif unit.upper() == 'G':
    modified = weight / 1000
    print("Weight in KG is :" + str(modified))
  else :
    print("enter a valid input ")

else :
  print(" so your weight is currently "+ str(weight) )  
