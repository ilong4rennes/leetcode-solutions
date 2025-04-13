# Last updated: 4/13/2025, 9:58:13 AM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        topk_heap = []
        for (key, value) in freq_dict.items():
            heapq.heappush(topk_heap, (value, key))
        topk_list = heapq.nlargest(k, topk_heap)
        result = [num[1] for num in topk_list]
        return result