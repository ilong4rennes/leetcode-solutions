# Last updated: 6/28/2025, 2:59:57 PM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        for c in s1:
            s1_dict[c] += 1
        window = defaultdict(int)
        left, right = 0, 0
        correct = 0
        while right < len(s2):
            c = s2[right]
            if c in s1_dict.keys():
                window[c] += 1
                if window[c] == s1_dict[c]:
                    correct += 1
            right += 1
            while correct == len(s1_dict):
                if right - left == len(s1):
                    return True
                d = s2[left]
                if d in s1_dict.keys():
                    if window[d] == s1_dict[d]:
                        correct -= 1
                    window[d] -= 1
                left += 1
        return False