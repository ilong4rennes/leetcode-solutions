class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
    
    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.is_end = True
    
    def trim(self, word):
        node = self
        chars = []
        for c in word:
            if c not in node.children:
                break
            chars.append(c)
            node = node.children[c]
            if node.is_end:
                return ''.join(chars)
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        words = sentence.split()
        for i in range(len(words)):
            words[i] = trie.trim(words[i])
        return ' '.join(words)
