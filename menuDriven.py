# Write a menu-driven program to write a program to perform basic arithmetic operations
# 1) Add
# 2) SUBTRACT
# 3) MULTIPLY
# 4) DIVIDE

num1= int(input("Enter the first number"))
num2= int(input("Enter the second number"))
choice= int(input("Enter your choice (1-4)"))
match choice:
    case 1:
        result1 =num1+num2
        print("Addition of two numbers:", result1)
    case 2:
            result2=num1-num2
            print("Subtraction of two numbers:", result2)
    case 3:
        result3 =num1*num2
        print("Multiplicationof two numbers:", result3)
    case 4:
        if num2!=0:
            result4 =num1/num2
            print("Division of two numbers:", result4)
        else:
            print("Division of zero not allowed")
    case _:
        print("Invalid choice")
        
        