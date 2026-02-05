class Solution:
    def countMonobit(self, n: int) -> int:
        c=0
        for i in range(n+1):
            if len(set(bin(i)[2:])) == 1:
                c+=1
        return c