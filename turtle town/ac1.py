import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("amazing turtle spiral")
t = turtle.Turtle()
t.speed(0)
turtle.colormode(255)
t.hideturtle()

colors = []
n = 36
for i in range(n):
    col = colorsys.hsv_to_rgb(i/n, 1, 1)
    colors.append((int(col[0]*225), int(col[1]*255), int(col[2]*225)))

for i in range (360):
    t.color(colors[i % n])
    t.width(i / 100 + 1)
    t.forward(i * 2)
    t.right(59)

turtle.done()