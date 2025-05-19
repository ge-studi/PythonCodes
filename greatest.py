# Write a program to find the greatest among three numbers entered by the user
number1 =int(input("Enter the first number"))
number2 = int(input("Enter the second number"))
number3 = int(input("Enter the third number"))
if number1>number2 and number1>number3:
    print("First number is the largest")
elif number2>number1 and number2>number3:
    print("Second number is the largest")
else:
    print("Third number is the largest")