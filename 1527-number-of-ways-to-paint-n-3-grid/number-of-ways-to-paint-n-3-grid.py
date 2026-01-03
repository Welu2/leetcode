class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        f0 = 6  # ABA type (same first and last color)
        f1 = 6  # ABC type (all different colors)
        
        for i in range(1, n):  # for rows 2 to n
            g0 = (3 * f0 + 2 * f1) % MOD
            g1 = (2 * f0 + 2 * f1) % MOD
            f0, f1 = g0, g1
        
        return (f0 + f1) % MOD