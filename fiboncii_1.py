# Write a program to display first n numbers of a fibonacii series
n = int(input("Enter how many fibonacii numbers to display: "))
count=0
a,b=0,1
print(f"First {n} Fibonacii numbers: ")
while count < n:
    print(a, end =' ')
    a,b = b,a + b
    count+=1