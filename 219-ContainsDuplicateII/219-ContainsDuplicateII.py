# Last updated: 4/24/2025, 10:35:22 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        id_dict = {}
        for index, num in enumerate(nums):
            if num in id_dict and abs(index - id_dict[num]) <= k:
                return True
            id_dict[num] = index
        return False