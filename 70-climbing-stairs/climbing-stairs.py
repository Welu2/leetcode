class Solution:
    def climbStairs(self, n: int) -> int:
        def F(n):
            if n == 1 or n== 0:
                return 1
           
            prev1 = 1  
            prev2 = 1  
            
            for i in range(2, n + 1):
                current = prev1 + prev2
                prev1 = prev2
                prev2 = current
            
            return prev2
        
        return F(n)

        