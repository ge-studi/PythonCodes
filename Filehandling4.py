# You have two text files, article.txt and ignore.txt.
# Load the words of ignore.txt into a set as the words to be ignored.

# Now you have to build a dictionary of words, along with their frequencies as they occur in the article.txt after you have excluded the ignore words.

# The final result should be sorted word list which do not occur in the ignore word list. And you wish to get their frquency and density.
# Density is (frequency/total words)* 100 
 
import re 
from collections import defaultdict

def load_ignore_words(filename):
    with open(filename, 'r')as file:
        words = file.read().lower().split()
    return set(words)

def process_article(filename, ignore_words):
    with open(filename, 'r')as file:
        text = file.read().lower()
        
    # Remove punctuation and split into words
    words = re.findall(r'\b\w+\b', text)
    total_words = len(words)
    
    word_freq = defaultdict(int)
    
    for word in words:
        if word not in ignore_words:
            word_freq[word] +=1
    return word_freq,total_words

def compute_density(word_freq,total_words):
    result = []
    for word in sorted(word_freq.keys()):
        freq = word_freq[word]
        density = (freq/total_words)* 100
        result.append((word,freq,round(density,2)))
    return result

ignore_words = load_ignore_words('ignore.txt')
word_freq, total_words = process_article('article.txt',ignore_words)
results = compute_density(word_freq,total_words)

# Output
print(f"{'Word':<15} {'Frequency':<10} {'Density (%)':<12}")
print("-" * 40)
for word, freq, density in results:
    print(f"{word:<15} {freq:<10} {density:<12}")