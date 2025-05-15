# Last updated: 5/15/2025, 5:47:23 PM
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        left, right, windowSum = 0, 0, 0
        target = sum(nums) - x
        minOps = float('inf')
        while right < len(nums):
            windowSum += nums[right]
            right += 1
            while left < right and windowSum > target:
                windowSum -= nums[left]
                left += 1
            if windowSum == target:
                minOps = min(len(nums) - (right - left), minOps)
        return -1 if minOps == float('inf') else minOps