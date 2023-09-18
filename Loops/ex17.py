# Write a program to print the Fibonacci series up to a given limit using a while loop.
n = int(input("enter your number"))
x = 0
y = 1
z = 0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y