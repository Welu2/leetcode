class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
    
        row_sums = [[0] * (n + 1) for _ in range(m)]
        for r in range(m):
            for c in range(n):
                row_sums[r][c + 1] = row_sums[r][c] + grid[r][c]
                
        
        col_sums = [[0] * n for _ in range(m + 1)]
        for c in range(n):
            for r in range(m):
                col_sums[r + 1][c] = col_sums[r][c] + grid[r][c]
                
        def is_magic(r, c, k):
            target = row_sums[r][c + k] - row_sums[r][c]
            
            for i in range(r + 1, r + k):
                if row_sums[i][c + k] - row_sums[i][c] != target: return False
            for j in range(c, c + k):
                if col_sums[r + k][j] - col_sums[r][j] != target: return False
            
            
            d1 = sum(grid[r + i][c + i] for i in range(k))
            if d1 != target: return False
            d2 = sum(grid[r + i][c + k - 1 - i] for i in range(k))
            return d2 == target

        for k in range(min(m, n), 1, -1):
            for r in range(m - k + 1):
                for c in range(n - k + 1):
                    if is_magic(r, c, k):
                        return k
        return 1