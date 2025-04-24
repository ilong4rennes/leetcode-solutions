# Last updated: 4/24/2025, 6:58:35 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_indexed = [(num, index) for index, num in enumerate(nums)]
        nums_indexed.sort(key=lambda x:x[0])

        left, right = 0, len(nums_indexed) - 1
        while left < right:
            sum_of_2 = nums_indexed[left][0] + nums_indexed[right][0]
            if sum_of_2 == target:
                return [nums_indexed[left][1], nums_indexed[right][1]]
            elif sum_of_2 <= target:
                left += 1
            else: 
                right -= 1