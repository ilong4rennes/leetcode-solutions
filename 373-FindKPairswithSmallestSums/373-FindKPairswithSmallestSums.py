# Last updated: 2/6/2026, 5:26:07 PM
1class Solution:
2    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
3        heap = []
4        heapq.heapify(heap)
5        result = []
6        for i in range(min(len(nums1), k)):
7            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
8        while heapq and len(result) < k:
9            minSum, i, j = heapq.heappop(heap)
10            pair = (nums1[i], nums2[j])
11            result.append(pair)
12            if j + 1 < len(nums2):
13                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
14        return result