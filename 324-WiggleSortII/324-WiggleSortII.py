class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        numsCopy = nums[:]
        start = 0
        mid = (len(nums) - 1) // 2
        end = len(nums) - 1
        for id in range(len(nums)):
            if id % 2 == 0:
                nums[id] = numsCopy[mid]
                mid -= 1
            else:
                nums[id] = numsCopy[end]
                end -= 1