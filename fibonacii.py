# Display the fibonacii series up to a maximum limit
limit = int(input("Enter the maximum limit"))

a,b = 0,1
print("Fibonacii series upto", limit, ":")
while a <= limit:
    print(a, end=' ')
    a,b = b,a + b
    