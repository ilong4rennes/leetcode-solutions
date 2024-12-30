class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

    def insert(self, word):
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
        node.is_end = True
        node.count += 1
    
    def words_freq(self, prefix, result):
        node = self
        if node.is_end:
            result.append((prefix, node.count))
            # prefix = ''
        for (char, child_node) in node.children.items():
            new_prefix = prefix + char
            child_node.words_freq(new_prefix, result)
        return result

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        freq_list = trie.words_freq('', [])
        sorted_words = sorted(freq_list, key=lambda x: (-x[1], x[0]))
        return [word for word, freq in sorted_words[:k]]
