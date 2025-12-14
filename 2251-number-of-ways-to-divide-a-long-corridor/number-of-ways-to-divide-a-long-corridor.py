class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod=10**9+7
        seats=[i for i,c in enumerate(corridor) if c== "S"]
        total=len(seats)
        if total == 0 or total % 2 == 1:
            return 0
        if total ==2:
            return 1
        ways=1
        for i in range(2,total,2):
            prev=seats[i-1]
            cur=seats[i]
            ways=(ways*(cur-prev))%mod
        return ways