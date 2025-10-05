# Last updated: 10/5/2025, 7:11:16 PM
class Solution:
    class State:
        def __init__(self, node, probFromStart):
            self.node = node
            self.probFromStart = probFromStart
        
        def __lt__(self, other):
            return self.probFromStart > other.probFromStart
        
    def dijkstra(self, graph, succProb, start_node, end_node):
        probTo = [-1] * len(graph)
        pq = []
        heapq.heappush(pq, self.State(start_node, 1))
        while pq:
            state = heapq.heappop(pq)
            curNode = state.node
            curProbFromStart = state.probFromStart
            if curNode == end_node:
                return curProbFromStart
            if probTo[curNode] != -1: continue
            probTo[curNode] = curProbFromStart
            for neighbor in graph[curNode]:
                nextNode, prob = neighbor[0], neighbor[1]
                nextProbFromStart = curProbFromStart * prob
                if probTo[nextNode] != -1: continue
                heapq.heappush(pq, self.State(nextNode, nextProbFromStart))
        return 0

    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            edge = edges[i]
            prob = succProb[i]
            node1, node2 = edge[0], edge[1]
            graph[node1].append((node2, prob))
            graph[node2].append((node1, prob))
        maxProb = self.dijkstra(graph, succProb, start_node, end_node)
        return maxProb
        