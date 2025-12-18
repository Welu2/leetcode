class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        base = 0
        for i in range(n):
            base += strategy[i] * prices[i]

        first = [0] * n
        second = [0] * n
        for i in range(n):
            first[i] = -strategy[i] * prices[i]
            second[i] = (1 - strategy[i]) * prices[i]

        pf1 = [0] * (n + 1)
        pf2 = [0] * (n + 1)
        for i in range(n):
            pf1[i + 1] = pf1[i] + first[i]
            pf2[i + 1] = pf2[i] + second[i]

        best_gain = 0
        half = k // 2
        for L in range(0, n - k + 1):
            mid = L + half
            R = L + k

            first_half_gain = pf1[mid] - pf1[L]
            second_half_gain = pf2[R] - pf2[mid]
            gain = first_half_gain + second_half_gain

            if gain > best_gain:
                best_gain = gain

        return base + best_gain