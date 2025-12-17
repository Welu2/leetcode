class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n=len(prices)
        dp_flat_prev  = [0] * (k + 1)
        dp_long_prev  = [-inf] * (k + 1)
        dp_short_prev = [-inf] * (k + 1)

        price0 = prices[0]
        for t in range(k + 1):
            dp_long_prev[t] = -price0
            dp_short_prev[t] = price0

        for i in range(1, n):
            price = prices[i]
            dp_flat = [0] * (k + 1)
            dp_long = [-inf] * (k + 1)
            dp_short = [-inf] * (k + 1)

            for t in range(k + 1):
                best_flat = dp_flat_prev[t]

                if t + 1 <= k and dp_long_prev[t + 1] != -inf:
                    best_flat = max(best_flat, dp_long_prev[t + 1] + price)

                if t + 1 <= k and dp_short_prev[t + 1] != -inf:
                    best_flat = max(best_flat, dp_short_prev[t + 1] - price)

                dp_flat[t] = best_flat

                dp_long[t] = max(dp_long_prev[t], dp_flat_prev[t] - price)
                dp_short[t] = max(dp_short_prev[t], dp_flat_prev[t] + price)

            dp_flat_prev, dp_long_prev, dp_short_prev = dp_flat, dp_long, dp_short

        return max(dp_flat_prev)