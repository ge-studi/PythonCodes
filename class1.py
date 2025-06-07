# Develop a class called TextReader which works as follows:
    
#     t= TextReader("article.txt")        # loads text from this file
#     t.text()                            # contains the entire text as string
#     t.lines                             # contains the total no. of lines in the file
#     t.wordcount                         # contains the total number of words in file
#     # t.display()                       # displays the entire text
#     t.wordlist()                        # returns a list of words (no duplicates)


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
            self.lines = []
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
        
t = TextReader("article.txt")
print(t.text())           # Entire text
print(t.lines)            # Total number of lines
print(t.wordcount)        # Total number of words
print(t.wordlist())       # Unique word list
t.display()             

