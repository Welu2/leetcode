class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def isMagic(r, c):
            
            vals = []
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    vals.append(grid[i][j])
            if sorted(vals) != list(range(1, 10)):
                return False
            
            
            if any(sum(grid[i][c:c+3]) != 15 for i in range(r, r + 3)):
                return False
            
            if any(grid[r][j] + grid[r+1][j] + grid[r+2][j] != 15 for j in range(c, c + 3)):
                return False
            
            if (grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15 or
                grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15):
                return False
            
            return True

        
        for r in range(rows - 2):
            for c in range(cols - 2):
                
                if grid[r+1][c+1] == 5 and isMagic(r, c):
                    count += 1
        return count

