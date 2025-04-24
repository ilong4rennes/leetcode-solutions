# Last updated: 4/24/2025, 6:30:26 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left].isalnum() == False: left += 1
            while left < right and s[right].isalnum() == False: right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True