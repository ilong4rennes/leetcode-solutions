# Last updated: 5/12/2025, 6:51:06 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, windows = defaultdict(int), defaultdict(int)
        left, right, valid = 0, 0, 0
        for char in s1:
            need[char] += 1

        while right < len(s2):
            char = s2[right]
            right += 1
            if char in need:
                windows[char] += 1
                if windows[char] == need[char]:
                    valid += 1
            
            while valid == len(need):
                if right - left == len(s1): return True
                d = s2[left]
                left += 1
                if d in need:
                    if windows[d] == need[d]:
                        valid -= 1
                    windows[d] -= 1
                    
        return False