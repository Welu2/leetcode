class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low == high:
            return 1 if low % 2 !=0 else 0
        a=high-low

        if low %2 != 0 and high % 2 !=0:
            return 2+(a-((a//2)+1))
        else:
            return (a-(a//2))