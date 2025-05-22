# Display all words that are contained in the sentence. Words that come multiple times should be displayed only once.
sentence = input("Enter the sentence: ")
wordsToFind = input("Enter words: ")
# Convert sentence and words to lower case for case-insensitive matching
sentence_Words = set(sentence.lower().split()) # using set in sentence to avoid duplicates
search_Words = set(wordsToFind.lower().split()) # using set in word to avoid duplicates

# find intersection
foundWords = sentence_Words.intersection(search_Words)

# display the word in sentence without duplicates
print("Words in the sentence: ")
for word in foundWords:
    print(word)