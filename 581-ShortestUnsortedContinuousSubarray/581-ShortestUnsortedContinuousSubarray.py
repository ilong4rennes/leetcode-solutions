class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minNum, maxNum = float(inf), float(-inf)
        left, right = 0, - 1
        for i in range(len(nums)):
            maxNum = max(nums[i], maxNum)
            if nums[i] < maxNum:
                right = i
        
        for i in range(len(nums) - 1, -1, -1):
            minNum = min(nums[i], minNum)
            if nums[i] > minNum:
                left = i 
                
        return right - left + 1
        