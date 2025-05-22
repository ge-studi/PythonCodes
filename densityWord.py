# Display the density of each word in a long sentence. The displayed words should not exist in the set of excluded words.
# However, to calculate the density, you would use the total number of words contained in the sentence.

from collections import Counter
excludedWords = {"this", "and", "is", "not", "a", "the"}
sentence = input("Enter the sentence: ")
words = sentence.lower().split()
total_Words = len(words)

words_Count = Counter(words)

print("Word densities excluding common words: ")
for word in words_Count:
    if word not in excludedWords:
        density = words_Count[word]/total_Words
        print(f"{word}: {density: .3f}")
    