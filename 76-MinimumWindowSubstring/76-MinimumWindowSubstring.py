# Last updated: 6/6/2025, 3:01:38 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, window = {}, {}
        valid = 0
        left, right = 0, 0
        length = float('inf')

        for char in t:
            need[char] = need.get(char, 0) + 1

        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window.get(c, 0) == need[c]:
                    valid += 1
            
            while left < right and valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                if d in need:
                    if window.get(d, 0) == need[d]:
                        valid -= 1
                    window[d] -= 1
        return "" if length == float('inf') else s[start: start + length]