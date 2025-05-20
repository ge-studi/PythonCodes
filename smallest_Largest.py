# Write a program to input 10 numbers and display the smallest and largest of them
numbers= []
print("Enter 10 numbers: ")

for i in range(10):
    num =int(input(f"Enter number {i+1}: "))
    numbers.append(num)
smallest = min(numbers)
largest = max(numbers)
print(f"The smallest number is: ",smallest)
print(f"The largest number is: ",largest)