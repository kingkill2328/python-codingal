valid = True
while valid:
  try:
    n = int(input("Enter a number"))
    while n%2 == 0:
      print ("bye")
    valid = False
  except ValueError:
    print("Invalid input")