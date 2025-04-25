# Last updated: 4/24/2025, 10:04:23 PM
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1

        # First pass: fill elements less than pivot
        for num in nums:
            if num < pivot:
                result[left] = num
                left += 1

        # Second pass: fill elements greater than pivot (from the end)
        for num in reversed(nums):
            if num > pivot:
                result[right] = num
                right -= 1

        # Fill remaining space with pivot
        while left <= right:
            result[left] = pivot
            left += 1

        return result