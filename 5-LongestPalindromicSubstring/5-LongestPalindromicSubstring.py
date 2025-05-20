# Last updated: 5/20/2025, 6:20:21 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            s1 = self.palindrome(i, i, s)
            s2 = self.palindrome(i, i + 1, s)
            if len(s1) > len(result): result = s1
            if len(s2) > len(result): result = s2
        return result
    
    def palindrome(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]