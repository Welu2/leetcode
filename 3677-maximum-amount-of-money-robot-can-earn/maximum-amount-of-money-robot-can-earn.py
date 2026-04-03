class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
    
   
        dp = [[[-float('inf')] * 3 for _ in range(n)] for _ in range(m)]
        
        # Initialize the starting cell (0, 0)
        start_val = coins[0][0]
        dp[0][0][0] = start_val
        if start_val < 0:
            # We can use our first neutralization immediately if the start is a robber
            dp[0][0][1] = 0
            
        for r in range(m):
            for c in range(n):
                for k in range(3):
                    if dp[r][c][k] == -float('inf'):
                        continue
                    
                    # Possible moves: Right and Down
                    for dr, dc in [(0, 1), (1, 0)]:
                        nr, nc = r + dr, c + dc
                        
                        if nr < m and nc < n:
                            next_val = coins[nr][nc]
                            
                            # Option 1: Don't neutralize the next cell
                            dp[nr][nc][k] = max(dp[nr][nc][k], dp[r][c][k] + next_val)
                            
                           
                            if k < 2 and next_val < 0:
                                dp[nr][nc][k+1] = max(dp[nr][nc][k+1], dp[r][c][k])
                                
     
        return int(max(dp[m-1][n-1]))