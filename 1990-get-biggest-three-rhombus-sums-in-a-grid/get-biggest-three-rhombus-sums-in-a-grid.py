class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sums = set()
        
        for i in range(m):
            for j in range(n):
               
                sums.add(grid[i][j])
                
               
                for k in range(1, max(m, n)):
                  
                    if i - k < 0 or i + k >= m or j - k < 0 or j + k >= n:
                        break
                    
           
                    current_sum = grid[i - k][j] + grid[i + k][j] + grid[i][j - k] + grid[i][j + k]
                    
              
                    for d in range(1, k):
                        current_sum += grid[i - k + d][j + d] # Top to Right
                        current_sum += grid[i + k - d][j + d] # Bottom to Right
                        current_sum += grid[i - k + d][j - d] # Top to Left
                        current_sum += grid[i + k - d][j - d] # Bottom to Left
                    
                    sums.add(current_sum)
                    
        
        return sorted(list(sums), reverse=True)[:3]