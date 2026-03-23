class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
       
        dp = [[(0, 0)] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                
                # Starting point
                if r == 0 and c == 0:
                    dp[r][c] = (val, val)
                    continue
                
                # Get possible products from the top and left cells
                candidates = []
                if r > 0:
                    candidates.extend([dp[r-1][c][0] * val, dp[r-1][c][1] * val])
                if c > 0:
                    candidates.extend([dp[r][c-1][0] * val, dp[r][c-1][1] * val])
                
                dp[r][c] = (max(candidates), min(candidates))

        max_prod = dp[m-1][n-1][0]
        
      
        return max_prod % MOD if max_prod >= 0 else -1