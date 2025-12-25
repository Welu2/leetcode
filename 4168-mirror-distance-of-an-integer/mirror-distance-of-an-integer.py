class Solution:
    def mirrorDistance(self, n: int) -> int:
        def reverse(n):
            s=str(n)
            return int(s[::-1])
        return abs(n-reverse(n))      