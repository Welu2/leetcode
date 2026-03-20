class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans_rows, ans_cols = m - k + 1, n - k + 1
        ans = [[0] * ans_cols for _ in range(ans_rows)]
        
        for i in range(ans_rows):
            for j in range(ans_cols):
                # 1. Collect all elements in the current k x k submatrix
                elements = set()
                for r in range(i, i + k):
                    for c in range(j, j + k):
                        elements.add(grid[r][c])
                
                # 2. Sort the distinct elements
                unique_elements = sorted(list(elements))
                
                # 3. Handle cases with fewer than 2 distinct elements
                if len(unique_elements) < 2:
                    ans[i][j] = 0
                else:
                    # 4. Find the minimum difference between adjacent sorted unique values
                    min_diff = float('inf')
                    for idx in range(len(unique_elements) - 1):
                        diff = unique_elements[idx+1] - unique_elements[idx]
                        if diff < min_diff:
                            min_diff = diff
                    ans[i][j] = min_diff
                    
        return ans