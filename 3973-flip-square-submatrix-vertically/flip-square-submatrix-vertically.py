class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            row1 = x + i
            row2 = x + k - 1 - i
            
            # Perform the swap for each column in the submatrix
            for j in range(y, y + k):
                grid[row1][j], grid[row2][j] = grid[row2][j], grid[row1][j]
        
        return grid