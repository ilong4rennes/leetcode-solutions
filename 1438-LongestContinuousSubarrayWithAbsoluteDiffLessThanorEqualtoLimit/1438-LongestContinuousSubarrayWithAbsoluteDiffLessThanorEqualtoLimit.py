class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque, max_deque = deque(), deque()
        left = 0
        result = 0
        for right in range(len(nums)):
            while min_deque and min_deque[-1] > nums[right]:
                min_deque.pop()
            min_deque.append(nums[right])
            while max_deque and max_deque[-1] < nums[right]:
                max_deque.pop()
            max_deque.append(nums[right])

            while max_deque[0] - min_deque[0] > limit:
                if max_deque[0] == nums[left]: 
                    max_deque.popleft()
                if min_deque[0] == nums[left]: 
                    min_deque.popleft()
                left += 1
            result = max(result, right - left + 1)

        return result