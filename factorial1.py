# Input a number and calculate its factorial
num =float(input("Enter a number: "))
factorial =1
if num < 0 or not num.is_integer():
    print("Factorial is only defined for non-negative whole numbers.")
else:
    n = int(num)
    if n == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, n + 1):
            factorial *= i
        print(f"The factorial of {num:.2f} is: {factorial:.2f}")