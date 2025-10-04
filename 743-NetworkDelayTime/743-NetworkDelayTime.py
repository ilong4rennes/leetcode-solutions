# Last updated: 10/4/2025, 4:54:42 PM
class Solution:
    class State:
        def __init__(self, node, distFromStart):
            self.node = node
            self.distFromStart = distFromStart
        
        def __lt__(self, other):
            return self.distFromStart < other.distFromStart

    def dijkstra(self, graph, src):
        distTo = [-1] * len(graph)
        pq = []
        heapq.heappush(pq, self.State(src, 0))
        
        while pq:
            state = heapq.heappop(pq)
            curNode = state.node
            curDistFromStart = state.distFromStart
            if distTo[curNode] != -1: continue
            distTo[curNode] = curDistFromStart
            for neighbor in graph[curNode]:
                nextNode = neighbor[0]
                nextDistFromStart = curDistFromStart + neighbor[1]
                if distTo[nextNode] != -1: continue
                heapq.heappush(pq, self.State(nextNode, nextDistFromStart))
        return distTo

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        for _from, _to, weight in times:
            graph[_from].append([_to, weight])
        distTo = self.dijkstra(graph, k)
        for i in range(1, n + 1):
            if distTo[i] == -1: return -1
        return max(distTo)

        