class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for a, b in edges:
            if self.foundCycle(adj_list, a, b, None):  
                return [a, b] 

            adj_list[a].append(b)
            adj_list[b].append(a)

        return []

    def foundCycle(self, adj_list, node, target, parent):
        """DFS to check if there's a path from node to target, ignoring the parent."""
        if node == target:
            return True  # Cycle found
        
        for neighbor in adj_list[node]:
            if (neighbor != parent and 
                self.foundCycle(adj_list, neighbor, target, node)):
                    return True
        
        return False
