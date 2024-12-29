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

    def find_shortest_root(self, word):
        node = self
        root = []
        for c in word:
            if c not in node.children:
                break
            root.append(c)
            node = node.children[c]
            if node.is_end:
                return ''.join(root)  # Return the root as soon as it is found
        return word  # No root found, return the original word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)
        words = sentence.split()
        for i in range(len(words)):
            words[i] = trie.find_shortest_root(words[i])
        return ' '.join(words)