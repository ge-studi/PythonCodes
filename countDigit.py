# Write a program to count a digit in a number
num =int(input("Enter a number"))
i= abs(num)
count=0
if i==0:
    count=1
else:
    while i>0:
        count+=1
        i//=10
print("Total number of digits in anumber",count)