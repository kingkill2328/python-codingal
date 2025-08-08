num = int(input("Enter the number"))
t = num
numLen = 0
while t > 0:
    numLen = numLen + 1
    t = t//10
if numLen >= 4:
    numLen = int(numLen/2)
    chk = 0
    while num > 0:
        rem = num%10
        if chk == numLen:
            midone = rem
        elif chk == numLen - 1:
            midTwo = rem
        num = int(num/10)
        chk = chk+1
    prod = midone * midTwo
    print(prod)
else:
    print("It has to be atleast 4 digits")