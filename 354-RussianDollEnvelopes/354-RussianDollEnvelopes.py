# Last updated: 1/8/2026, 2:37:14 AM
1class Solution:
2    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
3        envelopes.sort(key=lambda x:(x[0], -x[1]))
4        heights = [envelopes[i][1] for i in range(len(envelopes))]
5        return self.lengthOfLIS(heights)
6    
7    def lengthOfLIS(self, nums):
8        piles = 0
9        n = len(nums)
10        top = [0] * n
11        for i in range(n):
12            poker = nums[i]
13            left, right = 0, piles
14            while left < right:
15                mid = (left + right) // 2
16                if top[mid] >= poker:
17                    right = mid
18                else:
19                    left = mid + 1
20            if left == piles:
21                piles += 1
22            top[left] = poker
23        return piles