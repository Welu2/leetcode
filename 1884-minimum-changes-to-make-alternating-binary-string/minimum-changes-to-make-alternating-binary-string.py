class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        if n == 1:
            return 0
        o=[]
        j=[]
        for i in range(n):
            if i % 2 != 0:
                o.append("0")
                j.append("1")
            else:
                j.append("0")
                o.append("1")
                
        def diff(s,k):
            d=0
            for i in range(n):
                if s[i] != k[i]:
                    d+=1
            return d
        return min(diff(s,o),diff(s,j))
