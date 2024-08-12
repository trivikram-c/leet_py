class WordDictionary:

    def __init__(self):
        self.map = {}
        

    def addWord(self, word: str) -> None:
        temp = self.map
        for letter in word:
            if letter not in temp:
                temp[letter] = {}
            temp = temp[letter]
        temp[0] = [0]        

    def search(self, word: str) -> bool:
        temp = self.map
        return self._dotsearch(temp, word)
    

    def _dotsearch(self, root, word):
        if not word:
            if 0 in root:  return True
            else:   return False
        out = False
        if word[0] == '.':
            for key in root.keys():
                if key == 0:
                    continue
                out |= self._dotsearch(root[key], word[1:])
                if out: return out
        else:
            out = self._dotsearch(root[word[0]], word[1:]) if word[0] in root else False
        return out
                
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)