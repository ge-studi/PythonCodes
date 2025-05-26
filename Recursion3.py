# Make a function to calculate the factorial of a number:
# f =factorial(5)
def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)

n = int(input("Enter the number to find factorial: "))
f=factorial(n)
print(f"The factorial of {n} is:",f)