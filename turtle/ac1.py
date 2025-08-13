import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(600,600)
warith = turtle.Turtle()
num = int(input("Enter the nnumber of size"))
angle = 360//num
for i in range(num):
    warith.forward(100)
    warith.left(angle)
turtle.done()