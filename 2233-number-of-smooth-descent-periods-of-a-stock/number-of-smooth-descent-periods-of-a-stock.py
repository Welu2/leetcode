class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[1 for _ in range(n)]
        dp[0]=1
        for j in range(1,n):
            if prices[j-1] -prices[j] ==1:
                dp[j]=max(dp[j],dp[j-1]+1)

        return sum(dp)