import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        seen = set()
        seen.add(1)
        factors = [2, 3, 5]
        for _ in range(n):
            minElem = heapq.heappop(heap)
            for factor in factors:
                newNum = minElem * factor
                if newNum not in seen:
                    seen.add(newNum)
                    heapq.heappush(heap, newNum)
        return minElem
