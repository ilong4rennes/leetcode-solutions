# Last updated: 4/24/2025, 8:54:43 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nextNonZero = 0
        for curr in range(len(nums)):
            if nums[curr] != 0:
                nums[curr], nums[nextNonZero] = nums[nextNonZero], nums[curr]
                nextNonZero += 1