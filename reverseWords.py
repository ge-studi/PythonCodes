# Write a program to make string from input string with words in reverse order.
# "A CAT RAN" => "RAN CAT A"
sentence = input("Enter the sentence: ")
words =sentence.split() # split into list of words
reverse_words = words[::-1] # Reverse the list
reversed_sentence = ' '.join(reverse_words)
print("Words in reverse order are: ",reversed_sentence)