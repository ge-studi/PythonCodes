# Write a function that would return a list of factorial values.
# For example, L = factorialList(3,6)  # get factorial of 3,4,5 into L
                                       # L = {6,24,120}

# Note: You will use the recursive factorial function
# Using the idea of previous solution, generate a dictionary that
# contains key:value as n:factorial where n goes from start to end.

# D=generateFactorial(5,8)
# Should return a dictionary like{5:120, 6:720,......}
# print(D[6])
# gives 720... note that 6 is a key not an index!!

def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)

def generateFactorial(start,end):
    return{i:factorial(i)for i in range(start,end)}

start = int(input("Enter the value:"))
end = int(input("Enter the value:"))

D=generateFactorial(start,end)
print("Generated Dictionary:",D)

key =int(input("Enter the key to get its factorial"))
if key in D:
    print(f"Factorial of {key} is {D[key]}")
else:
    print("Key not found in dictionary")
