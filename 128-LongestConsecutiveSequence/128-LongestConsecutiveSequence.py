# Last updated: 4/18/2025, 4:40:10 AM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        numSet = set(nums)

        for num in numSet:
            if (num - 1) not in numSet:
                curr_num = num
                curr_streak = 1
                while (curr_num + 1) in numSet:
                    curr_num += 1
                    curr_streak += 1
                max_streak = max(max_streak, curr_streak)
        
        return max_streak