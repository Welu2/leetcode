class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can_cross(day: int) -> bool:
            # Create grid and mark flooded cells up to 'day' (inclusive)
            grid = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1 
                
            # BFS from top row
            queue = deque()
            for j in range(col):
                if grid[0][j] == 0:
                    queue.append((0, j))
                    grid[0][j] = 1 # Mark visited
            
            while queue:
                x, y = queue.popleft()
                if x == row - 1:
                    return True
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < row and 0 <= ny < col and grid[nx][ny] == 0:
                        grid[nx][ny] = 1
                        queue.append((nx, ny))
            return False

        # Binary search for the LAST possible day
        left, right = 1, len(cells)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if can_cross(mid):
                ans = mid      # Current day works, try for a later day
                left = mid + 1
            else:
                right = mid - 1 # Too many cells flooded, try an earlier day
                
        return ans
