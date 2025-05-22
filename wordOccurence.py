# Input a sentence and input a word. You have to find out how many times the word occured in the sentence.
sentence = input("Enter the sentence: ")
word = input("Enter the word: ")
words = sentence.split()
count=words.count(word)
print(f"The word '{word}' occurred {count} times in the sentence")