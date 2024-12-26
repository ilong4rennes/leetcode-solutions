class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        distance = dict()
        for i in range(1, n + 1):
            distance[i] = float(inf)
        distance[k] = 0
    
        visited = deque()
        visited.append((0, k))

        while visited:
            curr_dist, node = visited.popleft()
            for next_node, weight in graph[node]:
                new_dist = curr_dist + weight
                if new_dist < distance[next_node]:
                    distance[next_node] = new_dist
                    visited.append((new_dist, next_node))
        
        max_dist = max(distance.values())
        return max_dist if max_dist < float('inf') else -1