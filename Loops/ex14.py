# Write a program to find the sum of all even numbers between 1 and 100 using a for loop.
sum = 0
for i in range(1,101):
    if i%2==0:
        sum+=i
print(f"sum of all even number from 1 to 100 is  {sum}")