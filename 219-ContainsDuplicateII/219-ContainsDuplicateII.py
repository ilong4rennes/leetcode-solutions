# Last updated: 4/24/2025, 10:33:50 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        id_dict = {}
        for index, num in enumerate(nums):
            last_id = id_dict.get(num, -1)
            if last_id != -1 and abs(index - last_id) <= k:
                return True
            id_dict[num] = index
        return False