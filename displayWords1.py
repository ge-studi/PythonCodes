# You wish to display only those words from the sentence that do not occur in a set of excluded words (eg. this, and, is, not etc.). 
# The set of excluded words would be maintained in your code, and the sentence is input from the keyboard. 
# You have to display all words that do not exist in this set, and you have to take care that multiple occurring words are displayed only once.

excluded_Words = {"this","and", "is", "not", "a", "the"}
sentence = input("Enter the sentence: ")
sentence_Words = set(sentence.lower().split()) # split sentence into words and convert to lower case to avoid case-insenstivity
filtered_Words = sentence_Words - excluded_Words # Filter words not in excluded words
print("Filtered words excluding common words: ")
for word in filtered_Words:
    print(word)
