# Last updated: 4/18/2025, 8:55:38 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()
        t_dict = dict()
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        return s_dict == t_dict