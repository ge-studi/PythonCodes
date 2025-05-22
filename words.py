# Get a list of words with their count in a sentence. The words should be in sorted order alphabetically.
# Words should not be repeated. Assume space as a separator for words.
sentence = input("Enter the sentence: ")
words =sentence.split() # split into list of words
uniqueWords=sorted(set(words)) # Get unique words, then sort aphabetically
print("Count of words in a sentence: ")
for word in uniqueWords:
    print(f"{word}: {words.count(word)}")