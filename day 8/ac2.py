units = int(input("Please enter number of units you consumed"))
if units < 50:
    amount = units * 2.60
    surchrge = 25
elif units <=100:
    amount = units * 3.25
    surchrge = 35
elif units <=200:
    amount = units * 5.26
    surchrge = 45
else:
    amount = units * 8.45
    surcharge = 70

total = amount + surcharge
print('Electricity Bill =', total)