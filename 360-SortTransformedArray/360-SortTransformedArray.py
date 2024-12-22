class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        nums = self.quadratic_transformation(nums, a, b, c)
        return self.sort_array(nums)

    def quadratic_transformation(self, nums, a, b, c):
        result = []
        for num in nums:
            new_num = a * num ** 2 + b * num + c
            result.append(new_num)
        return result
    
    def sort_array(self, nums):
        if len(nums) <= 1: return nums
        mid = len(nums) // 2
        left = self.sort_array(nums[:mid])
        right = self.sort_array(nums[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
