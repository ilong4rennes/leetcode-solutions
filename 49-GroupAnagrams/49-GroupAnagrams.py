# Last updated: 4/18/2025, 7:30:14 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord('a')] += 1
            strDict[tuple(key)].append(string)
        return list(strDict.values())