class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
    
        m, n = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        
        # Step 1: Group elements by their diagonals
        for i in range(m):
            for j in range(n):
                diagonals[i - j].append(mat[i][j])
        
        # Step 2: Sort each diagonal
        for key in diagonals:
            diagonals[key].sort()
        
        # Step 3: Rewrite the matrix with sorted diagonals
        for i in range(m):
            for j in range(n):
                mat[i][j] = diagonals[i - j].pop(0)
        
        return mat