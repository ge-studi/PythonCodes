# Write a function that would return a list of factorial values.
# For example, L = factorialList(3,6)  # get factorial of 3,4,5 into L
                                       # L = {6,24,120}

# Note: You will use the recursive factorial function

def factorial(n):
    if n == 0 or n==1:
        return 1
    return n*factorial(n-1)

def factorialList(start,end):
    return[factorial(i) for i in range (start, end)]

start = int(input("Enter the value"))
end = int(input("Enter the value"))

L=factorialList(start,end)
print("Factorial List:",L)