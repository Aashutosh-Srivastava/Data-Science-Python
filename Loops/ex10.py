# using for-else concept 

from turtle import *

for i in range(6):
    if i == 5: break
    fd(100)
    rt(60)
else:
    # home()
    penup()
    goto(150,-150)
    pendown()
    write('hexagon',align = 'center')
hideturtle()
mainloop()