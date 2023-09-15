from turtle import *
# nested loop 
speed('fast')
move= 5
while True:
    for i in range(6):
        fd(100 + move)
        for i in range(6):
            fd(50)
            rt(60)
        rt(90)
    rt(5)
    move =+ 5
hideturtle()
mainloop()