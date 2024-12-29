class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0
        self.prefix_count = 0  # Add prefix_count to track words passing through this node

    def insert(self, word: str) -> None:
        node = self
        for c in word:
            if c not in node.children:
                node.children[c] = Trie()  # Create a new Trie node
            node = node.children[c]
            node.prefix_count += 1  # Increment prefix count
        node.is_end = True
        node.count += 1  # Increment word count

    def countWordsEqualTo(self, word: str) -> int:
        node = self
        for c in word:
            if c not in node.children:
                return 0  # Word not found
            node = node.children[c]
        return node.count  # Return the count of the word

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self
        for c in prefix:
            if c not in node.children:
                return 0  # Prefix not found
            node = node.children[c]
        return node.prefix_count  # Return the prefix count

    def erase(self, word: str) -> None:
        stack = []  # To keep track of nodes and characters
        node = self

        # Traverse the Trie and populate the stack
        for char in word:
            if char not in node.children:
                return  # Word doesn't exist in the Trie
            stack.append((node, char))  # Save current node and character
            node = node.children[char]

        # Decrease the word count at the last node
        node.count -= 1
        if node.count < 0:
            node.count = 0  # Ensure count doesn't go below 0

        # Decrease prefix counts and remove nodes if necessary
        while stack:
            parent, char = stack.pop()
            parent.children[char].prefix_count -= 1
            if parent.children[char].prefix_count == 0 and parent.children[char].count == 0:
                del parent.children[char]  # Remove the child node
