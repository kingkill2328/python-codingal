print("enter marks obtained in 5 subjects")
math = int(input("enter marks in math"))
litreture = int(input("enter marks in litreture"))
science = int(input("enter marks in science"))
socialstudies = int(input("enter marks in socialstudies"))
computerscience = int(input("enter marks in computerscience"))

sum = math + litreture + science + socialstudies + computerscience
perc = (sum / 500) * 100
print("Overall percentage: ",perc)