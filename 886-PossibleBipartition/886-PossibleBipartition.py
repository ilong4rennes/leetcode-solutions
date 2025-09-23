# Last updated: 9/23/2025, 2:18:08 AM
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = self.buildGraph(n, dislikes)
        return self.isBipartite(graph)

    def buildGraph(self, n, dislikes):
        graph = [[] for _ in range(n)]
        for dislike in dislikes:
            a, b = dislike[0], dislike[1]
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        return graph
        
    def isBipartite(self, graph: List[List[int]]) -> bool:
        self.colors = ["BLUE", "RED"]
        self.visited = [False for _ in range(len(graph))]
        self.colorGraph = [None for _ in range(len(graph))]
        for node in range(len(graph)):
            if not self.visited[node]:
                isPossible = self.traverse(graph, node, "BLUE")
                if not isPossible: return False
        return True

    def traverse(self, graph, start, color):
        self.visited[start] = True
        self.colorGraph[start] = color
        neighbors = graph[start]
        for neighbor in neighbors:
            if not self.visited[neighbor]:
                newColor = "RED" if color == "BLUE" else "BLUE"
                isPossible = self.traverse(graph, neighbor, newColor)
                if not isPossible: return False
            else:
                if color != self.colorGraph[neighbor]:
                    pass
                else:
                    return False
        return True