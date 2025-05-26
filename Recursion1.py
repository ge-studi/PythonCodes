# From an input sentence, build a dictionary of words along with their frequency.
# Display the words in sorted order along with their count.

def buildFrequency(words,freq=None,index=0):
    if freq is None:
        freq = {}
    if index==len(words):
        return freq
    word = words[index]
    freq[word] = freq.get(word,0)+1
    return buildFrequency(words,freq,index+1)

sentence = input("Enter the sentence: ")
words=sentence.split()
freq_dict = buildFrequency(words)

for word in sorted(freq_dict):
    print(f"{word}:{freq_dict[word]}")