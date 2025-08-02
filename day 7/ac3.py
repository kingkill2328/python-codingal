print("enter marks obtained in 5 subjects")
markOne = int(input())
markTwo = int(input())
markThree = int(input())
markFour = int(input())
markFive = int(input())

tot = markOne + markTwo + markThree + markFour + markFive
avg = tot / 5

if avg >= 90:
    print("Grade A")
elif avg >= 81:
    print("Grade B")
elif avg >= 71:
    print("Grade C")
elif avg >= 61:
    print("Grade D")
elif avg >= 51:
    print("Grade E")
elif avg >= 41:
    print("Grade F")