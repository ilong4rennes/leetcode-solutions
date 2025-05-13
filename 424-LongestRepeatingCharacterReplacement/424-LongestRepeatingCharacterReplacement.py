# Last updated: 5/14/2025, 1:49:47 AM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        left, right, result = 0, 0, 0
        maxCount = 0
        while right < len(s):
            char = s[right]
            right += 1
            window[char] += 1
            maxCount = max(maxCount, window[char])
            while right - left - maxCount > k:
                d = s[left]
                left += 1
                window[d] -= 1
            result = max(result, right - left)
        return result