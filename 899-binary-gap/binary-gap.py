class Solution:
    def binaryGap(self, n: int) -> int:
        d=0
        j=bin(n)[2:]
        k=j.index("1")
        l=k
        for i in range(k+1,len(j)):
            if j[i] == "1":
                d=max(d,i-l)
                l=i
        return d