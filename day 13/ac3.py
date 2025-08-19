def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print("What operation do you want to perform?")
print("1.add")
print("2. subtract")
print("3.multiply")
print("4.divide")
choice = int(input("input the corrosponding digit"))
if choice == 1:
    print(add(5, 6))
elif choice == 2:
    print(subtract(5, 6))
elif choice == 3:
    print(multiply(5, 6))
elif choice == 4:
    print(divide(5, 6))
else : print("Invalid input")

