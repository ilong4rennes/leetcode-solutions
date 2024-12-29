class Trie:

    def __init__(self):
        self.children = {}
        self.prefix_count = 0
        self.count = 0

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()
            node = node.children[c]
            node.prefix_count += 1
        node.count += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self
        for c in word:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.count

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.prefix_count

    def erase(self, word: str) -> None:
        node = self
        stack = [] # (parent_node, char in children)
        for c in word:
            if c not in node.children:
                return
            stack.append((node, c))
            node = node.children[c]
        node.count -= 1
        if node.count < 0: node.count = 0

        # Update prefix_count
        while stack:
            parent_node, char = stack.pop()
            parent_node.children[char].prefix_count -= 1
            if (parent_node.children[char].prefix_count == 0 and
                parent_node.children[char].count == 0):
                    del parent_node.children[char]
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)