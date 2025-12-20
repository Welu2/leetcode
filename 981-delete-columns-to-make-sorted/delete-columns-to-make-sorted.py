class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=len(strs[0])
        n=len(strs)
        d=0
        
        for i in range(c):
            prev=ord(strs[0][i])
            for j in range(n):
                if ord(strs[j][i] )- prev < 0:
                    d+=1
                    break
                prev=ord(strs[j][i])

        return d