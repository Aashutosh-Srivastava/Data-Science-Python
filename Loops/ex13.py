# Write a program to print the multiplication table of a given number using a while loop.

num = int(input("Enter your number"))
for i in range(1,11):
    print(f"{num} * {i} = {num*i}")