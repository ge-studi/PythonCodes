# Make a function that inputs a string and a word, and returns the
# number of times the word occurred in the string
def countOccurrences(words,target,index = 0):
    if index == len(words):
        return 0
    count = 1 if words[index]==target else 0
    return count + countOccurrences(words,target,index+1)

sentence = input("Enter the sentence: ")
word_to_count = input("Enter words to count: ")
words=sentence.split()    # preprocessing the sentence into words
count = countOccurrences(words,word_to_count)
print(f"The word '{word_to_count}' occurred {count} time(s).")