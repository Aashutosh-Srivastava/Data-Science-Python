# Example of loops in python 

# for i in range(10):
#     print(i)

from turtle import *

# make a square 
# fd(100)
# lt(90)
# fd(100)
# lt(90)
# fd(100)
# lt(90)
# fd(100)
# lt(90)

# hideturtle()
# mainloop()


# Using speed() to control the speed 

# speed('fastest')
# for i in range(5):
#     fd(100)
#     rt(90)
#     fd(100)
#     lt(90)

# using penup() and pendown() ,goto()

speed('fastest')
penup()
goto(200,-200)
pendown()

for i in range(15):
    fd(10)
    rt(90)
    fd(10)
    lt(90)
    
    
hideturtle()
mainloop()