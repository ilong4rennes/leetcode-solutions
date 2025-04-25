# Last updated: 4/24/2025, 10:05:14 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1

        for num in nums:
            if num < pivot:
                result[left] = num
                left += 1

        for num in reversed(nums):
            if num > pivot:
                result[right] = num
                right -= 1

        while left <= right:
            result[left] = pivot
            left += 1

        return result