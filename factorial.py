# Write a program to calculate factorial of a number n
n = int(input("Enter the number: "))
factorial = 1
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n==0:
    print("Factorial of 0 is 1. ")
else:
    for i in range(1,n+1):
        factorial*=i
        
print(f"Factorial of {n} is {factorial}")
    

