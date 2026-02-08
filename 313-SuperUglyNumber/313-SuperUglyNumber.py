# Last updated: 2/7/2026, 7:07:42 PM
1class Solution:
2    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
3        heap = []
4        for prime in primes:
5            heapq.heappush(heap, (1, prime, 1))
6        ugly = [0] * (n + 1)
7        p = 1
8        while p <= n:
9            product, prime, index = heapq.heappop(heap)
10            if product != ugly[p - 1]:
11                ugly[p] = product
12                p += 1
13            heapq.heappush(heap, (ugly[index] * prime, prime, index + 1))
14        return ugly[n]