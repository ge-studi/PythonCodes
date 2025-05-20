# Write a program to check if a number is prime or not
import math
n = int(input("Enter the number: "))
if n <=1:
    print("Not a prime number ")
else:
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            print("Not a prime number ")
            break
    else:
        print("Number is prime ")