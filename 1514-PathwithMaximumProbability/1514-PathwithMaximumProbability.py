class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list = self.transform_graph(edges, succProb)
        probs = [0] * n
        probs[start_node] = 1
        pq = [(-1, start_node)] # (-probability, node)
        heapq.heapify(pq)

        while pq:
            curr_prob, curr_node = heapq.heappop(pq)
            curr_prob = -curr_prob
            for neighbor, prob in adj_list[curr_node]:
                new_prob = curr_prob * prob
                if new_prob > probs[neighbor]:
                    probs[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        return probs[end_node]
        
    def transform_graph(self, edges, succProb):
        adj_list = defaultdict(list)
        for i in range(len(edges)):
            node1, node2 = edges[i]
            succProbability = succProb[i]
            adj_list[node1].append((node2, succProbability))
            adj_list[node2].append((node1, succProbability))
        return adj_list