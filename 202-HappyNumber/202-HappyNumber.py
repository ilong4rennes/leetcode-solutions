class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set([n, 2, 3])
        newNumList = [0]
        while True:
            nums = self.getNumbers(n)
            newNum = self.sumOfSquares(nums)
            if newNum == 1: return True
            if newNum not in seen:
                seen.add(newNum)
                n = newNum
            else:
                return False
        
    def getNumbers(self, n):
        nums = []
        while n > 0:
            nums.append(n % 10)
            n = n // 10
        return nums
    
    def sumOfSquares(self, nums):
        result = 0
        for num in nums:
            result += (num ** 2)
        return result