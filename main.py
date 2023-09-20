import turtle
turtle.bgcolor('light pink')
turtle.pensize(2)
turtle.speed(0.5)
color=['Red','Green','Yellow','Blue']
for x in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(140)
        turtle.left(10)
turtle.mainloop()