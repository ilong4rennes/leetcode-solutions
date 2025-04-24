# Last updated: 4/24/2025, 7:26:27 PM
class Solution:
    def countSubstrings(self, s: str) -> int:
        def expandAroundCenter(left: int, right: int) -> int:
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count

        total = 0
        for i in range(len(s)):
            total += expandAroundCenter(i, i)     # Odd-length palindromes
            total += expandAroundCenter(i, i + 1) # Even-length palindromes
        return total