class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitList = self.getDigitList(digits)
        if digits == '': return []
        result = []
        self.backtracking('', result, digitList, 0, digits)
        return result
    
    def backtracking(self, path, result, digitList, index, digits):
        if index == len(digits):
            result.append(path)
            return
        options = digitList[index]
        for i in range(len(options)):
            char = options[i]
            path += char
            self.backtracking(path, result, digitList, index + 1, digits)
            path = path[:-1]
    
    def getDigitList(self, digits):
        digitDict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        digitList = []
        for digit in digits:
            digitList.append(digitDict[digit])
        return digitList