from turtle import *
dis = [100,100,100,100,100,100]
ngl = [90,72,42,70,66,60]

for d,a in zip(dis,ngl):
    fd(d)
    lt(a)
    
hideturtle()
mainloop()