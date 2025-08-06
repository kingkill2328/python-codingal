num = input("Enter a number from (0 - 127)")
if num.isdigit():
    num = int(num)
    if 0 <= num <= 127:
     print(f"the Ascii character for {num} is '{chr(num)}'")
        else:
          print("please enter a number from (0 - 127)")
else
    print("Please enter a valid number")
