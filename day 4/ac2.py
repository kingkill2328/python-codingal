amount = int(input("please enter amount in multiple of 10"))
note10 = note50 = note100 = 0
note100 = amount // 100
amount = amount % 100
note50 = amount // 50
amount = amount % 50
note10 = amount // 10
amount = amount % 10

print(f"Note 100 : {note100}")
print(f"Note 50 : {note50}")
print(f"Note 10 : {note10}")