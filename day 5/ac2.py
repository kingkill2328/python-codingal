actual_cost = float(input("Enter the actual buying price of the product"))
selling_cost = float(input("Enter the selling price of the product"))
profit = selling_cost - actual_cost
if profit > 0 :
    print("you made a profit")
elif profit < 0:
    print("you made a loss")
else:
    print("Break even no profit no loss")