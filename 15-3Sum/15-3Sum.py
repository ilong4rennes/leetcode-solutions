# Last updated: 4/22/2025, 8:28:05 PM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]: continue
            mid, right = left + 1, len(nums) - 1
            while mid < right:
                sum_of_3 = nums[left] + nums[mid] + nums[right]
                if sum_of_3 == 0:
                    result.add((nums[left], nums[mid], nums[right]))
                    mid += 1
                    right -= 1
                elif sum_of_3 < 0:
                    mid += 1
                else:
                    right -= 1
        return [list(triplet) for triplet in result]