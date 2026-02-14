class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [0.0] * (query_row + 2)
        dp[0] = poured

        for r in range(query_row):
            next_row = [0.0] * (query_row + 2)
            for c in range(r + 1):
                if dp[c] > 1:
                    excess = dp[c] - 1
                    next_row[c]     += excess / 2
                    next_row[c + 1] += excess / 2
            dp = next_row

        return min(1, dp[query_glass])