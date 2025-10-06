# Last updated: 10/5/2025, 8:06:40 PM
class Solution:
    class State:
        def __init__(self, node, priceFromStart, stopFromStart):
            self.node = node
            self.priceFromStart = priceFromStart
            self.stopFromStart = stopFromStart
        
        def __lt__(self, other):
            return self.priceFromStart < other.priceFromStart
        
    def dijkstra(self, graph, src, dst, k):
        priceTo = [-1] * len(graph)
        stopTo = [float('inf')] * len(graph)
        pq = []
        heapq.heappush(pq, self.State(src, 0, 0))
        while pq:
            state = heapq.heappop(pq)
            curNode = state.node
            curPriceFromStart = state.priceFromStart
            curStopFromStart = state.stopFromStart
            
            if curStopFromStart > k: continue
            if curNode == dst: return curPriceFromStart
            if curPriceFromStart >= priceTo[curNode] and curStopFromStart >= stopTo[curNode]: continue
            
            # priceTo[curNode] = curPriceFromStart
            # stopTo[curNode] = curStopFromStart
            if priceTo[curNode] == -1 or curPriceFromStart < priceTo[curNode]:
                priceTo[curNode] = curPriceFromStart
            if curStopFromStart < stopTo[curNode]:
                stopTo[curNode] = curStopFromStart
            
            for neighbor in graph[curNode]:
                nextNode, price = neighbor
                nextPriceFromStart = curPriceFromStart + price
                nextStopFromStart = curStopFromStart + 1
                if nextStopFromStart > k: 
                    continue
                if priceTo[nextNode] != -1 and nextPriceFromStart >= priceTo[nextNode] and nextStopFromStart >= stopTo[nextNode]:
                    continue
                heapq.heappush(pq, self.State(nextNode, nextPriceFromStart, nextStopFromStart))
        return -1

    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for flight in flights:
            _from, _to, price = flight
            graph[_from].append((_to, price))
        return self.dijkstra(graph, src, dst, k + 1)