# Write a program to check if a number is divisible by both 3 and 5
number = int(input("Enter a number"))
if number % 3 == 0 and number % 5 == 0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by 3 and 5")