num = int(input("Enter a number to find factorial of it using while loop:"))
original_num = num
fact = 1

while num > 0:
    fact *= num
    num -= 1

print("Factorial of", original_num, "=", fact) 

#using recursion:

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
num = int(input("Enter a number to find factorial using recursion:"))
print("Factorial of", num, "=", factorial(num))