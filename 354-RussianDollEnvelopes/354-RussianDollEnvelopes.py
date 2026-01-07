# Last updated: 1/8/2026, 1:52:17 AM
1class Solution:
2    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
3        n = len(envelopes)
4        envelopes.sort(key=lambda x: (x[0], -x[1]))
5        height = [envelopes[i][1] for i in range(n)]
6        return self.lengthOfLIS(height)
7        
8    def lengthOfLIS(self, nums: List[int]) -> int:
9        piles = 0
10        n = len(nums)
11        top = [0] * n
12        for i in range(n):
13            poker = nums[i]
14            left, right = 0, piles
15            while left < right:
16                mid = (left + right) // 2
17                if top[mid] >= poker:
18                    right = mid
19                else:
20                    left = mid + 1
21            if left == piles: 
22                piles += 1
23            top[left] = poker
24        return piles