num = int(input("Enter your number"))
fact = 1
while num>0:
    fact*=num
    num-= 1
print(f"Factorial of number {fact}")