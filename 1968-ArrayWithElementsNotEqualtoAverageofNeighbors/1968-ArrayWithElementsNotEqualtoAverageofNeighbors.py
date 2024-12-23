class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        numsCopy = nums[:]
        mid = (len(nums) - 1) // 2
        end = len(nums) - 1
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = numsCopy[mid]
                mid -= 1
            else:
                nums[i] = numsCopy[end]
                end -= 1
        return nums