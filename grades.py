# Write a program to assign grades based on marks using the following logic:
# If marks >=90 --> Grade A
# If marks >=75 --> Grade B
# If marks >=60 --> Grade C
# If marks >=40 --> Grade D
# ELSE GRADE F

marks = int(input("Enter your marks"))
if marks>=90: print("Grade A")
elif marks>=75: print("Grade B")
elif marks>=60: print("Grade C")
elif marks>=40: print("Grade D")
else: print("Grade F")