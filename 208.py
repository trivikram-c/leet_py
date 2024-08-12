from collections import defaultdict as dd
class Trie:

    def __init__(self):
        self.map = {}
        

    def insert(self, word: str) -> None:
        temp = self.map
        for letter in word:
            if letter not in temp:
                temp[letter] = {}
            temp = temp[letter]
        temp[0] = 0
        

    def search(self, word: str) -> bool:
        temp = self.map
        for letter in word:
            if letter in temp: 
                temp = temp[letter]
            else: return False
        return 0 in temp

    def startsWith(self, prefix: str) -> bool:
        temp = self.map
        for letter in prefix:
            if letter in temp: temp = temp[letter]
            else: return False
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)