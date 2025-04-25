# Last updated: 4/24/2025, 10:17:56 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)