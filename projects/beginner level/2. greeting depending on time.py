import time
te = time.strftime('%H:%M:%S')
hour =int(time.strftime('%H'))
print(hour)

if(hour>00 and hour<4):
  print("Have a happy midnight time gentleman")
elif(hour>4 and hour<6):
  print(' Hope you have a nice sleep sir, wish you a beautiful Dawn')
elif(hour>6 and hour<12):
  print(" Good Morning Sir !!")
elif(hour>12 and hour<18):
  print(" wish you have a pleasent afternoon")
elif(hour>18 and hour<25):
  print(" Have a good night sir !!")
else:
  print("enter a valid hour between 0 to 24")
