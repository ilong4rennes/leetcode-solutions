# Last updated: 4/24/2025, 6:53:23 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Pair each number with its original index
        nums_indexed = [(num, i) for i, num in enumerate(nums)]
        nums_indexed.sort(key=lambda x: x[0])

        left, right = 0, len(nums_indexed) - 1
        while left < right:
            s = nums_indexed[left][0] + nums_indexed[right][0]
            if s == target:
                return [nums_indexed[left][1], nums_indexed[right][1]]
            elif s < target:
                left += 1
            else:
                right -= 1
        # If no solution found (problem guarantees one), you could raise or return []
        return []