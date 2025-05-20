# Last updated: 5/20/2025, 4:38:46 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left += 1
            right -= 1
        return s