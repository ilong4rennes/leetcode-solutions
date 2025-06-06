# Last updated: 6/6/2025, 3:02:30 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, need = {}, {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        left, right = 0, 0
        valid = 0
        length = float('inf')
        start = 0
        while right < len(s):
            c = s[right]
            right += 1
            # update window
            if c in need: 
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]: 
                    valid += 1
            while left < right and valid == len(need):
                # update the minimum substring
                if right - left < length:
                    start = left
                    length = right - left
                d = s[left]
                left += 1
                # update window
                if d in need: 
                    # window[d] -= 1
                    if window[d] == need[d]: 
                        valid -= 1
                    window[d] -= 1
        return '' if length == float('inf') else s[start : start + length]