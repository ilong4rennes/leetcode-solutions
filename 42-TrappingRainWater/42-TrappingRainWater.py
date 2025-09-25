# Last updated: 9/25/2025, 2:25:58 AM
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        result = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max: left_max = height[left]
                else: result += (left_max - height[left])
                left += 1
            else: # height[left] >= height[right]
                if height[right] >= right_max: right_max = height[right]
                else: result += (right_max - height[right])
                right -= 1
        return result