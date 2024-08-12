# Figure out our age
import datetime
currentDate = datetime.datetime.now()

DOB_input= input ('Plz enter your date of birth (mm/dd/yyyy) ')
DOB= datetime.datetime.strptime(DOB_input,'%m/%d/%Y')
print (f"your date of birth is {DOB}")
age_in_days = DOB - currentDate
print(abs(age_in_days))

years = abs(((age_in_days.total_seconds())/(365.242*24*3600)))
yearsInt=int(years)

months=abs((years-yearsInt)*12)
monthsInt=int(months)

days=abs((months-monthsInt)*(365.242/12))
daysInt=int(days)

hours = abs((days-daysInt)*24)
hoursInt=int(hours)

minutes = abs((hours-hoursInt)*60)
minutesInt=int(minutes)

seconds = abs((minutes-minutesInt)*60)
secondsInt =int(seconds)

print('You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
 minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt))
