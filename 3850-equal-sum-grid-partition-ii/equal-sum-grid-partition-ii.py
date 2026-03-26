class Solution:
    def canPartitionGrid(self, grid: list[list[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        
        # Precompute row and column sums for O(1) partition sums
        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[r][c] for r in range(m)) for c in range(n)]

        def solve_horizontal():
            top_sum = 0
            # Track values in top/bottom sections to avoid re-scanning
            top_freq = {} 
            # Initial bottom section includes everything
            bot_freq = {}
            for r in range(m):
                for val in grid[r]:
                    bot_freq[val] = bot_freq.get(val, 0) + 1

            for i in range(m - 1): # Cut after row i
                # Move row i from bottom to top
                for val in grid[i]:
                    top_freq[val] = top_freq.get(val, 0) + 1
                    bot_freq[val] -= 1
                    if bot_freq[val] == 0: del bot_freq[val]
                
                top_sum += row_sums[i]
                bot_sum = total_sum - top_sum
                
                # Check Top section for removal
                if self.check(top_sum, bot_sum, 0, i, 0, n-1, top_freq, grid): return True
                # Check Bottom section for removal
                if self.check(bot_sum, top_sum, i+1, m-1, 0, n-1, bot_freq, grid): return True
            return False

        def solve_vertical():
            left_sum = 0
            left_freq, right_freq = {}, {}
            for r in range(m):
                for c in range(n):
                    val = grid[r][c]
                    right_freq[val] = right_freq.get(val, 0) + 1
            
            for j in range(n - 1): # Cut after column j
                for r in range(m):
                    val = grid[r][j]
                    left_freq[val] = left_freq.get(val, 0) + 1
                    right_freq[val] -= 1
                    if right_freq[val] == 0: del right_freq[val]
                
                left_sum += col_sums[j]
                right_sum = total_sum - left_sum
                
                if self.check(left_sum, right_sum, 0, m-1, 0, j, left_freq, grid): return True
                if self.check(right_sum, left_sum, 0, m-1, j+1, n-1, right_freq, grid): return True
            return False

        return solve_horizontal() or solve_vertical()

    def check(self, s_sum, target, r1, r2, c1, c2, freq, grid):
        if s_sum == target: return True
        diff = s_sum - target
        if diff <= 0: return False
        
        h, w = r2 - r1 + 1, c2 - c1 + 1
        # 2D Rule: Any cell works (if it exists in the section)
        if h > 1 and w > 1:
            return diff in freq
        # 1D Row Rule: Only endpoints
        if h == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff
        # 1D Column Rule: Only endpoints
        if w == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff
        return False
