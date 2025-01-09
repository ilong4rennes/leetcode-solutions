class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        seen = set()
        seen.add(1)
        factors = [2, 3, 5]
        for i in range(n):
            minElem = heapq.heappop(heap)
            for factor in factors:
                newElem = minElem * factor
                if newElem not in seen:
                    heapq.heappush(heap, newElem)
                    seen.add(newElem)
        return minElem