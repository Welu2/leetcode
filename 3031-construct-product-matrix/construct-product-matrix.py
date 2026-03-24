class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        MOD = 12345
        total_elements = n * m
        
      
        flat_grid = [grid[r][c] for r in range(n) for c in range(m)]
        p = [1] * total_elements
        
      
        curr_prefix = 1
        for i in range(total_elements):
            p[i] = curr_prefix
            curr_prefix = (curr_prefix * flat_grid[i]) % MOD
            
        
        curr_suffix = 1
        for i in range(total_elements - 1, -1, -1):
            p[i] = (p[i] * curr_suffix) % MOD
            curr_suffix = (curr_suffix * flat_grid[i]) % MOD
     
        result = []
        for i in range(0, total_elements, m):
            result.append(p[i : i + m])
            
        return result
            