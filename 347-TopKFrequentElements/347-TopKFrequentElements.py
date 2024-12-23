class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = dict()
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heapList = []
        for num, frequency in freq.items():
            heapList.append((-frequency, num))
        heapq.heapify(heapList)
        result = []
        for i in range(k):
            freq, num = heapq.heappop(heapList)
            result.append(num)
        return result