# Last updated: 4/18/2025, 4:43:55 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        numset = set(nums)
        maxLength = 1
        for num in numset:
            if num - 1 not in numset:
                currLength = 1
                while num + 1 in numset:
                    num += 1
                    currLength += 1
                maxLength = max(currLength, maxLength)

        return maxLength