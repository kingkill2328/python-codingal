try:
  num1, num2 = eval("Enter two numbers, seperated by comma's")
  result = num1 / num2
  print("Result is ",result)


except ZeroDivisionError as e:
  print("Division by zero is error")


except SyntaxError:
  print ("Comma is missing Enter number sperated by comma like 1, 2")


except :
    print ("No Exception")
else:
    print ("No Exception")
finally:
  print ("This will execute no matter what")