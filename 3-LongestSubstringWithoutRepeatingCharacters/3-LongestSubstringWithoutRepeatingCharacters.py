# Last updated: 6/29/2025, 4:21:39 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left, right = 0, 0
        maxLen = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] -= 1
            maxLen = max(maxLen, right - left)
        return maxLen