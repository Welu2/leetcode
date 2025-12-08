class Solution:
    def countTriples(self, n: int) -> int:
        d={i*i:i for i in range(1,n+1)}
        ans=0

        for j in range(1,n+1):
            for k in range(1,n+1):
                if j == k:
                    continue
                else:
                    t=j**2 +k **2 
                    if t in d:
                        ans+=1

        return ans

