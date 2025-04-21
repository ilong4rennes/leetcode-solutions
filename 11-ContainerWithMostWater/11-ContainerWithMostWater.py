# Last updated: 4/21/2025, 12:22:42 PM
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxArea = 0
        while left < right:
            leftNum, rightNum = heights[left], heights[right]
            currArea = min(leftNum, rightNum) * (right - left)
            maxArea = max(maxArea, currArea)
            if leftNum < rightNum: left += 1
            else: right -= 1
        return maxArea