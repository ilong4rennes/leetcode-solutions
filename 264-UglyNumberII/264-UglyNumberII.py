import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Min-heap to store ugly numbers in ascending order
        heap = [1]
        # Set to track numbers we've already added to avoid duplicates
        seen = {1}
        
        # Prime factors for generating ugly numbers
        factors = [2, 3, 5]
        
        # Extract the nth ugly number
        for _ in range(n):
            # Pop the smallest element from the heap
            current_ugly = heapq.heappop(heap)
            
            # Generate new ugly numbers by multiplying the current number by each factor
            for factor in factors:
                new_ugly = current_ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        return current_ugly