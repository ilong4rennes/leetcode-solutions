# Last updated: 6/29/2025, 3:51:39 PM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        need = defaultdict(int)
        for c in p:
            need[c] += 1
        window = defaultdict(int)
        left, right, correct = 0, 0, 0
        while right < len(s):
            c = s[right]
            if c in need.keys():
                window[c] += 1
                if window[c] == need[c]:
                    correct += 1
            right += 1
            while correct == len(need):
                if right - left == len(p):
                    result.append(left)
                d = s[left]
                if d in need.keys():
                    if window[d] == need[d]:
                        correct -= 1
                    window[d] -= 1
                left += 1
        return result