try:
  num = int(input("Enter a integer: "))
  a = [9, 3, 2, 10]
  print(a[num])

except ValueError:
  print("The Number entered is not a integer")

except IndexError:
  print("Index out of range")

except Exception as e:
  print(e)
