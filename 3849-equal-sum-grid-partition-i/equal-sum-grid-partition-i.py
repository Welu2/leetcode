class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
    
        
        row_sums = [sum(row) for row in grid]
        total_sum = sum(row_sums)
        
     
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        
       
        current_row_sum = 0
        for i in range(m - 1): 
            current_row_sum += row_sums[i]
            if current_row_sum == target:
                return True
                
      
        col_sums = [0] * n
        for r in range(m):
            for c in range(n):
                col_sums[c] += grid[r][c]
                
        current_col_sum = 0
        for j in range(n - 1): 
            current_col_sum += col_sums[j]
            if current_col_sum == target:
                return True
                
        return False
