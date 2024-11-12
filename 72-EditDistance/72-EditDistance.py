class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1Len, word2Len = len(word1), len(word2)
        memo = [[0] * (word2Len + 1) for _ in range(word1Len + 1)]
        return self.helper(word1, word2, word1Len, word2Len, memo)

    def helper(self, word1, word2, word1Id, word2Id, memo):
        if word1Id == 0: return word2Id
        if word2Id == 0: return word1Id
        if memo[word1Id][word2Id]: return memo[word1Id][word2Id]

        if word1[word1Id - 1] == word2[word2Id - 1]: 
            minEditDist = self.helper(word1, word2, word1Id - 1, word2Id - 1, memo)
        else: 
            insert = self.helper(word1, word2, word1Id, word2Id - 1, memo)
            delete = self.helper(word1, word2, word1Id - 1, word2Id, memo)
            replace = self.helper(word1, word2, word1Id - 1, word2Id - 1, memo)
            minEditDist = min(insert, delete, replace) + 1
        memo[word1Id][word2Id] = minEditDist
        return minEditDist
