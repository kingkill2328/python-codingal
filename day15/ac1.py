def total_calc(bill_amount,tip_perc):
  total = bill_amount + (bill_amount * tip_perc)
  total = round(total, 2)
  print(f"Please pay $ {total}")

total_calc(150, 0.05)