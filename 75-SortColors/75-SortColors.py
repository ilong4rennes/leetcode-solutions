# Last updated: 4/24/2025, 7:45:33 PM
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, curr = 0, len(nums) - 1, 0
        while curr <= right:
            leftElem, rightElem, currElem = nums[left], nums[right], nums[curr]
            if currElem == 0:
                nums[left] = currElem
                nums[curr] = leftElem
                left += 1
                curr += 1
            elif currElem == 1:
                curr += 1
            else: # currElem == 2
                nums[right] = currElem
                nums[curr] = rightElem
                right -= 1