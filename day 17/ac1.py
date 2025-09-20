try:
  number =  (input("Enter a number:"))
  print("The number entered is", number)
except ValueError as e: 
    print ("Exception:", e)
    