class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for i in range(len(order)):
            order_map[order[i]] = i
        
        for i in range(len(words) - 1):
            if not self.isSorted(words[i], words[i + 1], order_map):
                return False
        return True
    
    def isSorted(self, word1, word2, order_map):
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                return order_map[word1[i]] < order_map[word2[i]]
        return len(word1) <= len(word2)