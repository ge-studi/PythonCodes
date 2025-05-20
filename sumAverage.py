# Write a program to input 10 numbers and display sum and average
numbers = []
print("Enter 10 numbers")
sum=0
count=0
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
    sum+=num
    count+=1
    avg = sum/count
print("The sum of 10 numbers is: ",sum)
print("The average of 10 numbers is: ",avg)