import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the weighted graph
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Step 2: Initialize the min-heap and distances
        min_heap = [(0, k)]  # (distance, node)
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0  # Starting point

        # Step 3: Process the nodes using the min-heap
        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            # Skip already processed nodes (Step 5)
            # if current_dist > distances[u]:
            #     continue

            # Step 4: Update distances for adjacent vertices
            for v, weight in graph[u]:
                new_dist = current_dist + weight
                if new_dist < distances[v]:  # Update if shorter path found
                    distances[v] = new_dist
                    heapq.heappush(min_heap, (new_dist, v))

        # Step 8: Check if all vertices are reachable
        max_dist = max(distances.values())
        return max_dist if max_dist < float('inf') else -1