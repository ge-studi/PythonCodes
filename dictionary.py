# Load a text into dictionary of words with their frequencies
# Modify the program to
# a) Get a sorted list of words with their frequencies
# b) Get a list of words which have occurred more than once

from collections import Counter

text = input("Enter a sentence or paragraph: ")

# convert to lowercase and split into words
words = text.lower().split()
word_Freq = Counter(words) # count word frequencies

# a) Sorted list of words with their frequencies
print("\nSorted word frequencies: ")
for word in sorted(word_Freq):
    print(f"{word}: {word_Freq[word]}")

# b) List of words which have occurred more than once
print("\nWords that occurred more than once: ")
for word,freq in word_Freq.items():
    if freq > 1:
        print(f"{word}: {freq}")

