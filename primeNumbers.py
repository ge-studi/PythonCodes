# Write a program that generates all prime numbers between x and y
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))

print(f"Prime numbers between {x} and {y} are: ")
for num in range(x+1,y-1):
    if num > 1:
        for i in range(2,int(num **0.5) + 1):
            if num % i==0:
                break
        else:
                print(num, end= ' ')
                
            
    
    