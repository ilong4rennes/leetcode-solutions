class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, source: int) -> int:
        distances = [float('inf')] * (n + 1)
        distances[source] = 0
        pq = [(0, source)] # (distance, node)
        heapq.heapify(pq)
        adj_list = self.transform_graph(times)

        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > distances[curr_node]: continue
            for neighbor, weight in adj_list[curr_node]:
                new_dist = distances[curr_node] + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        return max(distances[1:]) if max(distances[1:]) != float('inf') else -1
    
    def transform_graph(self, times):
        adj_list = defaultdict(list)
        for source, target, weight in times:
            adj_list[source].append((target, weight))
        return adj_list