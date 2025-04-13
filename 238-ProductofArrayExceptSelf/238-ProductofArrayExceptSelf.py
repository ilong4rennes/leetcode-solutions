# Last updated: 4/13/2025, 6:00:46 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1] * n
        R = [1] * n
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
        for i in range(n-2, -1, -1):
            R[i] = R[i+1] * nums[i+1]
        result = [L[i]*R[i] for i in range(n)]
        return result