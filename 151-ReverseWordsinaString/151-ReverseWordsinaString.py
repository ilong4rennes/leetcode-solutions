# Last updated: 11/12/2025, 11:19:05 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for word in s.split():
            res.append(word)
        return " ".join(res[::-1])