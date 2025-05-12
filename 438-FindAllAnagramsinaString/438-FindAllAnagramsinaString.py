# Last updated: 5/12/2025, 8:10:13 PM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need, window = defaultdict(int), defaultdict(int)
        left, right, valid = 0, 0, 0
        result = []
        for char in p:
            need[char] += 1

        while right < len(s):
            char = s[right]
            right += 1
            if char in need:
                window[char] += 1
                if need[char] == window[char]:
                    valid += 1
            
            while valid == len(need):
                if right - left == len(p):
                    result.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if need[d] == window[d]:
                        valid -= 1
                    window[d] -= 1
        
        return result
