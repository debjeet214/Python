#  Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.


hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

if hours <= 40:
    gross_pay = hours * rate
else:
    gross_pay = 40 * rate + (hours - 40) * rate * 1.5
print("Gross Pay will be :", gross_pay)


# doing the same using the function

def computepay(hours, rate):
    if hours <= 40:
        pay = hours * rate
    else:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    return pay
hours = float(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))

gross_pay = computepay(hours, rate)
print("Pay", gross_pay)
