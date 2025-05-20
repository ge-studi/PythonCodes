# Write a program to find how times a particular digit occur in a number
num = int(input("Enter the number: "))
digit = int(input("Enter the digit you want to count: "))

i = abs(num)
count = 0
while i > 0:
    current_digit=i % 10
    if current_digit == digit:
        count+=1
    i//=10
print(f"The digit {digit} occurs {count} times in  the number {num}")