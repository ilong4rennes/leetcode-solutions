# Last updated: 8/4/2025, 4:29:00 AM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "": return []
        self.digitDict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.result = []
        self.track = []
        startIndex = 0
        self.backtrack(startIndex, digits)
        return self.result
    
    def backtrack(self, index, digits):
        if len(self.track) == len(digits):
            self.result.append(''.join(self.track[:]))
            return
        num = digits[index]
        possible_chars = self.digitDict[num]
        for char in possible_chars:
            self.track.append(char)
            self.backtrack(index + 1, digits)
            self.track.pop()