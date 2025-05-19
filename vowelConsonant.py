# Write a program to check whether entered character is a vowel or consonant
character = input("Enter a character").strip() 
if (character =='A' or character =='E' 
    or character =='I' or character =='O' or character =='U'  or character =='a' or character =='e' or character =='i' or 
    character =='o' or character =='u'):
    print("Character is a vowel")
else:
    print("Character is a consonant")