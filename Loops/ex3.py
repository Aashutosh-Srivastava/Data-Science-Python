# Reverse loop
from turtle import *
speed('fastest')
bgcolor('Yellow')
pencolor('black')
goto(0,0)
# penup()
for i in range(300,1,-6):
    fd(i)
    lt(360/6)
    write(i)
    circle(i)

hideturtle()
mainloop()