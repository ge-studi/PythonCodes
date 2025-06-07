# In the class created previously, add a function getWC() to get the count of some words which can be provided through a list
# sent as parameter. The usage of this function would be as follows

# d = t.getWC(wordList)       # wordList is a 'list' of words
#                             # return a dictionary {word:count} using
#                             # the words from the wordList

class TextReader:
    def __init__(self,filename):
        self.filename = filename
        self._load_text()
        
    def _load_text(self):
        try:
            with open(self.filename, 'r',encoding='utf-8') as file:
                self._text = file.read()
                self._lines = self._text.strip().split('\n')
                self._words = self._text.split()
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")
            self._text = ''
            self._lines = []
            self._words = []
            
    def text(self):
        """Returns the entire text as single string"""
        return self._text
    
    @property
    def lines(self):
        return len(self._lines)
    @property
    def wordcount(self):
        return len(self._words) 
    
    def wordlist(self):
        return list(set(self._words))
    
    def display(self):
        print(self._text)
        
    def getWC(self,wordList):
        from collections import Counter
        word_freq = Counter(self._words)
        return {word: word_freq.get(word,0) for word in wordList}
        
t = TextReader("article.txt")
d = t.getWC(t.wordlist())
print(d)          

