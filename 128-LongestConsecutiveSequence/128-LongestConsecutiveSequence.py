# Last updated: 4/18/2025, 4:42:55 AM
# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         if nums == []: return 0
#         numset = set(nums)
#         maxLength = 1
#         for num in nums:
#             if num - 1 not in numset:
#                 currLength = 1
#                 while num + 1 in numset:
#                     num += 1
#                     currLength += 1
#                 maxLength = max(currLength, maxLength)

#         return maxLength

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak