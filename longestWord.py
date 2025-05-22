# Input a sentence and display the longest word
sentence = input("Enter the sentence: ")
words = sentence.split() # Split the sentence into words
res = max(words,key=len)
print("Longest word in a sentence is: ",res)
